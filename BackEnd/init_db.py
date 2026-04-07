"""
Database initialization script
Creates default admin and viewer accounts for testing
"""

import sys
from pathlib import Path

# Add backend directory to path
sys.path.insert(0, str(Path(__file__).parent))

from database import SessionLocal, engine
from models import Base, User
from main import hash_password

# Drop all existing tables and create fresh ones
print("Creating database tables...")
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:
    # Create admin user
    admin = User(
        username="admin",
        name="แอดมิน",
        password=hash_password("password123"),
        role="admin"
    )
    db.add(admin)
    
    # Create viewer user
    viewer = User(
        username="viewer",
        name="ผู้ใช้งาน",
        password=hash_password("password123"),
        role="viewer"
    )
    db.add(viewer)
    
    db.commit()
    print("✓ Created admin user (username: admin, password: password123)")
    print("✓ Created viewer user (username: viewer, password: password123)")
    print("\n✓ Database initialization complete!")
    print("\nDefault Credentials:")
    print("  Admin  - username: admin, password: password123")
    print("  Viewer - username: viewer, password: password123")

except Exception as e:
    print(f"✗ Error: {e}")
    db.rollback()

finally:
    db.close()

