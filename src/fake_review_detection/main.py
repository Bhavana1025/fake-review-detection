"""
Main Script

Entry point for running the fake review detection pipeline.
"""

import pandas as pd
import matplotlib.pyplot as plt
from time import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

from .data_loader import load_data
from .data_processor import DataProcessor
from .feature_engineer import FeatureEngineer
from .models import SemiSupervisedLearner
from .utils import plot_confusion_matrix, under_sample


def main():
    """Main execution function."""
    start_time = time()

    # Load data
    df = load_data()

    # Process data
    processor = DataProcessor()
    df = processor.clean(df)

    # Engineer features
    feature_engineer = FeatureEngineer()
    df = feature_engineer.create_features(df)

    # Balance dataset
    df = under_sample(df)

    # Initialize models
    rf_model = RandomForestClassifier(
        random_state=42,
        criterion='entropy',
        max_depth=14,
        max_features='sqrt',
        n_estimators=500
    )
    nb_model = GaussianNB()

    # Train Random Forest
    rf_learner = SemiSupervisedLearner(rf_model, algorithm_name='Random Forest')
    rf_metrics = rf_learner.train(
        df,
        threshold=0.7,
        iterations=15
    )
    plot_confusion_matrix(
        rf_metrics['true_labels'],
        rf_metrics['predictions'],
        ['N', 'Y'],
        'Random Forest Confusion Matrix'
    )
    plt.show()

    # Train Naive Bayes
    nb_learner = SemiSupervisedLearner(nb_model, algorithm_name='Naive Bayes')
    nb_metrics = nb_learner.train(
        df,
        threshold=0.7,
        iterations=15
    )
    plot_confusion_matrix(
        nb_metrics['true_labels'],
        nb_metrics['predictions'],
        ['N', 'Y'],
        'Naive Bayes Confusion Matrix'
    )
    plt.show()

    print(f"\nTotal Time taken: {time() - start_time:.2f} seconds")


if __name__ == '__main__':
    main()
