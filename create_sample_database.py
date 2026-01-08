"""
Create Sample Database Script

This script creates a sample SQLite database with the required structure
for testing the fake review detection project.
"""

import sqlite3
import random
from datetime import datetime, timedelta
from pathlib import Path

# Sample review texts
AUTHENTIC_REVIEWS = [
    "Great food and excellent service. The staff was very friendly and attentive.",
    "I had a wonderful experience here. The ambiance is nice and the food was delicious.",
    "The restaurant has a cozy atmosphere. Food quality is good but a bit pricey.",
    "Nice place for a family dinner. Kids enjoyed the meal. Service was prompt.",
    "Average experience. Food was okay but nothing special. Service could be better.",
    "Disappointed with the service. Food took too long to arrive and was cold.",
    "Amazing food! Best restaurant in town. Highly recommend the pasta dishes.",
    "Good value for money. Portions are generous and food tastes great.",
    "The restaurant is clean and well-maintained. Staff is professional.",
    "Had a pleasant dinner here. The dessert menu is particularly good."
]

FAKE_REVIEWS = [
    "This place is absolutely amazing! Best restaurant ever! Five stars!",
    "Perfect in every way! Outstanding service and food! Highly recommend!",
    "Excellent! Wonderful! Fantastic! This restaurant is the best!",
    "Amazing food! Great service! Perfect atmosphere! Love it!",
    "Best restaurant! Excellent quality! Outstanding experience!",
    "Terrible place! Worst food ever! Do not go here!",
    "Horrible service! Bad food! Waste of money!",
    "This restaurant is terrible! Poor quality! Avoid at all costs!",
    "Worst experience! Bad food and service! Not recommended!",
    "Poor quality! Terrible service! Would not recommend!"
]

RESTAURANT_NAMES = [
    "The Golden Spoon", "Bella Vista", "Ocean Breeze", "Mountain View",
    "Sunset Grill", "City Lights", "Garden Paradise", "Royal Palace",
    "Cozy Corner", "The Chef's Table", "Riverside Cafe", "Downtown Diner"
]

REVIEWER_NAMES = [
    "John Smith", "Sarah Johnson", "Mike Davis", "Emily Brown",
    "David Wilson", "Lisa Anderson", "Chris Taylor", "Amy Martinez",
    "Robert Thomas", "Jennifer White", "James Harris", "Michelle Clark"
]

LOCATIONS = [
    "New York, NY", "Los Angeles, CA", "Chicago, IL", "Houston, TX",
    "Phoenix, AZ", "Philadelphia, PA", "San Antonio, TX", "San Diego, CA"
]


def create_database(db_path: str, num_reviews: int = 200):
    """
    Create a sample database with review data.
    
    Args:
        db_path: Path to the database file
        num_reviews: Number of reviews to generate
    """
    # Ensure directory exists
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    
    # Remove existing database if it exists
    if Path(db_path).exists():
        Path(db_path).unlink()
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create tables
    print("Creating database tables...")
    
    # Review table
    cursor.execute("""
        CREATE TABLE review (
            reviewID TEXT PRIMARY KEY,
            reviewerID TEXT,
            restaurantID TEXT,
            date TEXT,
            rating INTEGER,
            usefulCount INTEGER,
            reviewContent TEXT,
            flagged TEXT CHECK(flagged IN ('Y', 'N'))
        )
    """)
    
    # Reviewer table
    cursor.execute("""
        CREATE TABLE reviewer (
            reviewerID TEXT PRIMARY KEY,
            name TEXT,
            location TEXT,
            yelpJoinDate TEXT
        )
    """)
    
    # Restaurant table
    cursor.execute("""
        CREATE TABLE restaurant (
            restaurantID TEXT PRIMARY KEY,
            rating REAL
        )
    """)
    
    # Generate data
    print(f"Generating {num_reviews} reviews...")
    
    # Create reviewers
    reviewers = []
    for i in range(1, 21):  # 20 reviewers
        reviewer_id = f"R{i:04d}"
        name = random.choice(REVIEWER_NAMES)
        location = random.choice(LOCATIONS)
        join_date = datetime(2015, 1, 1) + timedelta(days=random.randint(0, 2000))
        yelp_join = join_date.strftime("%B %Y")
        
        reviewers.append((reviewer_id, name, location, yelp_join))
        cursor.execute(
            "INSERT INTO reviewer (reviewerID, name, location, yelpJoinDate) VALUES (?, ?, ?, ?)",
            (reviewer_id, name, location, yelp_join)
        )
    
    # Create restaurants
    restaurants = []
    for i in range(1, 13):  # 12 restaurants
        restaurant_id = f"RES{i:04d}"
        # Restaurant rating between 3.0 and 4.5
        rating = round(random.uniform(3.0, 4.5), 1)
        restaurants.append((restaurant_id, rating))
        cursor.execute(
            "INSERT INTO restaurant (restaurantID, rating) VALUES (?, ?)",
            (restaurant_id, rating)
        )
    
    # Generate reviews
    fake_count = 0
    authentic_count = 0
    
    for i in range(1, num_reviews + 1):
        review_id = f"REV{i:05d}"
        reviewer_id = random.choice(reviewers)[0]
        restaurant_id, restaurant_rating = random.choice(restaurants)
        
        # Determine if review is fake (30% chance)
        is_fake = random.random() < 0.3
        flagged = 'Y' if is_fake else 'N'
        
        if is_fake:
            fake_count += 1
            # Fake reviews tend to be extreme (1 or 5 stars)
            rating = random.choice([1, 5])
            review_text = random.choice(FAKE_REVIEWS)
            # Fake reviews often have lower useful counts
            useful_count = random.randint(0, 5)
        else:
            authentic_count += 1
            # Authentic reviews have more varied ratings
            rating = random.randint(1, 5)
            review_text = random.choice(AUTHENTIC_REVIEWS)
            useful_count = random.randint(0, 20)
        
        # Generate date (within last 2 years)
        review_date = datetime.now() - timedelta(days=random.randint(0, 730))
        date_str = review_date.strftime("%Y-%m-%d")
        
        cursor.execute("""
            INSERT INTO review 
            (reviewID, reviewerID, restaurantID, date, rating, usefulCount, reviewContent, flagged)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (review_id, reviewer_id, restaurant_id, date_str, rating, useful_count, review_text, flagged))
    
    conn.commit()
    conn.close()
    
    print(f"\nDatabase created successfully!")
    print(f"Location: {db_path}")
    print(f"Total reviews: {num_reviews}")
    print(f"  - Authentic (N): {authentic_count}")
    print(f"  - Fake (Y): {fake_count}")
    print(f"Reviewers: 20")
    print(f"Restaurants: 12")


if __name__ == "__main__":
    # Create database in data/raw directory
    project_root = Path(__file__).parent
    db_path = project_root / "data" / "raw" / "yelpResData.db"
    
    print("=" * 60)
    print("Creating Sample Database for Fake Review Detection")
    print("=" * 60)
    print()
    
    create_database(str(db_path), num_reviews=200)
    
    print()
    print("=" * 60)
    print("You can now run the project with: python main.py")
    print("=" * 60)
