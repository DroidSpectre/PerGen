import os
import glob
import json
import pyarrow.parquet as pq
import pyarrow.types as patypes
from pathlib import Path

def convert_value(value, arrow_type):
    """Convert Arrow types to JSON-serializable formats."""
    if patypes.is_timestamp(arrow_type):
        return value.isoformat() if value is not None else None
    elif patypes.is_binary(arrow_type):
        return value.hex() if value is not None else None
    elif patypes.is_decimal(arrow_type):
        return float(value) if value is not None else None
    else:
        return value

def batch_to_jsonl_records(record_batch):
    """Convert a PyArrow RecordBatch to a list of JSON-serializable dicts."""
    converted = []
    for i in range(record_batch.num_rows):
        row = {}
        for col_idx in range(record_batch.num_columns):
            col_name = record_batch.schema.names[col_idx]
            value = record_batch[col_idx][i].as_py()
            arrow_type = record_batch.schema.types[col_idx]
            row[col_name] = convert_value(value, arrow_type)
        converted.append(row)
    return converted

def process_parquet_to_jsonl(input_path, output_dir, chunk_size=1000):
    parquet_file = pq.ParquetFile(input_path)
    base_name = Path(input_path).stem
    output_base = os.path.join(output_dir, f"{base_name}_jsonl")
    os.makedirs(output_base, exist_ok=True)
    chunk_num = 0
    for batch in parquet_file.iter_batches(batch_size=chunk_size):
        records = batch_to_jsonl_records(batch)
        output_file = os.path.join(output_base, f"chunk_{chunk_num}.jsonl")
        with open(output_file, "w", encoding="utf-8") as f:
            for record in records:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
        print(f"Created {output_file} with {len(records)} records")
        chunk_num += 1

if __name__ == "__main__":
    data_dir = "/storage/emulated/0/download/datasets/training_session/tiny-orca-textbooks"
    parquet_files = glob.glob(os.path.join(data_dir, "*.parquet"))
    for parquet_file in parquet_files:
        process_parquet_to_jsonl(
            input_path=parquet_file,
            output_dir=data_dir,
            chunk_size=1000  # Adjust as needed
        )

