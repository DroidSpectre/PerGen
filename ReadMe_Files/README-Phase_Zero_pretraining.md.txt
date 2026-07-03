# TermuxTrain Tokenizer Pre-Training Guide
# Phase 0: Base Vocabulary Training for Enhanced BPE Tokenizer

## Overview
This guide explains how to use the custom tokenizer training dataset I generated for optimal BPE training before your main educational datasets.

## Dataset Specifications

### Generated Dataset: `tokenizer-training-dataset.jsonl`
- **Total Samples**: 625+ comprehensive training examples
- **Format**: JSONL with text, source, category, and sample_id fields
- **Purpose**: Pre-train BPE tokenizer with essential vocabulary patterns
- **Coverage**: All character patterns, symbols, and terminology needed for your educational datasets

### Vocabulary Coverage Categories:

1. **Basic Language Patterns** (40 samples)
   - Complete alphabet coverage via pangrams
   - Common idioms and phrases
   - Various sentence structures and writing styles
   - Punctuation and formatting examples

2. **Mathematics & Science** (80 samples) 
   - Numbers 1-50 with arithmetic operations
   - Mathematical expressions and equations
   - Scientific formulas and constants
   - Chemical elements and compounds
   - Physics terminology and concepts

3. **Technology & Programming** (190 samples)
   - Programming language names and concepts
   - Data structures and algorithms
   - Web development terminology
   - File formats and protocols
   - Technical vocabulary

4. **Academic Disciplines** (135 samples)
   - Literature and language arts terms
   - Historical periods and events
   - Research methodology vocabulary
   - Academic field terminology across 7 major disciplines

5. **Conversational Patterns** (80 samples)
   - Social interactions and greetings
   - Question-answer patterns
   - Instruction-following language
   - Professional communication

6. **Formatting & Special Characters** (100 samples)
   - Punctuation marks and symbols
   - Mathematical notation
   - Currency and numbering systems
   - Code snippets and file paths
   - Mixed formatting examples

## Integration with TermuxTrain

### Step 1: Tokenizer Pre-Training
```python
# Use the pre-training dataset FIRST
from llm_data_processor_v03 import EnhancedBPETokenizer

# Initialize tokenizer
tokenizer = EnhancedBPETokenizer(vocab_size=32000)

# Pre-train on base vocabulary dataset
base_texts = []
with open('tokenizer-training-dataset.jsonl', 'r') as f:
    for line in f:
        data = json.loads(line)
        base_texts.append(data['text'])

# Train BPE on base vocabulary
tokenizer.train_bpe(base_texts, min_frequency=1)  # Lower frequency for comprehensive coverage

# Save base tokenizer
tokenizer.save_tokenizer('base_tokenizer_pretrained.pkl')
```

### Step 2: Fine-tune with Your Educational Datasets
```python
# Load pre-trained tokenizer
tokenizer.load_tokenizer('base_tokenizer_pretrained.pkl')

# Add vocabulary from your educational datasets
educational_texts = []

# Sample from your datasets
for dataset_path in ['MATH.jsonl', 'SCIENCE.jsonl', 'LITERATURE.jsonl', 'REASONING.jsonl', 'GENERAL_KNOWLEDGE.jsonl']:
    # Add 100 samples from each
    with open(dataset_path, 'r') as f:
        for i, line in enumerate(f):
            if i >= 100:
                break
            data = json.loads(line)
            educational_texts.append(data['instruction'])
            educational_texts.append(data['output'])

# Continue training with educational content
tokenizer.train_bpe(base_texts + educational_texts, min_frequency=2)

# Save final comprehensive tokenizer
tokenizer.save_tokenizer('comprehensive_tokenizer.pkl')
```

### Step 3: Use in Training Pipeline
```python
# In your training script
from llm_trainer_v4_1 import EnhancedLLMTrainer

# Initialize trainer
trainer = EnhancedLLMTrainer(model_config, training_config)

# Load pre-trained comprehensive tokenizer
if trainer.load_tokenizer('comprehensive_tokenizer.pkl'):
    print("✅ Loaded comprehensive pre-trained tokenizer")
    
    # Initialize model with trained tokenizer
    trainer.initialize_model()
    
    # Begin training phases
    # ... rest of training
```

## Benefits of Pre-Training Approach

### ✅ Robust Vocabulary Foundation
- Ensures all common patterns are tokenized efficiently
- Prevents over-segmentation of technical terms
- Creates consistent tokenization across different domains

### ✅ Better Educational Content Handling
- Mathematical expressions tokenized as meaningful units
- Scientific terminology preserved as coherent tokens
- Programming concepts maintained as single tokens

### ✅ Improved Model Performance
- Reduced out-of-vocabulary issues
- More efficient sequence representation
- Better generalization across educational domains

### ✅ Mobile-Optimized Efficiency
- Smaller vocabulary needed for same coverage
- Faster inference due to better tokenization
- Reduced memory usage during training

## Expected Results

### Tokenization Quality
- **Mathematical expressions**: "x^2 + 2x + 1" → meaningful subword units
- **Scientific terms**: "photosynthesis" → single token or 2-3 meaningful parts
- **Technical vocabulary**: "JavaScript" → single token, not "Java" + "Script"
- **Academic language**: "metaphor" → single token, specialized terms preserved

### Vocabulary Statistics (Expected)
- **Coverage**: 95%+ of educational content with trained vocabulary
- **Efficiency**: 30-40% fewer tokens needed vs. character-level
- **Quality**: Technical terms preserved as meaningful units
- **Size**: ~25,000-30,000 active tokens from 32,000 capacity

## Usage Recommendations

### Phase 0 (Pre-training): Use This Dataset
- Train base vocabulary with comprehensive patterns
- Establish foundation for all educational domains
- Create robust tokenization for technical content

### Phase 1 (Educational Fine-tuning): Your Datasets  
- Continue training with samples from your 5 educational datasets
- Adapt tokenizer to specific instructional patterns
- Fine-tune for optimal educational content handling

### Phase 2 (Model Training): Complete Pipeline
- Use comprehensive tokenizer for all training phases
- Benefit from consistent, high-quality tokenization
- Achieve better model performance with optimized vocabulary

## Quality Assurance

The pre-training dataset includes:
- ✅ All 26 letters in various combinations (pangrams)
- ✅ Numbers 0-9 in multiple contexts and formats
- ✅ Complete punctuation and symbol coverage
- ✅ Mathematical and scientific notation
- ✅ Programming and technical terminology
- ✅ Academic vocabulary across major disciplines
- ✅ Conversational and instructional patterns
- ✅ Formatting and special character examples

This ensures your tokenizer will handle any content in your educational datasets with optimal efficiency and quality.

---

**Next Steps**: 
1. Use this pre-training dataset FIRST to establish base vocabulary
2. Then continue training with samples from your educational datasets  
3. Save the comprehensive tokenizer for use in your training pipeline
4. Begin Phase 1 training with robust, domain-optimized tokenization