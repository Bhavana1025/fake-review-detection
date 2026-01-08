"""
Data Loading Module

Handles loading data from SQLite database.
"""

import sqlite3
import pandas as pd
from pathlib import Path
from typing import Optional


def load_data(db_path: Optional[str] = None) -> pd.DataFrame:
    """
    Load review data from SQLite database.

    Args:
        db_path: Path to the SQLite database file. If None, looks for
                 'yelpResData.db' in the data/raw directory.

    Returns:
        DataFrame containing merged review, reviewer, and restaurant data.
    """
    if db_path is None:
        # Default path: look in data/raw directory
        # Go up from src/fake_review_detection/data_loader.py to project root
        current_file = Path(__file__).resolve()
        project_root = current_file.parent.parent.parent.parent
        db_path = project_root / "data" / "raw" / "yelpResData.db"
        
        # If not found, try relative to current working directory
        if not db_path.exists():
            cwd_db_path = Path("data") / "raw" / "yelpResData.db"
            if cwd_db_path.exists():
                db_path = cwd_db_path.resolve()
            elif (project_root / "Data" / "yelpResData.db").exists():
                # Fallback to old location
                db_path = project_root / "Data" / "yelpResData.db"

    if not db_path.exists():
        raise FileNotFoundError(
            f"Database file not found at: {db_path}\n"
            f"Please place your SQLite database file (yelpResData.db) in the 'data/raw/' directory.\n"
            f"The database should contain tables: 'review', 'reviewer', and 'restaurant'."
        )

    print(f"Loading Data from Database: {db_path}")
    conn = sqlite3.connect(str(db_path))
    conn.text_factory = lambda x: str(x, 'gb2312', 'ignore')
    cursor = conn.cursor()

    # Load review data
    cursor.execute("""
        SELECT reviewID, reviewerID, restaurantID, date, rating, 
               usefulCount as reviewUsefulCount, reviewContent, flagged 
        FROM review 
        WHERE flagged in ('Y','N')
    """)
    review_df = pd.DataFrame(
        cursor.fetchall(),
        columns=[column[0] for column in cursor.description]
    )

    # Load reviewer data
    cursor.execute("SELECT * FROM reviewer")
    reviewer_df = pd.DataFrame(
        cursor.fetchall(),
        columns=[column[0] for column in cursor.description]
    )

    # Load restaurant data
    cursor.execute("SELECT restaurantID, rating as restaurantRating FROM restaurant")
    restaurant_df = pd.DataFrame(
        cursor.fetchall(),
        columns=[column[0] for column in cursor.description]
    )

    # Merge all dataframes
    df = review_df.merge(reviewer_df, on='reviewerID', how='inner')
    df = df.merge(restaurant_df, on='restaurantID', how='inner')

    conn.close()
    print("Data Load Complete")
    return df
