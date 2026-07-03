# UNIVERSAL CSV TO JSONL CONVERTER v4 - USAGE EXAMPLES

## Basic Usage

### 1. Convert a single CSV file (auto-detect format)
python csv_converter_v4_universal.py data.csv

### 2. Convert with specific output file
python csv_converter_v4_universal.py data.csv -o training_data.jsonl

### 3. Convert large file with row limit
python csv_converter_v4_universal.py huge_dataset.csv --max-rows 100000

### 4. Batch convert all CSV files in directory
python csv_converter_v4_universal.py /path/to/csv_files --batch

### 5. Convert with specific schema
python csv_converter_v4_universal.py data.csv --schema alpaca

## Advanced Usage

### 6. Custom column mapping
python csv_converter_v4_universal.py data.csv --schema custom --mapping '{"question":"Q", "answer":"A"}'

### 7. Batch convert with pattern matching
python csv_converter_v4_universal.py ./datasets --batch --pattern "*_train.csv"

### 8. Large file processing with chunking
python csv_converter_v4_universal.py large_file.csv --chunk-size 5000 --max-rows 1000000

## Schema Types

- **auto**: Automatically detect the best format
- **alpaca**: instruction, input, output format (for LLM training)
- **qa**: question, answer format
- **text**: single text column format
- **custom**: user-defined mapping

## Memory Efficiency Features

The v4 converter can handle files of ANY SIZE because it:
- Streams data row-by-row instead of loading everything into memory
- Uses chunked processing for progress tracking
- Automatically detects CSV delimiters
- Provides real-time progress updates for large files

## Example Column Mappings

### For Alpaca Format:
Your CSV columns → JSONL output
instruction → instruction
input → input (optional)
output → output

### For Q&A Format:
Your CSV columns → JSONL output  
question → question
answer → answer

### Custom Mapping Example:
If your CSV has columns: "prompt", "context", "response"
Use: --mapping '{"instruction":"prompt", "input":"context", "output":"response"}'