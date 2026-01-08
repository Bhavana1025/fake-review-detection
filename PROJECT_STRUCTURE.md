# Project Structure

This document describes the organization of the Fake Review Detection project.

## Directory Structure

```
fake-review-detection/
│
├── src/                          # Source code
│   └── fake_review_detection/    # Main package
│       ├── __init__.py           # Package initialization
│       ├── data_loader.py        # Database loading
│       ├── data_processor.py     # Data cleaning/preprocessing
│       ├── feature_engineer.py   # Feature engineering
│       ├── models.py             # ML model implementations
│       ├── utils.py              # Utility functions
│       └── main.py               # Main pipeline
│
├── data/                         # Data directory
│   ├── raw/                      # Raw data files (SQLite DB)
│   └── processed/                # Processed data files
│
├── models/                       # Saved model files
├── notebooks/                    # Jupyter notebooks
├── tests/                        # Unit tests
├── docs/                         # Documentation
│
├── main.py                       # Entry point script
├── setup.py                      # Package setup
├── pyproject.toml               # Modern Python project config
├── requirements.txt             # Python dependencies
├── config.example.py            # Configuration template
│
├── README.md                     # Main documentation
├── QUICKSTART.md                # Quick start guide
├── CONTRIBUTING.md              # Contribution guidelines
├── LICENSE                      # MIT License
└── .gitignore                   # Git ignore rules
```

## Module Descriptions

### `data_loader.py`
- **Purpose**: Loads data from SQLite database
- **Key Functions**: `load_data()`
- **Dependencies**: sqlite3, pandas

### `data_processor.py`
- **Purpose**: Cleans and preprocesses text data
- **Key Classes**: `DataProcessor`
- **Dependencies**: nltk, pandas

### `feature_engineer.py`
- **Purpose**: Creates engineered features for ML models
- **Key Classes**: `FeatureEngineer`
- **Features Created**:
  - MNR (Maximum Number of Reviews)
  - RL (Review Length)
  - RD (Rating Deviation)
  - Maximum Content Similarity
- **Dependencies**: sklearn, pandas, numpy

### `models.py`
- **Purpose**: Implements semi-supervised learning
- **Key Classes**: `SemiSupervisedLearner`
- **Dependencies**: sklearn, pandas, tqdm

### `utils.py`
- **Purpose**: Utility functions for visualization and data manipulation
- **Key Functions**: `plot_confusion_matrix()`, `under_sample()`
- **Dependencies**: matplotlib, sklearn, pandas

### `main.py`
- **Purpose**: Main execution pipeline
- **Workflow**: Load → Clean → Engineer → Train → Evaluate

## Data Flow

1. **Data Loading**: SQLite database → pandas DataFrame
2. **Data Cleaning**: Raw text → Cleaned text (stopwords removed, tokenized)
3. **Feature Engineering**: Cleaned data → Feature-rich DataFrame
4. **Data Balancing**: Imbalanced data → Balanced dataset
5. **Model Training**: Features → Trained models
6. **Evaluation**: Models → Metrics and visualizations

## File Naming Conventions

- Python modules: `snake_case.py`
- Classes: `PascalCase`
- Functions: `snake_case`
- Constants: `UPPER_SNAKE_CASE`

## Adding New Features

1. **New Data Source**: Add loader in `data_loader.py`
2. **New Preprocessing**: Extend `DataProcessor` class
3. **New Features**: Add methods to `FeatureEngineer` class
4. **New Models**: Create new learner class or extend `SemiSupervisedLearner`
5. **New Utilities**: Add functions to `utils.py`

## Testing

- Test files: `tests/test_*.py`
- Run tests: `pytest tests/`
- Test coverage: Aim for >80%

## Documentation

- Code documentation: Docstrings in all modules
- User documentation: README.md, QUICKSTART.md
- Developer documentation: CONTRIBUTING.md, PROJECT_STRUCTURE.md
