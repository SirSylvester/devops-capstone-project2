"""
Flask CLI Command Extensions
"""
from service import app
from service.models import db


######################################################################
# Command to force tables to be rebuilt
# Usage:
#   flask db-create
######################################################################
@app.cli.command("db-create")
def db_create():
    """Recreates the database."""
    try:
        db.drop_all()  # Drop all tables
        db.create_all()  # Create all tables
        db.session.commit()
        print("Database tables created successfully")
    except Exception as e:
        print(f"Error creating database: {e}")
