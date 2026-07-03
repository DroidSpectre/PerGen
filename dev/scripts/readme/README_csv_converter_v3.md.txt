# CSV to JSONL Converter v3 - Complete User Guide

## Overview

The Enhanced CSV to JSONL Converter v3 is a comprehensive tool designed specifically for TermuxTrain's dataset preparation pipeline. It converts educational datasets from CSV format to JSONL (JSON Lines) format with full support for both 500-sample and 1k-sample datasets, interactive operation, and command-line flexibility.

## 🚀 Quick Start

### 1. Simple Interactive Mode (Recommended)
```bash
python csv_converter_v3.py
```
Follow the interactive menu to convert your datasets with ease.

### 2. Command Line Mode
```bash
# Convert standard 500-sample datasets
python csv_converter_v3.py --mode standard

# Convert 1k sample datasets  
python csv_converter_v3.py --mode 1k

# Convert all CSV files in a directory
python csv_converter_v3.py --mode all --input-dir /path/to/csvs --output-dir /path/to/output
```

## ✨ Features

### 🎯 **Multi-Mode Operation**
- **Interactive Mode**: User-friendly menu system
- **Standard Mode**: Convert 500-sample educational datasets
- **1K Mode**: Convert large 1k-sample datasets
- **All Mode**: Convert any CSV files in directory
- **Custom Mode**: Convert specific files

### 📁 **Flexible Directory Support**
- **Auto-Discovery**: Finds all CSV files automatically
- **Custom Directories**: Specify input and output locations
- **Path Validation**: Ensures directories exist and are accessible
- **Safe Output**: Creates output directories automatically

### ✅ **Built-in Validation**
- **Format Verification**: Validates instruction,input,output format
- **Sample Preview**: Shows converted entries for verification
- **Statistics**: Comprehensive conversion reports
- **Error Handling**: Graceful handling of problematic files

### 🔧 **Command Line Power**
- **Full Argument Support**: All features available via CLI
- **Batch Processing**: Handle multiple files efficiently
- **Validation Options**: Optional post-conversion validation
- **Flexible Configuration**: Customize sample counts and behavior

## 📋 Prerequisites

### Required CSV Format
Your CSV files **must** have these exact column headers:
```csv
instruction,input,output
```

### Example CSV Structure
```csv
instruction,input,output
"What is photosynthesis?","","Photosynthesis is the process by which plants convert sunlight into chemical energy using chlorophyll..."
"Solve: 2x + 5 = 15","","To solve 2x + 5 = 15: 1) Subtract 5 from both sides: 2x = 10, 2) Divide by 2: x = 5"
```

## 🎯 Interactive Mode Guide

### Step-by-Step Usage

1. **Launch Interactive Mode**
   ```bash
   python csv_converter_v3.py
   ```

2. **Choose Conversion Type**
   ```
   🎯 INTERACTIVE DATASET CONVERTER
   ==================================================
   Available conversion options:
   1. Convert standard datasets (500 samples each)
   2. Convert 1k sample datasets
   3. Convert all CSV files in directory
   4. Convert specific files
   5. Exit
   
   Select option (1-5):
   ```

3. **Specify Directories**
   ```
   CSV directory (press Enter for current): /path/to/your/csvs
   Output directory (press Enter for same as CSV): /path/to/output
   ```

4. **Review Results**
   ```
   📊 CONVERSION SUMMARY
   ========================================
   Total samples converted: 5,000
   Successful conversions: 9/9
   ```

5. **Optional Validation**
   ```
   Validate converted files? (y/n): y
   ```

### Supported Dataset Types

#### Option 1: Standard Datasets (500 samples each)
- `MATH.csv`
- `LITERATURE.csv`
- `GENERAL_KNOWLEDGE.csv`
- `SCIENCE.csv`
- `REASONING.csv`

#### Option 2: 1K Sample Datasets
- `Chat_Communication_1k.csv`
- `Critical_Thinking_Problem_Solving_1k.csv`
- `Emotional_Intelligence_1k.csv`
- `Common_Sense_World_Facts_1k.csv`

#### Option 3: All CSV Files
Automatically discovers and converts all `.csv` files in the specified directory.

