# Quick Start Guide

Get up and running with the Fake Review Detection project in minutes!

## Prerequisites

- Python 3.9 or higher
- pip package manager

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/fake-review-detection.git
cd fake-review-detection
```

### 2. Set Up Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download NLTK Data

The first time you run the code, NLTK will automatically download required data. If you want to download manually:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### 5. Prepare Your Data

Place your SQLite database file (`yelpResData.db`) in the `data/raw/` directory.

The database should have the following tables:
- `review` - Contains review data with columns: reviewID, reviewerID, restaurantID, date, rating, usefulCount, reviewContent, flagged
- `reviewer` - Contains reviewer information
- `restaurant` - Contains restaurant data with columns: restaurantID, rating

### 6. Run the Project

```bash
python main.py
```

## Expected Output

The script will:
1. Load data from the database
2. Clean and preprocess the data
3. Engineer features
4. Train Random Forest and Naive Bayes models
5. Display evaluation metrics and confusion matrices

## Troubleshooting

### Database Not Found

If you get a database error, ensure:
- The database file is in `data/raw/yelpResData.db`
- The file path is correct
- The database has the required tables

### NLTK Data Missing

If you see NLTK errors, run:
```python
import nltk
nltk.download('all')
```

### Import Errors

Make sure you're in the project root directory and the virtual environment is activated.

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check out the [CONTRIBUTING.md](CONTRIBUTING.md) guide if you want to contribute
- Explore the code in `src/fake_review_detection/` to understand the implementation

## Need Help?

Open an issue on GitHub or check the documentation in the `docs/` directory.
