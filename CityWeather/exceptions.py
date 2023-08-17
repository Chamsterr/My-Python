class CantGetCoordinates(Exception):
    """Program can't get current GPS coordinates"""

class ApiServiceError(Exception):
    """Api service error"""

class JSONDecodeError(Exception):
    """JSON decode error"""