#### Option 4: Specific Files
Allows you to specify exactly which CSV files to convert.

## 🔧 Command Line Reference

### Basic Syntax
```bash
python csv_converter_v3.py [OPTIONS]
```

### Available Arguments

| Argument | Short | Description | Default |
|----------|-------|-------------|---------|
| `--mode` | | Conversion mode: `standard`, `1k`, `all`, `interactive` | `interactive` |
| `--input-dir` | `-i` | Input directory containing CSV files | `.` (current) |
| `--output-dir` | `-o` | Output directory for JSONL files | Same as input |
| `--files` | `-f` | Specific CSV files to convert | None |
| `--validate` | | Validate converted JSONL files | False |
| `--samples` | | Number of sample entries to show during validation | 3 |

### Command Line Examples

#### Convert Standard Datasets
```bash
# Convert 500-sample datasets in current directory
python csv_converter_v3.py --mode standard

# Convert from custom directory
python csv_converter_v3.py --mode standard -i /home/data/csvs -o /home/data/jsonl

# With validation
python csv_converter_v3.py --mode standard --validate --samples 5
```

#### Convert 1K Datasets
```bash
# Convert 1k-sample datasets
python csv_converter_v3.py --mode 1k

# Custom directories with validation
python csv_converter_v3.py --mode 1k -i datasets/large -o training_data --validate
```

#### Convert All Files
```bash
# Convert all CSV files in directory
python csv_converter_v3.py --mode all

# Specific directory with validation
python csv_converter_v3.py --mode all -i /path/to/csvs -o /path/to/jsonl --validate
```

#### Convert Specific Files
```bash
# Convert specific files
python csv_converter_v3.py --mode all --files dataset1.csv dataset2.csv dataset3.csv

# With custom directories
python csv_converter_v3.py --mode all -i input_folder -o output_folder --files file1.csv file2.csv
```

## 📊 Understanding Output

### Console Output Example
```
🚀 ENHANCED CSV TO JSONL CONVERTER v3
============================================================
Input directory: ./datasets
Output directory: ./training_data
Mode: standard

🔄 CONVERTING CSV DATASETS TO JSONL
============================================================
Input directory: ./datasets
Output directory: ./training_data
Found 5 CSV files
----------------------------------------

Converting ./datasets/MATH.csv to ./training_data/MATH.jsonl...
Successfully converted 500 samples to ./training_data/MATH.jsonl
✅ MATH.csv: 500 samples converted

Converting ./datasets/LITERATURE.csv to ./training_data/LITERATURE.jsonl...
Successfully converted 500 samples to ./training_data/LITERATURE.jsonl
✅ LITERATURE.csv: 500 samples converted

📊 CONVERSION SUMMARY
========================================
Total samples converted: 2,500
Successful conversions: 5/5

📈 STANDARD DATASETS STATISTICS
==================================================
Successfully converted: 5/5 Standard Datasets
Total training samples: 2,500
Average samples per dataset: 500

Dataset Breakdown:
  📁 MATH.csv                          :  500 samples (20.0%)
  📁 LITERATURE.csv                    :  500 samples (20.0%)
  📁 GENERAL_KNOWLEDGE.csv             :  500 samples (20.0%)
  📁 SCIENCE.csv                       :  500 samples (20.0%)
  📁 REASONING.csv                     :  500 samples (20.0%)

🎯 TRAINING RECOMMENDATIONS (Standard Datasets):
  • Tokenizer training: Use ~50 samples from each dataset
  • Fine-tuning: Use full datasets in specialized phases
  • Mixed training: Combine all for comprehensive training
  • Expected training time: 2-4 hours per dataset (mobile CPU)
```

### JSONL Output Format
Each line in the output file contains one JSON object:
```json
{"instruction": "What is photosynthesis?", "input": "", "output": "Photosynthesis is the process by which plants convert sunlight into chemical energy..."}
{"instruction": "Solve: 2x + 5 = 15", "input": "", "output": "To solve 2x + 5 = 15: 1) Subtract 5 from both sides: 2x = 10, 2) Divide by 2: x = 5"}
```

