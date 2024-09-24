from typing import Any, Dict


class CryptoComAiAgentResponse:
    """
    A class representing the response from the CDC AI Agent service.

    Attributes:
        status (str): The status of the response (e.g., Success, Failed).
        result (Dict[str, Any]): The result of the query, containing action, message, and other data.
    """

    def __init__(self, status: str, result: Dict[str, Any]):
        """
        Initialize the CryptoComAiAgentResponse object.

        Args:
            status (str): The status of the response (Success or Failed).
            result (Dict[str, Any]): A dictionary containing the result of the AI query.
        """
        self.status = status
        self.result = result

    def __repr__(self):
        """
        Provide a string representation for debugging purposes.

        Returns:
            str: A string showing the status and result of the response.
        """
        return f"CryptoComAiAgentResponse(status={self.status}, result={self.result})"

    def __str__(self):
        """
        Provide a user-friendly string representation of the response.

        Returns:
            str: A formatted string with the status and result of the response.
        """
        return f"Status: {self.status}, Result: {self.result}"

class Method:
    """
    A class representing HTTP methods used for interacting with the CDC AI Agent service.

    Attributes:
        GET (str): Represents the GET HTTP method.
        POST (str): Represents the POST HTTP method.
        PUT (str): Represents the PUT HTTP method.
        DELETE (str): Represents the DELETE HTTP method.
    """
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
