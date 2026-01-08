# Fake Review Detection

Detection of fake online reviews using semi-supervised and supervised learning approaches.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Methodology](#methodology)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project implements machine learning models to detect fake online reviews. It uses both semi-supervised and supervised learning techniques, including Random Forest and Naive Bayes classifiers. The system analyzes various features extracted from reviews, reviewers, and restaurants to identify potentially fraudulent reviews.

## ✨ Features

- **Semi-Supervised Learning**: Utilizes pseudo-labeling to leverage unlabeled data
- **Multiple Algorithms**: Implements Random Forest and Naive Bayes classifiers
- **Feature Engineering**: Extracts meaningful features including:
  - Maximum Number of Reviews (MNR)
  - Review Length (RL)
  - Rating Deviation (RD)
  - Maximum Content Similarity
- **Data Preprocessing**: Comprehensive data cleaning and text preprocessing
- **Model Evaluation**: Detailed metrics including accuracy, precision, recall, and F1-score

## 📁 Project Structure

```
fake-review-detection/
├── src/
│   └── fake_review_detection/
│       ├── __init__.py
│       ├── data_loader.py      # Database loading functionality
│       ├── data_processor.py   # Data cleaning and preprocessing
│       ├── feature_engineer.py # Feature engineering
│       ├── models.py           # ML model implementations
│       ├── utils.py            # Utility functions
│       └── main.py             # Main pipeline
├── data/
│   ├── raw/                    # Raw data files (e.g., SQLite database)
│   └── processed/              # Processed data files
├── models/                     # Saved model files
├── notebooks/                  # Jupyter notebooks for exploration
├── tests/                      # Unit tests
├── docs/                       # Documentation
├── main.py                     # Entry point script
├── requirements.txt            # Python dependencies
├── pyproject.toml             # Project configuration
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/fake-review-detection.git
   cd fake-review-detection
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK data** (if not automatically downloaded)
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

5. **Prepare your data**
   - Place your SQLite database file (`yelpResData.db`) in the `data/raw/` directory
   - The database should contain tables: `review`, `reviewer`, and `restaurant`

## 💻 Usage

### Basic Usage

Run the main script to execute the complete pipeline:

```bash
python main.py
```

### Using as a Package

You can also import and use the modules in your own code:

```python
from src.fake_review_detection import (
    load_data,
    DataProcessor,
    FeatureEngineer,
    SemiSupervisedLearner
)
from sklearn.ensemble import RandomForestClassifier

# Load and process data
df = load_data()
processor = DataProcessor()
df = processor.clean(df)

# Engineer features
feature_engineer = FeatureEngineer()
df = feature_engineer.create_features(df)

# Train model
model = RandomForestClassifier(random_state=42)
learner = SemiSupervisedLearner(model, algorithm_name='Random Forest')
metrics = learner.train(df, threshold=0.7, iterations=15)
```

### Custom Configuration

You can customize the training parameters:

```python
learner = SemiSupervisedLearner(model, algorithm_name='My Model')
metrics = learner.train(
    df,
    threshold=0.8,      # Confidence threshold for pseudo-labeling
    iterations=20,       # Number of semi-supervised iterations
    test_size=0.2,       # Test set proportion
    random_state=42      # Random seed
)
```

## 🔬 Methodology

### Data Processing Pipeline

1. **Data Loading**: Loads review, reviewer, and restaurant data from SQLite database
2. **Data Cleaning**: 
   - Removes stopwords
   - Tokenizes text
   - Normalizes dates
   - Converts text to lowercase
3. **Feature Engineering**:
   - **MNR**: Normalized maximum number of reviews per reviewer per date
   - **RL**: Review length (word count)
   - **RD**: Rating deviation from restaurant average
   - **Maximum Content Similarity**: Cosine similarity between reviewer's reviews
4. **Data Balancing**: Under-sampling to balance fake and authentic reviews
5. **Model Training**: Semi-supervised learning with pseudo-labeling

### Semi-Supervised Learning

The semi-supervised approach:
1. Splits data into training and test sets
2. Trains on labeled training data
3. Predicts on test set with confidence scores
4. Adds high-confidence predictions to training set
5. Repeats until convergence or max iterations

### Models

- **Random Forest**: Ensemble method with 500 trees, entropy criterion
- **Naive Bayes**: Gaussian Naive Bayes classifier

## 📊 Evaluation Metrics

The models are evaluated using:
- **Accuracy**: Overall correctness
- **Precision**: True positives / (True positives + False positives)
- **Recall**: True positives / (True positives + False negatives)
- **F1-Score**: Harmonic mean of precision and recall
- **Confusion Matrix**: Detailed classification breakdown

## 📦 Requirements

See `requirements.txt` for the complete list. Key dependencies:

- `pandas>=2.2.0` - Data manipulation
- `numpy>=1.26.0` - Numerical computing
- `scikit-learn>=1.4.0` - Machine learning
- `nltk>=3.8.1` - Natural language processing
- `matplotlib>=3.8.0` - Visualization
- `seaborn>=0.13.0` - Statistical visualization
- `tqdm>=4.66.0` - Progress bars

## 🧪 Testing

Run tests (when available):

```bash
pytest tests/
```

## 📝 Notes

- The project expects a SQLite database with specific schema
- Default database path: `data/raw/yelpResData.db`
- Models use random seeds for reproducibility
- Processing time depends on dataset size

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

Your Name - [Your GitHub](https://github.com/Bhavana1025)

## 🙏 Acknowledgments

- Yelp dataset (if used)
- Scikit-learn community
- NLTK contributors

---

**Note**: Remember to update the database path and author information in the configuration files before sharing.