### Validation Output Example
```
🔍 VALIDATING MATH.jsonl
----------------------------------------
Total lines: 500

Sample entries (first 3):

Entry 1:
  Instruction: What is the quadratic formula?...
  Input: (empty)
  Output: The quadratic formula is x = (-b ± √(b² - 4ac)) / 2a, where a, b, and c are...

Entry 2:
  Instruction: Solve for x: 3x + 7 = 22...
  Input: (empty)
  Output: To solve 3x + 7 = 22: 1) Subtract 7 from both sides: 3x = 15, 2) Divide by 3: x = 5...
```

## 🗂️ Directory Structure Examples

### Basic Setup
```
project/
├── csv_converter_v3.py
├── MATH.csv
├── LITERATURE.csv
├── GENERAL_KNOWLEDGE.csv
├── SCIENCE.csv
└── REASONING.csv
```

### Organized Structure
```
llm_training/
├── scripts/
│   └── csv_converter_v3.py
├── datasets/
│   ├── standard/
│   │   ├── MATH.csv
│   │   ├── LITERATURE.csv
│   │   └── ... (other 500-sample files)
│   └── large/
│       ├── Chat_Communication_1k.csv
│       ├── Critical_Thinking_Problem_Solving_1k.csv
│       └── ... (other 1k files)
├── training_data/
│   ├── standard/
│   └── large/
└── models/
```

### Usage with Organized Structure
```bash
# Convert standard datasets
python scripts/csv_converter_v3.py --mode standard -i datasets/standard -o training_data/standard

# Convert 1k datasets
python scripts/csv_converter_v3.py --mode 1k -i datasets/large -o training_data/large
```

## ⚠️ Error Handling & Troubleshooting

### Common Issues & Solutions

#### Issue: "File not found"
```
❌ MATH.csv: File not found
```
**Solution**: 
- Check that the CSV file exists in the specified directory
- Verify the exact filename (case-sensitive)
- Use absolute paths if relative paths cause issues

#### Issue: "Wrong column headers"
```
Warning: Expected columns [instruction, input, output] not found
Found columns: ['question', 'answer', 'topic']
```
**Solution**: 
- Ensure your CSV has exactly these column names: `instruction`, `input`, `output`
- Check for extra spaces or special characters in headers
- Verify the CSV isn't corrupted or improperly formatted

#### Issue: "Empty rows skipped"
```
Skipping row 45: empty instruction or output
```
**Solution**: 
- This is normal behavior - the converter skips incomplete data
- Review your source CSV for empty cells
- Ensure critical fields (instruction, output) are populated

#### Issue: "Permission denied"
```
Error processing dataset.csv: [Errno 13] Permission denied
```
**Solution**: 
- Ensure read permissions on input files
- Ensure write permissions in output directory
- Check if files are open in other applications

#### Issue: "Encoding errors"
```
Error processing dataset.csv: 'charmap' codec can't decode
```
**Solution**: 
- Save your CSV files with UTF-8 encoding
- Check for special characters or international text
- Use a text editor that supports UTF-8

### Performance Considerations

#### Large Dataset Handling
- **Memory Usage**: Each dataset processes one row at a time (memory efficient)
- **Processing Time**: Expect ~1-2 minutes per 1000 samples
- **Disk Space**: JSONL files are typically 20-30% larger than CSV

#### Optimization Tips
- Close other applications during conversion for large datasets
- Use SSD storage for faster file I/O
- Process datasets individually if memory is limited

## 🔗 TermuxTrain Integration

### After Conversion

1. **Verify Output Files**
   ```bash
   ls -la *.jsonl
   # Check file sizes are reasonable
   ```

2. **Test with Small Sample**
   ```python
   import json
   
   # Quick validation
   with open('MATH.jsonl', 'r') as f:
       for i, line in enumerate(f):
           if i >= 3: break
           data = json.loads(line)
           print(f"Sample {i+1}: {data['instruction'][:50]}...")
   ```

