# Database Setup Guide

## Required Database

This project requires a SQLite database file named `yelpResData.db` with the following structure:

## Database Location

Place your database file in: `data/raw/yelpResData.db`

## Required Tables

### 1. `review` Table
Must contain the following columns:
- `reviewID` - Unique review identifier
- `reviewerID` - ID of the reviewer
- `restaurantID` - ID of the restaurant
- `date` - Review date
- `rating` - Review rating
- `usefulCount` - Number of useful votes
- `reviewContent` - The actual review text
- `flagged` - Flag indicating if review is fake ('Y') or authentic ('N')

### 2. `reviewer` Table
Must contain reviewer information:
- `reviewerID` - Unique reviewer identifier (primary key)
- `name` - Reviewer name
- `location` - Reviewer location
- `yelpJoinDate` - Date when reviewer joined Yelp
- Other reviewer-related columns

### 3. `restaurant` Table
Must contain restaurant information:
- `restaurantID` - Unique restaurant identifier (primary key)
- `rating` - Restaurant's average rating (as `restaurantRating` in queries)
- Other restaurant-related columns

## Example SQL Schema

```sql
-- Review table
CREATE TABLE review (
    reviewID TEXT PRIMARY KEY,
    reviewerID TEXT,
    restaurantID TEXT,
    date TEXT,
    rating INTEGER,
    usefulCount INTEGER,
    reviewContent TEXT,
    flagged TEXT CHECK(flagged IN ('Y', 'N'))
);

-- Reviewer table
CREATE TABLE reviewer (
    reviewerID TEXT PRIMARY KEY,
    name TEXT,
    location TEXT,
    yelpJoinDate TEXT
);

-- Restaurant table
CREATE TABLE restaurant (
    restaurantID TEXT PRIMARY KEY,
    rating REAL
);
```

## Getting Your Database

1. If you have the database file, simply copy it to `data/raw/yelpResData.db`
2. If you need to create a test database, you can use the schema above
3. The database should contain reviews with `flagged` values of 'Y' (fake) or 'N' (authentic)

## Verification

Once you've placed the database file, you can verify it by running:

```python
import sqlite3

conn = sqlite3.connect('data/raw/yelpResData.db')
cursor = conn.cursor()

# Check tables exist
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

# Check review table structure
cursor.execute("PRAGMA table_info(review);")
print("Review table columns:", cursor.fetchall())

conn.close()
```

## Running the Project

After placing the database file in `data/raw/yelpResData.db`, you can run:

```bash
python main.py
```
