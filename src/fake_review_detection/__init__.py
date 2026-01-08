"""
Fake Review Detection Package

A machine learning project for detecting fake online reviews using
semi-supervised and supervised learning approaches.
"""

__version__ = "1.0.0"
__author__ = "Your Name"

from .data_loader import load_data
from .data_processor import DataProcessor
from .feature_engineer import FeatureEngineer
from .models import SemiSupervisedLearner
from .utils import plot_confusion_matrix

__all__ = [
    "load_data",
    "DataProcessor",
    "FeatureEngineer",
    "SemiSupervisedLearner",
    "plot_confusion_matrix",
]