3. **Integration with Training Pipeline**
   ```python
   from llm_trainer_v4_1 import EnhancedLLMTrainer
   
   # Use converted datasets
   dataset_paths = [
       "MATH.jsonl",
       "LITERATURE.jsonl",
       "GENERAL_KNOWLEDGE.jsonl",
       "SCIENCE.jsonl",
       "REASONING.jsonl"
   ]
   
   # Tokenizer training
   trainer.train_tokenizer(dataset_paths, sample_size=250)
   
   # Model training
   for dataset_path in dataset_paths:
       trainer.train(dataset_path, epochs=1, is_jsonl=True)
   ```

### Training Strategy with Converted Datasets

#### Phase 1: Tokenizer Training
- Use samples from all converted datasets
- Standard datasets: ~50 samples each
- 1K datasets: ~100-200 samples each

#### Phase 2: Specialized Training  
- Train on each dataset separately
- 1-2 epochs for focused skill development
- Monitor loss and validation metrics

#### Phase 3: Integration Training
- Combine datasets for comprehensive capabilities
- Final tuning for well-rounded AI assistant
- Balance between different skill domains

## 📈 Advanced Usage

### Batch Processing Multiple Directories
```python
import os
import subprocess

directories = ["batch1", "batch2", "batch3"]

for directory in directories:
    cmd = f"python csv_converter_v3.py --mode all -i {directory} -o {directory}_output --validate"
    subprocess.run(cmd, shell=True)
```

### Custom Validation Script
```python
import json
import os

def validate_conversion_quality(jsonl_path):
    """Custom validation for specific requirements"""
    with open(jsonl_path, 'r') as f:
        lines = f.readlines()
    
    # Check sample size
    print(f"Total samples: {len(lines)}")
    
    # Check for consistency
    for i, line in enumerate(lines[:10]):
        data = json.loads(line)
        if len(data['instruction']) < 10:
            print(f"Warning: Short instruction in line {i+1}")
        if len(data['output']) < 20:
            print(f"Warning: Short output in line {i+1}")

# Use custom validation
validate_conversion_quality('MATH.jsonl')
```

### Integration with Training Scripts
```python
# Add to your training configuration
training_config = {
    'datasets': {
        'standard': ['MATH.jsonl', 'LITERATURE.jsonl', 'SCIENCE.jsonl'],
        'large': ['Chat_Communication_1k.jsonl', 'Emotional_Intelligence_1k.jsonl'],
        'creative': ['Creative_Innovation_1k.jsonl']
    },
    'batch_size': 4,
    'learning_rate': 0.001
}
```

## 🎯 Best Practices

### File Organization
- ✅ Keep CSV and JSONL files in separate directories
- ✅ Use descriptive directory names (e.g., `csv_datasets`, `training_data`)
- ✅ Maintain consistent naming conventions
- ✅ Backup original CSV files before conversion

### Quality Assurance
- ✅ Always use validation mode for important conversions
- ✅ Check sample entries to ensure proper conversion
- ✅ Verify file sizes match expected dataset sizes
- ✅ Test integration with training pipeline before full conversion

### Workflow Efficiency
- ✅ Use interactive mode for initial setup and testing
- ✅ Use command-line mode for production/automated workflows  
- ✅ Process datasets in logical groups (standard, 1k, custom)
- ✅ Keep conversion logs for troubleshooting

## 🆘 Support & Troubleshooting

### Getting Help
1. **Check Error Messages**: Read console output carefully
2. **Validate Input**: Ensure CSV format is correct
3. **Test Small**: Try converting single files first
4. **Check Permissions**: Verify file and directory access

### Common Success Indicators
- ✅ Console shows "Successfully converted X samples"  
- ✅ JSONL files created with reasonable sizes
- ✅ Validation shows proper JSON format
- ✅ Sample entries display correctly

### Performance Benchmarks
- **Small datasets (500 samples)**: ~30 seconds
- **Large datasets (1k samples)**: ~1-2 minutes  
- **Multiple datasets**: Process sequentially for reliability
- **Memory usage**: Minimal (~50MB peak for largest datasets)

---

The CSV to JSONL Converter v3 provides a complete, robust solution for preparing your educational datasets for TermuxTrain. With its flexible modes, comprehensive validation, and seamless integration capabilities, it ensures your datasets are properly formatted and ready for high-quality LLM training on mobile hardware.