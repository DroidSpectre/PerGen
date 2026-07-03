#!/usr/bin/env python3
"""
Universal CSV to JSONL Converter v4 - Any Size, Any Format
Enhanced version that handles CSV files of any size with flexible column mapping
Optimized for memory efficiency and scalability
"""

import csv
import json
import os
import argparse
import sys
from typing import List, Dict, Any, Optional, Iterator
from pathlib import Path
import time

class CSVToJSONLConverter:
    """
    Universal CSV to JSONL converter with memory-efficient streaming
    """

    def __init__(self, chunk_size: int = 1000):
        self.chunk_size = chunk_size
        self.supported_schemas = {
            'alpaca': ['instruction', 'input', 'output'],
            'chat': ['messages', 'conversation'],
            'qa': ['question', 'answer'],
            'text': ['text', 'content'],
            'custom': []  # User-defined
        }

    def detect_schema(self, fieldnames: List[str]) -> tuple[str, Dict[str, str]]:
        """
        Auto-detect the best schema and create column mapping
        Returns: (schema_name, column_mapping)
        """
        fieldnames_lower = [f.lower().strip() for f in fieldnames]

        # Check for Alpaca format (instruction, input, output)
        alpaca_matches = {
            'instruction': self._find_column(fieldnames_lower, ['instruction', 'inst', 'task', 'prompt']),
            'input': self._find_column(fieldnames_lower, ['input', 'context', 'system', 'user_input']),
            'output': self._find_column(fieldnames_lower, ['output', 'response', 'answer', 'target', 'completion'])
        }

        if alpaca_matches['instruction'] and alpaca_matches['output']:
            return 'alpaca', {
                'instruction': fieldnames[alpaca_matches['instruction']],
                'input': fieldnames[alpaca_matches['input']] if alpaca_matches['input'] is not None else None,
                'output': fieldnames[alpaca_matches['output']]
            }

        # Check for Q&A format
        qa_matches = {
            'question': self._find_column(fieldnames_lower, ['question', 'q', 'query', 'prompt', 'instruction']),
            'answer': self._find_column(fieldnames_lower, ['answer', 'a', 'response', 'output', 'completion'])
        }

        if qa_matches['question'] and qa_matches['answer']:
            return 'qa', {
                'question': fieldnames[qa_matches['question']],
                'answer': fieldnames[qa_matches['answer']]
            }

        # Check for simple text format
        text_match = self._find_column(fieldnames_lower, ['text', 'content', 'data', 'message'])
        if text_match is not None:
            return 'text', {'text': fieldnames[text_match]}

        # Default: use first column as text
        return 'text', {'text': fieldnames[0]}

    def _find_column(self, fieldnames_lower: List[str], candidates: List[str]) -> Optional[int]:
        """Find the best matching column index"""
        for candidate in candidates:
            for i, field in enumerate(fieldnames_lower):
                if candidate in field or field in candidate:
                    return i
        return None

    def stream_csv_rows(self, csv_path: str) -> Iterator[Dict[str, Any]]:
        """
        Memory-efficient streaming of CSV rows
        """
        try:
            with open(csv_path, 'r', encoding='utf-8', newline='') as csvfile:
                # Detect delimiter
                sample = csvfile.read(1024)
                csvfile.seek(0)
                delimiter = csv.Sniffer().sniff(sample).delimiter

                reader = csv.DictReader(csvfile, delimiter=delimiter)

                for row_num, row in enumerate(reader, 1):
                    # Clean row data
                    cleaned_row = {k: v.strip() if v else "" for k, v in row.items()}
                    yield row_num, cleaned_row, reader.fieldnames

        except Exception as e:
            print(f"Error reading CSV {csv_path}: {e}")
            return

    def convert_to_jsonl(self, csv_path: str, jsonl_path: str, 
                        schema: str = 'auto', 
                        custom_mapping: Dict[str, str] = None,
                        max_rows: int = None) -> Dict[str, Any]:
        """
        Convert CSV to JSONL with streaming for memory efficiency
        """
        stats = {
            'total_rows': 0,
            'converted_rows': 0,
            'skipped_rows': 0,
            'errors': 0,
            'schema': schema,
            'file_size_mb': 0
        }

        print(f"Converting {csv_path} to {jsonl_path}...")
        print(f"Max rows: {'unlimited' if max_rows is None else max_rows:,}")

        # Get file size
        stats['file_size_mb'] = os.path.getsize(csv_path) / (1024 * 1024)
        print(f"Input file size: {stats['file_size_mb']:.2f} MB")

        start_time = time.time()

        try:
            with open(jsonl_path, 'w', encoding='utf-8') as jsonl_file:
                fieldnames = None
                column_mapping = None
                detected_schema = None

                for row_num, row, current_fieldnames in self.stream_csv_rows(csv_path):
                    stats['total_rows'] += 1

                    # Initialize schema detection on first row
                    if fieldnames is None:
                        fieldnames = current_fieldnames

                        if schema == 'auto':
                            detected_schema, column_mapping = self.detect_schema(fieldnames)
                            stats['schema'] = detected_schema
                        elif custom_mapping:
                            detected_schema = 'custom'
                            column_mapping = custom_mapping
                        else:
                            detected_schema = schema
                            column_mapping = self._get_default_mapping(schema, fieldnames)

                        print(f"Detected schema: {detected_schema}")
                        print(f"Column mapping: {column_mapping}")

                    # Check max rows limit
                    if max_rows and stats['total_rows'] > max_rows:
                        print(f"Reached max rows limit: {max_rows:,}")
                        break

                    # Convert row based on schema
                    try:
                        json_obj = self._convert_row_to_json(row, detected_schema, column_mapping)
                        if json_obj:
                            jsonl_file.write(json.dumps(json_obj, ensure_ascii=False) + '\n')
                            stats['converted_rows'] += 1
                        else:
                            stats['skipped_rows'] += 1
                    except Exception as e:
                        print(f"Error processing row {row_num}: {e}")
                        stats['errors'] += 1
                        stats['skipped_rows'] += 1

                    # Progress reporting for large files
                    if stats['total_rows'] % 10000 == 0:
                        elapsed = time.time() - start_time
                        rate = stats['total_rows'] / elapsed
                        print(f"Processed {stats['total_rows']:,} rows ({rate:.0f} rows/sec)")

        except Exception as e:
            print(f"Critical error: {e}")
            stats['errors'] += 1
            return stats

        # Final statistics
        elapsed = time.time() - start_time
        stats['processing_time'] = elapsed
        stats['rows_per_second'] = stats['total_rows'] / elapsed if elapsed > 0 else 0

        print(f"\nConversion completed in {elapsed:.2f} seconds")
        print(f"Rate: {stats['rows_per_second']:.0f} rows/second")
        print(f"Total: {stats['total_rows']:,} | Converted: {stats['converted_rows']:,} | Skipped: {stats['skipped_rows']:,}")

        return stats

    def _get_default_mapping(self, schema: str, fieldnames: List[str]) -> Dict[str, str]:
        """Get default column mapping for known schemas"""
        if schema == 'alpaca' and len(fieldnames) >= 3:
            return {
                'instruction': fieldnames[0],
                'input': fieldnames[1] if len(fieldnames) > 1 else None,
                'output': fieldnames[-1]  # Last column is usually output
            }
        elif schema == 'qa' and len(fieldnames) >= 2:
            return {
                'question': fieldnames[0],
                'answer': fieldnames[1]
            }
        elif schema == 'text':
            return {'text': fieldnames[0]}
        else:
            return {'text': fieldnames[0]}

    def _convert_row_to_json(self, row: Dict[str, str], schema: str, mapping: Dict[str, str]) -> Optional[Dict[str, Any]]:
        """Convert a CSV row to JSON based on schema"""

        if schema == 'alpaca':
            instruction = row.get(mapping['instruction'], '').strip()
            output = row.get(mapping['output'], '').strip()

            if not instruction or not output:
                return None

            json_obj = {
                'instruction': instruction,
                'input': row.get(mapping['input'], '').strip() if mapping.get('input') else '',
                'output': output
            }
            return json_obj

        elif schema == 'qa':
            question = row.get(mapping['question'], '').strip()
            answer = row.get(mapping['answer'], '').strip()

            if not question or not answer:
                return None

            return {
                'question': question,
                'answer': answer
            }

        elif schema == 'text':
            text = row.get(mapping['text'], '').strip()
            if not text:
                return None
            return {'text': text}

        elif schema == 'custom':
            json_obj = {}
            for json_key, csv_column in mapping.items():
                if csv_column in row:
                    value = row[csv_column].strip()
                    if value:  # Only include non-empty values
                        json_obj[json_key] = value
            return json_obj if json_obj else None

        return None

    def batch_convert(self, input_dir: str, output_dir: str = None, 
                     pattern: str = "*.csv", schema: str = 'auto',
                     max_rows_per_file: int = None) -> Dict[str, Dict[str, Any]]:
        """
        Convert multiple CSV files in batch
        """
        input_path = Path(input_dir)
        output_path = Path(output_dir or input_dir)
        output_path.mkdir(exist_ok=True)

        csv_files = list(input_path.glob(pattern))
        if not csv_files:
            print(f"No CSV files found in {input_dir} matching {pattern}")
            return {}

        print(f"\n🔄 BATCH CONVERTING {len(csv_files)} CSV FILES")
        print("=" * 60)

        results = {}
        total_stats = {
            'total_files': len(csv_files),
            'successful': 0,
            'failed': 0,
            'total_rows_processed': 0,
            'total_rows_converted': 0
        }

        for csv_file in csv_files:
            jsonl_file = output_path / (csv_file.stem + '.jsonl')

            print(f"\n[{csv_files.index(csv_file) + 1}/{len(csv_files)}] Processing {csv_file.name}")

            stats = self.convert_to_jsonl(
                str(csv_file), 
                str(jsonl_file), 
                schema=schema,
                max_rows=max_rows_per_file
            )

            results[csv_file.name] = stats

            if stats['converted_rows'] > 0:
                total_stats['successful'] += 1
                total_stats['total_rows_processed'] += stats['total_rows']
                total_stats['total_rows_converted'] += stats['converted_rows']
            else:
                total_stats['failed'] += 1

        # Print summary
        print(f"\n📊 BATCH CONVERSION SUMMARY")
        print("=" * 50)
        print(f"Files processed: {total_stats['total_files']}")
        print(f"Successful: {total_stats['successful']}")
        print(f"Failed: {total_stats['failed']}")
        print(f"Total rows processed: {total_stats['total_rows_processed']:,}")
        print(f"Total rows converted: {total_stats['total_rows_converted']:,}")

        return results

