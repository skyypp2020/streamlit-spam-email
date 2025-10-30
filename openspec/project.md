# Project Context

## Purpose
Build a spam email classification system using machine learning techniques to automatically identify and filter spam emails from legitimate ones.

## Tech Stack
- Python 3.x
- scikit-learn for machine learning
- pandas for data manipulation
- Jupyter Notebooks for analysis and development
- pytest for testing

## Project Conventions

### Code Style
- Follow PEP 8 conventions for Python code
- Use descriptive variable names in snake_case
- Include docstrings for all functions and classes
- Maximum line length of 88 characters (Black formatter standard)

### Architecture Patterns
- Modular design with separate concerns:
  - Data preprocessing
  - Feature engineering
  - Model training
  - Evaluation
  - Inference
- Use object-oriented patterns for model implementations
- Implement pipeline pattern for data processing steps

### Testing Strategy
- Unit tests for all core functions
- Integration tests for data pipelines
- Model evaluation metrics:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - Confusion matrix

### Git Workflow
- Feature branches for new capabilities
- Main branch for stable releases
- Commit messages follow conventional commits format
- Pull request reviews required for merges

## Domain Context
- Email classification is a binary classification problem (spam/ham)
- Text preprocessing is crucial for email content
- Features may include:
  - Text statistics
  - Word frequencies
  - URL patterns
  - Header information
- Class imbalance handling may be required
- Performance metrics must consider both false positives and negatives

## Important Constraints
- Model inference time should be < 100ms per email
- False positive rate should be < 1%
- Model size should be < 100MB
- Must handle various text encodings
- Privacy considerations for email content

## External Dependencies
- NLTK for text processing
- spaCy for advanced NLP (optional)
- scikit-learn for ML algorithms
- joblib for model serialization
