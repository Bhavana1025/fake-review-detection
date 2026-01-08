"""
Machine Learning Models Module

Implements semi-supervised learning algorithms for fake review detection.
"""

import pandas as pd
import numpy as np
from typing import Any, Dict
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)
from tqdm import tqdm


class SemiSupervisedLearner:
    """Semi-supervised learning wrapper for scikit-learn models."""

    def __init__(self, model: Any, algorithm_name: str = "Model"):
        """
        Initialize the semi-supervised learner.

        Args:
            model: Scikit-learn compatible model with fit, predict, and predict_proba methods.
            algorithm_name: Name of the algorithm for display purposes.
        """
        self.model = model
        self.algorithm_name = algorithm_name

    def train(
        self,
        df: pd.DataFrame,
        target_column: str = 'flagged',
        test_size: float = 0.25,
        threshold: float = 0.8,
        iterations: int = 40,
        random_state: int = 42,
        drop_columns: list = None
    ) -> Dict[str, Any]:
        """
        Train the model using semi-supervised learning.

        Args:
            df: Dataframe with features and target.
            target_column: Name of the target column.
            test_size: Proportion of data to use for testing.
            threshold: Confidence threshold for pseudo-labeling.
            iterations: Maximum number of iterations.
            random_state: Random state for reproducibility.
            drop_columns: Columns to drop before training.

        Returns:
            Dictionary containing evaluation metrics and predictions.
        """
        print(f"Training {self.algorithm_name} Model")

        if drop_columns is None:
            drop_columns = [
                'reviewID', 'reviewerID', 'restaurantID', 'date',
                'name', 'location', 'yelpJoinDate', 'flagged',
                'reviewContent', 'restaurantRating'
            ]

        labels = df[target_column].copy()
        features = df.drop(
            [col for col in drop_columns if col in df.columns],
            axis=1,
            errors='ignore'
        )

        X_train, X_test, y_train, y_test = train_test_split(
            features, labels, test_size=test_size, random_state=random_state
        )

        X_test_copy = X_test.copy()
        y_test_copy = y_test.copy()

        # Semi-supervised learning loop
        current_iteration = 0
        pbar = tqdm(total=iterations, desc=f"{self.algorithm_name} Training")

        while not X_test.empty and current_iteration < iterations:
            current_iteration += 1

            # Train on current labeled data
            self.model.fit(X_train, y_train)

            # Get predictions and probabilities
            probs = self.model.predict_proba(X_test)
            preds = self.model.predict(X_test)

            # Find confident predictions
            max_probs = np.max(probs, axis=1)
            confident_mask = max_probs > threshold
            confident_indices = X_test.index[confident_mask].tolist()

            # Add confident predictions to training set
            if confident_indices:
                X_train = pd.concat([X_train, X_test.loc[confident_indices]])
                y_train = pd.concat([y_train, pd.Series(
                    preds[confident_mask],
                    index=confident_indices
                )])

                # Remove from test set
                X_test = X_test.drop(confident_indices)
                y_test = y_test.drop(confident_indices)

            pbar.update(1)

        pbar.close()

        # Final evaluation
        final_preds = self.model.predict(X_test_copy)

        # Calculate metrics
        metrics = {
            'accuracy': accuracy_score(y_test_copy, final_preds),
            'precision': precision_score(y_test_copy, final_preds, pos_label="Y", zero_division=0),
            'recall': recall_score(y_test_copy, final_preds, pos_label="Y", zero_division=0),
            'f1': f1_score(y_test_copy, final_preds, pos_label="Y", zero_division=0),
            'confusion_matrix': confusion_matrix(y_test_copy, final_preds),
            'predictions': final_preds,
            'true_labels': y_test_copy
        }

        # Print results
        print(f"\n{self.algorithm_name} Model Results")
        print("--" * 20)
        print(f'Accuracy Score: {metrics["accuracy"]:.4f}')
        print(f'Precision Score: {metrics["precision"]:.4f}')
        print(f'Recall Score: {metrics["recall"]:.4f}')
        print(f'F1 Score: {metrics["f1"]:.4f}')
        print(f'Confusion Matrix:\n{metrics["confusion_matrix"]}')

        return metrics
