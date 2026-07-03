#!/usr/bin/env python3
"""
File Extension Converter
Renames .txt files to their proper extensions based on filename patterns
"""

import os
import sys
from pathlib import Path

def get_proper_extension(filename):
    """Determine the proper extension based on the filename"""

    # Remove .txt extension if present
    base_name = filename.replace('.txt', '')

    # Java files
    if base_name.endswith('.java'):
        return '.java'

    # XML files
    if base_name.endswith('.xml'):
        return '.xml'

    # Gradle files
    if base_name.endswith('.gradle'):
        return '.gradle'

    # Shell script files
    if base_name.endswith('.sh'):
        return '.sh'

    # JSON files
    if base_name.endswith('.json'):
        return '.json'

    # Markdown files
    if base_name.endswith('.md'):
        return '.md'

    # ProGuard rules
    if base_name.endswith('.pro'):
        return '.pro'

    # Properties files
    if base_name.endswith('.properties'):
        return '.properties'

    # No extension files (like gradlew)
    if '.' not in base_name:
        return ''  # Remove .txt, leave as is

    return None

def rename_files(directory='.', dry_run=True):
    """Rename all .txt files to their proper extensions"""

    # Get current directory path
    dir_path = Path(directory)

    # Find all .txt files
    txt_files = list(dir_path.glob('*.txt'))

    if not txt_files:
        print("No .txt files found in the directory.")
        return

    print(f"Found {len(txt_files)} .txt file(s)\n")

    renamed_count = 0
    skipped_count = 0

    for txt_file in txt_files:
        original_name = txt_file.name

        # Determine proper extension
        proper_ext = get_proper_extension(original_name)

        if proper_ext is None:
            print(f"⚠️  SKIP: {original_name} - Cannot determine proper extension")
            skipped_count += 1
            continue

        # Create new filename
        base_name = original_name.replace('.txt', '')

        if proper_ext == '':
            # No extension (like gradlew)
            new_name = base_name
        else:
            # Remove the extension from base_name and add proper extension
            new_name = base_name

        new_path = dir_path / new_name

        # Check if target file already exists
        if new_path.exists() and new_path != txt_file:
            print(f"⚠️  SKIP: {original_name} -> {new_name} (target already exists)")
            skipped_count += 1
            continue

        # Rename the file
        if dry_run:
            print(f"✓ WOULD RENAME: {original_name} -> {new_name}")
        else:
            try:
                txt_file.rename(new_path)
                print(f"✓ RENAMED: {original_name} -> {new_name}")
                renamed_count += 1
            except Exception as e:
                print(f"✗ ERROR: {original_name} - {str(e)}")
                skipped_count += 1

    print(f"\n{'=' * 50}")
    if dry_run:
        print("DRY RUN MODE - No files were actually renamed")
        print(f"Would rename: {len(txt_files) - skipped_count} files")
    else:
        print(f"Successfully renamed: {renamed_count} files")
    print(f"Skipped: {skipped_count} files")
    print(f"{'=' * 50}")

def main():
    """Main function"""
    print("=" * 50)
    print("File Extension Converter")
    print("=" * 50)
    print()

    # Get directory from command line or use current directory
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'

    # Check if directory exists
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist")
        sys.exit(1)

    # First, do a dry run
    print("DRY RUN - Preview of changes:")
    print("-" * 50)
    rename_files(directory, dry_run=True)

    print()
    response = input("Do you want to proceed with renaming? (yes/no): ").strip().lower()

    if response in ['yes', 'y']:
        print()
        print("ACTUAL RUN - Renaming files:")
        print("-" * 50)
        rename_files(directory, dry_run=False)
    else:
        print("\nOperation cancelled.")

if __name__ == "__main__":
    main()