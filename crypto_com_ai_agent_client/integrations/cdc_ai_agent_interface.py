from enum import Enum
from typing import Any, Dict, List, Optional


class Role(Enum):
    """
    Enum respresenting the role of a QueryContext
    """
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


class QueryContext:
    """
    A class representing the context within a CryptoComAiAgentResponse.

    Attributes:
        role (Role): The role of the context (e.g., system, user, assistant).
        content (str): The content of the context.
    """

    def __init__(self, role: Role, content: str):
        self.role = role
        self.content = content

    def __repr__(self):
        return f"QueryContext(role={self.role}, content={self.content})"

    def __str__(self):
        return f"QueryContext(role={self.role}, content={self.content})"


class Status(Enum):
    """
    Enum respresenting the status of a Result
    """
    SUCCESS = "success"
    ERROR = "error"


class Result:
    """
    A class representing the result of a CryptoComAiAgentResponse.

    Attributes:
        status (str): The status of the result.
        function (str): The function associated with the result.
        message (str): A message describing the result.
        data (Dict[str, Any]): Additional data associated with the result.
    """

    def __init__(self, status: Status, function: str, message: str, data: Dict[str, Any]):
        self.status = status
        self.function = function
        self.message = message
        self.data = data

    def __repr__(self):
        return f"Result(status={self.status}, function={self.function}, message={self.message}, data={self.data})"


class CryptoComAiAgentResponse:
    """
    A class representing the response from the CDC AI Agent service.

    Attributes:
        status (str): The status of the response. (e.g. "success" or "failed")
        message (Optional[str]): An optional message from the response describing any errors.
        has_errors (Optional[bool]): Indicates whether the results list contains any errors.
        results (Optional[List[Result]]): The results of the query, if available.
        context (Optional[List[QueryContext]]): The context of the query, if available.
    """

    def __init__(self, status: str, message: Optional[str] = None,
                 hasErrors: Optional[bool] = None, results: Optional[List[Dict[str, Any]]] = None,
                 context: Optional[List[Dict[str, Any]]] = None):
        """
        Initialize the CryptoComAiAgentResponse object.

        Args:
            status (str): The status of the response. (e.g. "success" or "failed")
            message (Optional[str]): An optional message from the response describing any errors.
            hasErrors (Optional[bool]): Indicates whether the results list contains any errors.
            results (Optional[List[Dict[str, Any]]]): The results of the query, if available.
            context (Optional[List[Dict[str, Any]]]): The context of the query, if available.
        """
        self.status = status
        self.message = message
        self.hasErrors = hasErrors
        self.results = [Result(r['status'], r['function'],
                               r['message'], r['data']) for r in results] if results else None
        self.context = [QueryContext((r['role']), r['content'])
                        for r in context] if context else None

    @property
    def has_errors(self):
        """
        Get the has_errors property. The property is named hasErrors in the response from the API.
        """
        return self.hasErrors

    def __repr__(self):
        """
        Provide a string representation for debugging purposes.

        Returns:
            str: A string showing the attributes of the response.
        """
        return (f"CryptoComAiAgentResponse(status={self.status}, message={self.message}, "
                f"has_errors={self.has_errors}, results={self.results}, context={self.context})")

    def __str__(self):
        """
        Provide a user-friendly string representation of the response.

        Returns:
            str: A formatted string with the attributes of the response.
        """
        return (f"Status: {self.status}, Message: {self.message}, Has Errors: {self.has_errors}, "
                f"Results: {self.results}, Context: {self.context}")

    def to_dict(self):
        """
        Convert the CryptoComAiAgentResponse object to a dictionary.

        Returns:
            dict: A dictionary representation of the response.
        """
        return {
            "status": self.status,
            "message": self.message,
            "hasErrors": self.hasErrors,
            "results": [result.__dict__ for result in self.results],
            "context": [context.__dict__ for context in self.context]
        }
