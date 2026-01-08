"""
Configuration file example.

Copy this file to config.py and update with your settings.
"""

# Database Configuration
DATABASE_PATH = "data/raw/yelpResData.db"

# Model Configuration
RANDOM_STATE = 42
TEST_SIZE = 0.25

# Random Forest Parameters
RF_PARAMS = {
    'random_state': 42,
    'criterion': 'entropy',
    'max_depth': 14,
    'max_features': 'sqrt',
    'n_estimators': 500
}

# Naive Bayes Parameters
NB_PARAMS = {}

# Semi-Supervised Learning Parameters
SEMI_SUPERVISED_PARAMS = {
    'threshold': 0.7,
    'iterations': 15
}

# Feature Engineering
FEATURE_COLUMNS_TO_DROP = [
    'reviewID',
    'reviewerID',
    'restaurantID',
    'date',
    'name',
    'location',
    'yelpJoinDate',
    'flagged',
    'reviewContent',
    'restaurantRating'
]
