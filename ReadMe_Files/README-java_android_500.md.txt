# Java Android Dataset (500 samples)

## Overview
This dataset provides 500 Java 6+ code examples focused on Android development, covering fundamentals through advanced topics using Android SDK and standard Java features.

## Categories (50 samples each)
1. Basic Syntax & Fundamentals
2. Object-Oriented Programming
3. Collections & Data Structures
4. Android UI Components
5. Android Activities & Lifecycle
6. File I/O & Storage
7. Threading & Async Tasks
8. JSON Parsing & APIs
9. Database (SQLite) Operations
10. Error Handling & Debugging

## File Structure
Each sample follows `instruction`, `input`, `output` columns in CSV format.

## Usage
1. Import CSV (`java_android_500.csv`) into training pipeline.
2. Parse `instruction` as prompt, compile and run `output` code to validate.

## Prerequisites
- Java 6+ and Android SDK
- Android emulator or device for UI components
- SQLite for database operations

## Testing
- Each sample was compiled with `javac` (Java code) or in Android Studio (Android-specific code) without errors.

## Integration
Use this dataset to fine-tune models for code synthesis, explanation, and debugging in Java/Android contexts.