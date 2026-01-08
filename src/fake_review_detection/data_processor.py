"""
Data Processing Module

Handles data cleaning and preprocessing operations.
"""

import pandas as pd
from datetime import datetime
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import nltk

# Download required NLTK data if not already present
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)


class DataProcessor:
    """Handles data cleaning and preprocessing."""

    def __init__(self):
        """Initialize the data processor."""
        self.stop_words = set(stopwords.words('english'))
        self.tokenizer = RegexpTokenizer(r'\w+')

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean and preprocess the dataframe.

        Args:
            df: Raw dataframe to clean.

        Returns:
            Cleaned dataframe.
        """
        print("Cleaning Data")
        df = df.copy()

        # Clean date column
        if 'date' in df.columns:
            df['date'] = df['date'].apply(
                lambda x: x[1:] if isinstance(x, str) and x.startswith('\n') else x
            )

        # Format yelpJoinDate
        if 'yelpJoinDate' in df.columns:
            df['yelpJoinDate'] = df['yelpJoinDate'].apply(
                lambda x: datetime.strftime(
                    datetime.strptime(x, '%B %Y'), '01/%m/%Y'
                ) if isinstance(x, str) else x
            )

        # Clean review content
        if 'reviewContent' in df.columns:
            # Remove stopwords
            df['reviewContent'] = df['reviewContent'].apply(
                lambda x: ' '.join(
                    word for word in str(x).split()
                    if word.lower() not in self.stop_words
                )
            )
            # Tokenize
            df['reviewContent'] = df['reviewContent'].apply(
                lambda x: ' '.join(self.tokenizer.tokenize(str(x)))
            )
            # Convert to lowercase
            df['reviewContent'] = df['reviewContent'].str.lower()

        print("Data Cleaning Complete")
        return df
