class ArtWorkNotFoundException(Exception):
    """Raised when an artwork is not found in the database."""
    def __init__(self, artworkId):
        message = f"Artwork with ID '{artworkId}' not found in the database."
        super().__init__(message)

