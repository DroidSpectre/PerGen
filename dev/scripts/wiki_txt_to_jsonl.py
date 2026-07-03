import json
import os
import re
from pathlib import Path

def clean_text(text):
    """Clean and normalize text content"""
    # Remove excessive whitespace while preserving paragraph structure
    text = re.sub(r'\n\s*\n', '\n\n', text)
    # Remove leading/trailing whitespace
    text = text.strip()
    # Ensure no empty lines at start or end
    text = re.sub(r'^\n+|\n+$', '', text)
    return text

def extract_title(text):
    """Extract potential title from the beginning of text"""
    lines = text.split('\n')
    if lines:
        first_line = lines[0].strip()
        # If first line is short and doesn't end with punctuation, likely a title
        if len(first_line) < 100 and not first_line.endswith(('.', '!', '?')):
            return first_line
    return None

def convert_wikipedia_to_jsonl(input_file, output_dir="output", samples_per_file=1000):
    """
    Convert Plain Text Wikipedia to multiple JSONL files
    
    Args:
        input_file: Path to the plain text Wikipedia file
        output_dir: Directory to save JSONL files
        samples_per_file: Number of samples per JSONL file
    """
    
    # Create output directory
    Path(output_dir).mkdir(exist_ok=True)
    
    file_count = 0
    sample_count = 0
    total_samples = 0
    current_file = None
    
    print(f"Processing {input_file}...")
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        content = infile.read()
    
    # Split on blank lines (multiple consecutive newlines)
    articles = re.split(r'\n\s*\n\s*\n', content)
    
    for article in articles:
        article = clean_text(article)
        
        # Skip empty or very short articles
        if len(article) < 50:
            continue
        
        # Open new file if needed
        if sample_count == 0:
            if current_file:
                current_file.close()
            
            filename = f"wikipedia_train_{file_count:04d}.jsonl"
            filepath = os.path.join(output_dir, filename)
            current_file = open(filepath, 'w', encoding='utf-8')
            print(f"Creating {filename}")
            file_count += 1
        
        # Extract title if possible
        title = extract_title(article)
        
        # Create JSON object with appropriate tags for LLM training
        json_obj = {
            "text": article,
            "source": "wikipedia",
            "dataset": "plain_text_wikipedia_english",
            "sample_id": total_samples
        }
        
        # Add title if extracted
        if title:
            json_obj["title"] = title
        
        # Add word count for potential filtering
        json_obj["word_count"] = len(article.split())
        
        # Write to current file
        json.dump(json_obj, current_file, ensure_ascii=False)
        current_file.write('\n')
        
        sample_count += 1
        total_samples += 1
        
        # Reset sample count if reached limit
        if sample_count >= samples_per_file:
            sample_count = 0
    
    # Close the last file
    if current_file:
        current_file.close()
    
    print(f"\nConversion complete!")
    print(f"Total samples processed: {total_samples}")
    print(f"Files created: {file_count}")
    print(f"Output directory: {output_dir}")

def validate_jsonl_files(output_dir):
    """Validate the created JSONL files"""
    jsonl_files = list(Path(output_dir).glob("*.jsonl"))
    
    print(f"\nValidating {len(jsonl_files)} JSONL files...")
    
    total_samples = 0
    for filepath in sorted(jsonl_files):
        sample_count = 0
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    json.loads(line)  # Validate JSON
                    sample_count += 1
            print(f"{filepath.name}: {sample_count} samples")
            total_samples += sample_count
        except json.JSONDecodeError as e:
            print(f"Error in {filepath.name}: {e}")
    
    print(f"Total validated samples: {total_samples}")

if __name__ == "__main__":
    # Configuration
    INPUT_FILE = "/storage/emulated/0/download/PTW-Eng/AllCombined.txt"  # Update with your file path
    OUTPUT_DIR = "wikipedia_jsonl_output"
    SAMPLES_PER_FILE = 1000
    
    # Convert the dataset
    convert_wikipedia_to_jsonl(
        input_file=INPUT_FILE,
        output_dir=OUTPUT_DIR,
        samples_per_file=SAMPLES_PER_FILE
    )
    
    # Validate the output
    validate_jsonl_files(OUTPUT_DIR)
