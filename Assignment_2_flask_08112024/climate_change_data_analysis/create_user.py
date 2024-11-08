from app import app, db
from app.models import User

# Ensure the app context is pushed for database operations
with app.app_context():
    # Create a new user
    user = User(username='testuser', password='testpassword123', role='admin')
    db.session.add(user)
    db.session.commit()

    print("User created successfully!")
