"""
Tests for data processor module.
"""

import pandas as pd
import pytest
from src.fake_review_detection.data_processor import DataProcessor


def test_data_processor_initialization():
    """Test DataProcessor initialization."""
    processor = DataProcessor()
    assert processor is not None
    assert processor.stop_words is not None
    assert processor.tokenizer is not None


def test_clean_basic():
    """Test basic data cleaning."""
    processor = DataProcessor()
    df = pd.DataFrame({
        'reviewContent': ['This is a great restaurant!', 'I love this place.'],
        'date': ['\n2024-01-01', '2024-01-02']
    })
    cleaned_df = processor.clean(df)
    assert 'reviewContent' in cleaned_df.columns
    assert len(cleaned_df) == 2
