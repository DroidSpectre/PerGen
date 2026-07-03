# Math/Logic/Reasoning Dataset for MicroLLM Training

## Dataset Overview
- **Purpose**: Train a specialized 96k parameter microLLM for mathematical reasoning
- **Total samples**: 4900
- **Format**: JSONL (JSON Lines) with Alpaca schema
- **Target**: Neural pathway formation for mathematical thinking

## Category Breakdown
- **Algebraic Thinking**: 600 samples
- **Basic Arithmetic**: 800 samples
- **Geometric Reasoning**: 400 samples
- **Logical Reasoning**: 600 samples
- **Number Theory**: 300 samples
- **Pattern Recognition**: 500 samples
- **Probability Statistics**: 400 samples
- **Step By Step Solving**: 600 samples
- **Word Problems**: 700 samples

## Difficulty Distribution
- **Easy**: 800 samples
- **Hard**: 900 samples
- **Medium**: 3200 samples

## Schema Structure
Each sample follows the Alpaca format:
```json
{
    "instruction": "The math problem or question",
    "input": "",
    "output": "Step-by-step solution with reasoning",
    "category": "problem_type",
    "difficulty": "easy|medium|hard"
}
```

## Design Principles for Neural Pathway Formation

### 1. Explicit Step-by-Step Reasoning
Every problem shows the complete thought process, helping the model learn:
- Problem identification
- Solution strategy selection  
- Step-by-step execution
- Result verification

### 2. Progressive Complexity
- **Easy (800 samples)**: Basic arithmetic operations
- **Medium (3200 samples)**: Multi-step problems, word problems, patterns
- **Hard (900 samples)**: Complex reasoning, multi-step algebra

### 3. Mathematical Categories for Specialized Pathways

#### Basic Arithmetic (800 samples)
Foundation for all mathematical thinking:
- Addition, subtraction, multiplication, division
- Order of operations
- Mental math strategies

#### Algebraic Thinking (600 samples) 
Abstract reasoning development:
- Linear equation solving
- Variable manipulation
- Expression simplification

#### Logical Reasoning (600 samples)
Critical thinking pathways:
- If-then statements
- Deductive reasoning
- Truth tables
- Logical comparisons

#### Word Problems (700 samples)
Real-world application:
- Context interpretation
- Mathematical modeling
- Multi-step problem solving

#### Pattern Recognition (500 samples)
Sequence and structure understanding:
- Arithmetic sequences
- Geometric sequences
- Fibonacci patterns
- Alternating patterns

#### Geometric Reasoning (400 samples)
Spatial mathematical thinking:
- Area and perimeter calculations
- Volume computations
- Angle relationships
- Shape properties

#### Probability & Statistics (400 samples)
Statistical reasoning:
- Basic probability
- Mean and median
- Data interpretation
- Combinations

#### Step-by-Step Solving (600 samples)
Systematic approach reinforcement:
- Multi-step arithmetic
- Equation solving methodology
- Problem decomposition

#### Number Theory (300 samples)
Deep mathematical understanding:
- Prime numbers
- Factors and multiples
- Divisibility rules
- Mathematical properties

## Training Recommendations

### For Neural Pathway Formation:
1. **Sequential Training**: Train categories in order of complexity
2. **Repetition**: Multiple epochs to reinforce patterns
3. **Mixed Batches**: Combine different categories for generalization
4. **Validation**: Use held-out samples to test reasoning transfer

### Specialized Model Architecture:
- Target: 96k parameters for mobile deployment
- Attention heads: Focus on sequential reasoning
- Layer depth: Sufficient for multi-step thinking
- Vocabulary: Math-specific tokenization

## Usage with TermuxTrain System:
```python
# Load and train the math specialist model
processor = TermuxJSONLProcessor(schema="alpaca", vocab_size=1000)
model = create_micro_llm(vocab_size=1000) 
trainer = MicroTrainer(model)

# Train on math dataset
processor.train_tokenizer("math_reasoning_dataset_5000.jsonl")
for batch in processor.create_training_batches("math_reasoning_dataset_5000.jsonl"):
    trainer.train_step(batch)
```

This dataset is designed to create a specialized mathematical reasoning module that can work alongside other specialized models in a multi-model brain-inspired system.