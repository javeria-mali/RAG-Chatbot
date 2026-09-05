from .db import users_collection
import bcrypt


def register_user(name, email, password):
    # Check if user already exists
    existing_user = users_collection.find_one({"email": email})

    if existing_user:
        return False, "Email already registered!"

    # Hash password before saving
    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    # Create user
    user = {
        "name": name,
        "email": email,
        "password": hashed_password
    }

    users_collection.insert_one(user)

    return True, "Registration successful!"


def login_user(email, password):
    # Find user by email
    user = users_collection.find_one({"email": email})

    if not user:
        return False, "Invalid email or password!"

    # Check password
    password_correct = bcrypt.checkpw(
        password.encode("utf-8"),
        user["password"]
    )

    if not password_correct:
        return False, "Invalid email or password!"

    return True, "Login successful!"