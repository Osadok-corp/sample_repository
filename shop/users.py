import hashlib
import re


def is_valid_email(email):
    """Check that the email address has a valid format."""
    return re.fullmatch(r"[^@\s]+@[^@\s]+\.[a-z]{2,}", email) is not None


def hash_password(password, salt):
    """Return a SHA-256 hash of the password with salt."""
    return hashlib.sha256((salt + password).encode("utf-8")).hexdigest()


class User:
    """Registered shop customer."""

    def __init__(self, email, password, salt="static-salt"):
        if not is_valid_email(email):
            raise ValueError("invalid email")
        self.email = email
        self.password_hash = hash_password(password, salt)
