class UserNotFoundException(Exception):
    """Raised when a user is not found in the database."""
    def __init__(self, userId):
        message = f"User with ID '{userId}' not found in the database."
        super().__init__(message)
