class HDSKeyCollisionError(Exception):
    """
    Raised when two key hashes collied
    """
    pass


class HDSKeyError(Exception):
    """
    Raised when a key is not found, but expected
    """
    pass
