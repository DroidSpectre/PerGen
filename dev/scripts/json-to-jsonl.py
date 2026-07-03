#!/usr/bin/env python3
import os
import glob
import json
import sys

def find_base_dir(relative_path):
    """
    Try the Termux storage symlink first, then the raw Android path.
    """
    # After `termux-setup-storage`, this symlink exists:
    termux_path = os.path.expanduser(f'~/storage/downloads/{relative_path}')
    if os.path.isdir(termux_path):
        return termux_path

    # Direct Android Download folder
    android_path = f'/storage/emulated/0/Download/{relative_path}'
    if os.path.isdir(android_path):
        return android_path

    return None

def convert_all_json(base_dir):
    """
    For every .json file in base_dir, write a .jsonl with one record per line.
    """
    pattern = os.path.join(base_dir, '*.json')
    json_files = glob.glob(pattern)
    if not json_files:
        print(f"No .json files found in {base_dir}", file=sys.stderr)
        return

    for src in json_files:
        dst = os.path.splitext(src)[0] + '.jsonl'
        try:
            print(f"Reading:  {src}")
            with open(src, 'r', encoding='utf-8') as f_in:
                data = json.load(f_in)
                if not isinstance(data, list):
                    raise ValueError("Root element must be a JSON array")
            print(f"Writing:  {dst}")
            with open(dst, 'w', encoding='utf-8') as f_out:
                for record in data:
                    json.dump(record, f_out)
                    f_out.write('\n')
        except Exception as e:
            print(f"Error converting {src}: {e}", file=sys.stderr)

if __name__ == '__main__':
    # Adjust this to your subfolder under Downloads
    rel_path = 'datasets/Cosmopedia-100k-307mb'

    base = find_base_dir(rel_path)
    if not base:
        print(
            f"❌ Could not find '{rel_path}' under ~/storage/downloads or "
            f"/storage/emulated/0/Download",
            file=sys.stderr
        )
        sys.exit(1)

    convert_all_json(base)
    print("✅ All done!")