def main():
    """Main function with comprehensive CLI"""
    parser = argparse.ArgumentParser(description="Universal CSV to JSONL Converter - Any Size, Any Format")

    parser.add_argument('input', help='Input CSV file or directory')
    parser.add_argument('-o', '--output', help='Output JSONL file or directory')
    parser.add_argument('--schema', choices=['auto', 'alpaca', 'qa', 'text', 'custom'], 
                       default='auto', help='Output schema format')
    parser.add_argument('--mapping', help='Custom column mapping (JSON format)')
    parser.add_argument('--max-rows', type=int, help='Maximum rows to convert per file')
    parser.add_argument('--chunk-size', type=int, default=1000, 
                       help='Chunk size for processing (default: 1000)')
    parser.add_argument('--batch', action='store_true', 
                       help='Batch process all CSV files in directory')
    parser.add_argument('--pattern', default='*.csv', 
                       help='File pattern for batch processing')

    args = parser.parse_args()

    # Initialize converter
    converter = CSVToJSONLConverter(chunk_size=args.chunk_size)

    print("🚀 UNIVERSAL CSV TO JSONL CONVERTER v4")
    print("=" * 60)
    print(f"Input: {args.input}")
    print(f"Schema: {args.schema}")
    print(f"Max rows per file: {'unlimited' if not args.max_rows else args.max_rows:,}")
    print(f"Chunk size: {args.chunk_size:,}")

    # Parse custom mapping if provided
    custom_mapping = None
    if args.mapping:
        try:
            custom_mapping = json.loads(args.mapping)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON mapping: {args.mapping}")
            sys.exit(1)

    if args.batch or os.path.isdir(args.input):
        # Batch processing
        results = converter.batch_convert(
            input_dir=args.input,
            output_dir=args.output,
            pattern=args.pattern,
            schema=args.schema,
            max_rows_per_file=args.max_rows
        )
    else:
        # Single file processing
        input_file = Path(args.input)
        output_file = Path(args.output) if args.output else input_file.with_suffix('.jsonl')

        stats = converter.convert_to_jsonl(
            str(input_file),
            str(output_file),
            schema=args.schema,
            custom_mapping=custom_mapping,
            max_rows=args.max_rows
        )

        results = {input_file.name: stats}

    print(f"\n✅ CONVERSION COMPLETE!")
    print(f"Results saved. Ready for your ML training pipeline!")

if __name__ == "__main__":
    main()