# CSV to JSONL Converter - Comprehensive Usage Guide

## Overview
The CSV to JSONL converter transforms your educational datasets from CSV format to JSONL (JSON Lines) format, which is required for TermuxTrain's enhanced data processor. This tool is specifically designed for datasets with the `instruction,input,output` format.

## Quick Start

### 1. File Placement (Simple Method)
Place your CSV files in the same directory as the `csv_converter_v2.py` script:

```
your_project_folder/
├── csv_converter_v2.py
├── MATH.csv
├── LITERATURE.csv
├── GENERAL_KNOWLEDGE.csv
├── SCIENCE.csv
├── REASONING.csv
├── Chat_Communication_1k.csv
├── Critical_Thinking_Problem_Solving_1k.csv
├── Emotional_Intelligence_1k.csv
├── Common_Sense_World_Facts_1k.csv
└── Creative_Innovation_1k.jsonl
```

### 2. Run the Converter
Open terminal/command prompt and navigate to your folder:
```bash
cd /path/to/your_project_folder
python csv_converter_v2.py
```

### 3. Check Results
The script will create JSONL files in the same directory:
- `MATH.jsonl`
- `LITERATURE.jsonl`
- `GENERAL_KNOWLEDGE.jsonl`
- `SCIENCE.jsonl`
- `REASONING.jsonl`

## Detailed Usage

### Method 1: Direct Script Execution (Recommended)
```bash
python csv_converter_v2.py
```

**What it does:**
- Automatically looks for the 5 standard datasets in current directory
- Converts each CSV to JSONL format
- Provides detailed statistics and validation
- Shows sample entries for verification

### Method 2: Custom Directory Usage
If your CSV files are in a different location:

```python
from csv_converter_v2 import convert_all_datasets

# Convert files from custom directories
results = convert_all_datasets(
    csv_directory="/path/to/your/csv/files",
    output_directory="/path/to/save/jsonl/files"
)
```

### Method 3: Single File Conversion
To convert individual files:

```python
from csv_converter_v2 import csv_to_jsonl_instruction_format

# Convert a single file
count = csv_to_jsonl_instruction_format(
    csv_path="your_dataset.csv",
    jsonl_path="your_dataset.jsonl"
)
```

## File Requirements

### CSV Format Requirements
Your CSV files MUST have these exact column headers:
```csv
instruction,input,output
```

### Expected Datasets (500-sample sets)
The converter looks for these specific files:
- `MATH.csv`
- `LITERATURE.csv` 
- `GENERAL_KNOWLEDGE.csv`
- `SCIENCE.csv`
- `REASONING.csv`

### 1K Sample Datasets
For your larger datasets, rename them to match or convert individually:

**Option 1: Rename your 1k files**
```bash
# Rename your 1k files to match expected names
mv "Chat_Communication_1k.csv" "Chat_Communication.csv"
mv "Critical_Thinking_Problem_Solving_1k.csv" "Critical_Thinking.csv"
mv "Emotional_Intelligence_1k.csv" "Emotional_Intelligence.csv"
mv "Common_Sense_World_Facts_1k.csv" "Common_Sense.csv"
```

**Option 2: Convert individually**
```python
from csv_converter_v2 import csv_to_jsonl_instruction_format

datasets_1k = [
    "Chat_Communication_1k.csv",
    "Critical_Thinking_Problem_Solving_1k.csv", 
    "Emotional_Intelligence_1k.csv",
    "Common_Sense_World_Facts_1k.csv"
]

for dataset in datasets_1k:
    output_file = dataset.replace('.csv', '.jsonl')
    csv_to_jsonl_instruction_format(dataset, output_file)
```

## Understanding the Output

### Console Output
```
🔄 CONVERTING ALL EDUCATIONAL DATASETS
==================================================
Converting MATH.csv to MATH.jsonl...
Successfully converted 500 samples to MATH.jsonl
✅ MATH.csv: 500 samples converted
Converting LITERATURE.csv to LITERATURE.jsonl...
Successfully converted 500 samples to LITERATURE.jsonl
✅ LITERATURE.csv: 500 samples converted

📊 CONVERSION SUMMARY
Total samples converted: 2500
Total datasets: 5

📈 DATASET STATISTICS
==================================================
Successfully converted: 5/5 datasets
Total training samples: 2,500
Average samples per dataset: 500

Dataset Breakdown:
  📁 MATH.csv             : 500 samples (20.0%)
  📁 LITERATURE.csv       : 500 samples (20.0%)
  ...
```

### JSONL Output Format
Each line in the JSONL file contains one JSON object:
```json
{"instruction": "What is photosynthesis?", "input": "", "output": "Photosynthesis is the process by which plants..."}
{"instruction": "Solve: 2x + 5 = 15", "input": "", "output": "2x + 5 = 15\n2x = 15 - 5\n2x = 10\nx = 5"}
```

