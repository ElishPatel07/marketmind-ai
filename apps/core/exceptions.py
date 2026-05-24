"""
Custom application exceptions.

These exceptions provide:
- consistent error handling
- predictable API responses
- cleaner service logic
"""


class MarketMindException(Exception):
    """
    Base application exception.
    """

    def __init__(
        self,
        message: str,
    ):
        self.message = message

        super().__init__(message)


class ArticleNotFoundException(MarketMindException):
    """
    Raised when article does not exist.
    """


class DatabaseOperationException(MarketMindException):
    """
    Raised for database operation failures.
    """
