"""
Utility Functions Module

Contains helper functions for visualization and data manipulation.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix
from typing import List, Optional


def plot_confusion_matrix(
    y_true,
    y_pred,
    classes: List[str],
    title: Optional[str] = None,
    cmap=plt.cm.Blues,
    figsize: tuple = (8, 6)
) -> plt.Figure:
    """
    Plot a confusion matrix.

    Args:
        y_true: True labels.
        y_pred: Predicted labels.
        classes: List of class names.
        title: Title for the plot.
        cmap: Colormap for the plot.
        figsize: Figure size.

    Returns:
        Matplotlib figure object.
    """
    cm = confusion_matrix(y_true, y_pred)
    fig, ax = plt.subplots(figsize=figsize)
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)

    ax.set(
        xticks=np.arange(len(classes)),
        yticks=np.arange(len(classes)),
        xticklabels=classes,
        yticklabels=classes,
        title=title if title else 'Confusion Matrix',
        ylabel='True label',
        xlabel='Predicted label'
    )

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    fmt = 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(
                j, i, format(cm[i, j], fmt),
                ha="center", va="center",
                color="white" if cm[i, j] > thresh else "black"
            )

    fig.tight_layout()
    return fig


def under_sample(df, target_column: str = 'flagged', random_state: int = 42):
    """
    Perform under-sampling to balance the dataset.

    Args:
        df: Dataframe to balance.
        target_column: Name of the target column.
        random_state: Random state for reproducibility.

    Returns:
        Balanced dataframe.
    """
    print("Under-Sampling Data")
    sample_size = len(df[df[target_column] == 'Y'])
    authentic = df[df[target_column] == 'N'].sample(
        sample_size, random_state=random_state
    )
    fake = df[df[target_column] == 'Y']
    balanced_df = pd.concat([authentic, fake]).sample(frac=1, random_state=random_state)
    return balanced_df