## Error Handling

### Common Issues and Solutions

**Error: File not found**
```
❌ MATH.csv: File not found
```
**Solution:** Ensure the CSV file exists in the specified directory with the exact filename.

**Warning: Wrong column headers**
```
Warning: Expected columns [instruction, input, output] not found
Found columns: ['question', 'answer']
```
**Solution:** Your CSV must have columns named exactly: `instruction`, `input`, `output`

**Empty rows skipped**
```
Skipping row 45: empty instruction or output
```
**Solution:** This is normal - the converter skips rows with missing required data.

## Directory Structure Examples

### Basic Setup
```
project/
├── csv_converter_v2.py
├── MATH.csv
├── LITERATURE.csv
└── ... (other CSV files)
```

### Organized Setup
```
llm_training/
├── scripts/
│   └── csv_converter_v2.py
├── data/
│   ├── csv/
│   │   ├── MATH.csv
│   │   └── ... (other CSV files)
│   └── jsonl/
│       └── (output files)
└── models/
```

For organized setup, run:
```python
from scripts.csv_converter_v2 import convert_all_datasets
results = convert_all_datasets("data/csv", "data/jsonl")
```

## Validation and Quality Check

### Automatic Validation
The converter automatically:
- ✅ Validates column headers
- ✅ Checks for empty required fields
- ✅ Counts successful conversions
- ✅ Shows sample entries
- ✅ Generates statistics

### Manual Validation
Check your JSONL files:
```python
import json

# Check first few lines of output
with open('MATH.jsonl', 'r') as f:
    for i, line in enumerate(f):
        if i >= 3:  # Check first 3 entries
            break
        data = json.loads(line)
        print(f"Entry {i+1}:")
        print(f"  Instruction: {data['instruction']}")
        print(f"  Output: {data['output'][:100]}...")
```

## Integration with TermuxTrain

### After Conversion
1. **Move JSONL files** to your training data directory
2. **Update dataset paths** in your training scripts
3. **Use in tokenizer training:**
   ```python
   dataset_paths = [
       "MATH.jsonl",
       "LITERATURE.jsonl",
       "GENERAL_KNOWLEDGE.jsonl",
       "SCIENCE.jsonl", 
       "REASONING.jsonl"
   ]
   trainer.train_tokenizer(dataset_paths)
   ```

### Training Pipeline Integration
```python
# Phase 1: Base vocabulary (use tokenizer pre-training dataset)
# Phase 2: Educational content
for dataset_path in jsonl_files:
    history = trainer.train(dataset_path, epochs=1, is_jsonl=True)
```

## Troubleshooting

### Performance Issues
- **Large files:** Process files one at a time if memory is limited
- **Slow conversion:** Normal for large datasets, be patient

### Data Issues
- **Missing data:** Check source CSV for empty cells
- **Encoding errors:** Ensure CSV files use UTF-8 encoding
- **Format problems:** Verify CSV has proper instruction,input,output format

### File Issues
- **Permission errors:** Ensure write permissions in output directory
- **Path problems:** Use absolute paths if relative paths don't work

## Advanced Usage

### Batch Processing Multiple Directories
```python
import os
from csv_converter_v2 import convert_all_datasets

directories = ["dataset_batch_1", "dataset_batch_2", "dataset_batch_3"]

for directory in directories:
    if os.path.exists(directory):
        print(f"Processing {directory}...")
        convert_all_datasets(directory, f"{directory}_output")
```

### Custom Dataset Lists
Modify the script to handle different files:
```python
# Edit the datasets list in convert_all_datasets()
datasets = [
    "your_custom_dataset_1.csv",
    "your_custom_dataset_2.csv",
    "your_custom_dataset_3.csv"
]
```

## Next Steps After Conversion

1. **Verify JSONL files** are properly formatted
2. **Test with small samples** first 
3. **Integrate into TermuxTrain pipeline**
4. **Begin tokenizer training** with converted datasets
5. **Start your multi-phase training strategy**

## Support and Troubleshooting

### Common Success Indicators
- ✅ Console shows "Successfully converted X samples"
- ✅ JSONL files created with reasonable file sizes
- ✅ Sample validation shows proper format
- ✅ Statistics match expected dataset sizes

### When to Contact Support
- ❌ Consistent conversion failures
- ❌ Corrupted output files
- ❌ Unexpected data loss during conversion
- ❌ Performance issues with large files

The converter is designed to be robust and handle most educational datasets that follow the standard instruction-following format. Most issues can be resolved by checking file paths, formats, and permissions.