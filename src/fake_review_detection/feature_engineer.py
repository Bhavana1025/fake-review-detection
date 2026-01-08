"""
Feature Engineering Module

Creates new features for the machine learning models.
"""

import pandas as pd
import numpy as np
from collections import OrderedDict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import pairwise_distances


class FeatureEngineer:
    """Handles feature engineering operations."""

    def __init__(self):
        """Initialize the feature engineer."""
        pass

    def create_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Create engineered features from the dataframe.

        Args:
            df: Cleaned dataframe.

        Returns:
            Dataframe with new features added.
        """
        print("Feature Engineering: Creating New Features")
        df = df.copy()

        # Feature 1: Maximum Number of Reviews (MNR) - normalized
        if 'reviewerID' in df.columns and 'date' in df.columns:
            mnr_df1 = df[['reviewerID', 'date']].copy()
            mnr_df2 = mnr_df1.groupby(by=['date', 'reviewerID']).size().reset_index(name='mnr')
            if mnr_df2['mnr'].max() > 0:
                mnr_df2['mnr'] = mnr_df2['mnr'] / mnr_df2['mnr'].max()
            df = df.merge(mnr_df2, on=['reviewerID', 'date'], how='inner')

        # Feature 2: Review Length (RL)
        if 'reviewContent' in df.columns:
            df['rl'] = df['reviewContent'].apply(lambda x: len(str(x).split()))

        # Feature 3: Rating Deviation (RD)
        if 'rating' in df.columns and 'restaurantRating' in df.columns:
            df['rd'] = abs(df['rating'] - df['restaurantRating']) / 4

        # Feature 4: Maximum Content Similarity
        if 'reviewerID' in df.columns and 'reviewContent' in df.columns:
            df = self._add_content_similarity(df)

        # Remove rows with NaN values
        df.dropna(inplace=True)

        print("Feature Engineering Complete")
        return df

    def _add_content_similarity(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate maximum content similarity for each reviewer.

        Args:
            df: Dataframe with review content.

        Returns:
            Dataframe with similarity feature added.
        """
        res = OrderedDict()
        for _, row in df.iterrows():
            res.setdefault(row.reviewerID, []).append(str(row.reviewContent))

        individual_reviewer = [
            {'reviewerID': k, 'reviewContent': v}
            for k, v in res.items()
        ]

        reviewers = []
        similarities = []
        vectorizer = TfidfVectorizer(min_df=0)

        for reviewer_data in individual_reviewer:
            try:
                if len(reviewer_data['reviewContent']) > 1:
                    tfidf = vectorizer.fit_transform(reviewer_data['reviewContent'])
                    cosine = 1 - pairwise_distances(tfidf, metric='cosine')
                    np.fill_diagonal(cosine, -np.inf)
                    max_sim = cosine.max()
                    if max_sim == -np.inf:
                        max_sim = 0
                else:
                    max_sim = 0
            except Exception:
                max_sim = 0

            reviewers.append(reviewer_data['reviewerID'])
            similarities.append(max_sim)

        similarity_df = pd.DataFrame({
            'reviewerID': reviewers,
            'Maximum Content Similarity': similarities
        })

        df = pd.merge(df, similarity_df, on="reviewerID", how="left")
        return df
