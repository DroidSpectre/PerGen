
import os
import glob
import pandas as pd
import sys

def find_base_dir(relative_path):
    """
    Try the Termux symlink first, then the raw Android path.
    """
    # Termux storage symlink
    termux_path = os.path.expanduser(f'~/storage/downloads/{relative_path}')
    if os.path.isdir(termux_path):
        return termux_path

    # Raw Android path
    android_path = f'/storage/emulated/0/Download/{relative_path}'
    if os.path.isdir(android_path):
        return android_path

    # Nothing found
    return None

def convert_all_parquets(base_dir):
    parquets = glob.glob(os.path.join(base_dir, '*.parquet'))
    if not parquets:
        print(f"No .parquet files found in {base_dir}", file=sys.stderr)
        return

    for pq in parquets:
        # derive output path
        out = os.path.splitext(pq)[0] + '.jsonl'
        try:
            print(f"Reading:  {pq}")
            df = pd.read_parquet(pq, engine='pyarrow')
            print(f"Writing:  {out}")
            df.to_json(out, orient='records', lines=True)
        except Exception as e:
            print(f"Error converting {pq}: {e}", file=sys.stderr)

if __name__ == '__main__':
    # relative path under Downloads; adjust if your datasets dir is different
    rel_path = 'datasets/Cosmopedia-100k-307mb'

    base = find_base_dir(rel_path)
    if not base:
        print(f"❌ Could not find '{rel_path}' under ~/storage/downloads or /storage/emulated/0/Download", 
              file=sys.stderr)
        sys.exit(1)

    convert_all_parquets(base)
    print("✅ All done!")