from .integrations.cdc_ai_agent_api import generate_query
from .integrations.cdc_ai_agent_interface import CryptoComAiAgentResponse


class CryptoComAiAgentClient:
    """
    A client for interacting with the CDC AI Agent service.

    This client manages configuration and provides methods to send queries to the CDC AI Agent service.
    
    Attributes:
        config (dict): The configuration for the client, including OpenAI API key, blockchain details, and explorer API key.
        agent (Agent): An inner class providing the method to send queries to the AI agent.
    """

    def __init__(self, config):
        """
        Initialize the CDC AI Agent Client with the given configuration.

        Args:
            config (dict): Configuration for the client, such as OpenAI API key, chain info, and explorer API key.
        """
        self.config = config
        self.agent = self.Agent(self.config)  # Add the agent property

    class Agent:
        """
        An inner class representing the agent that communicates with the CDC AI Agent service.

        Attributes:
            config (dict): The configuration passed from the parent client.
        """

        def __init__(self, config):
            """
            Initialize the Agent with the given configuration.

            Args:
                config (dict): Configuration for the agent, inherited from the parent client.
            """
            self.config = config

        def generate_query(self, query: str) -> CryptoComAiAgentResponse:
            """
            Sends a query to the CDC AI Agent service and returns the AI-generated response.

            Args:
                query (str): The query string to send to the CDC AI Agent service (e.g., questions or commands related to blockchain).

            Returns:
                CryptoComAiAgentResponse: A response object containing the AI-generated message and related data.

            Raises:
                Exception: If an error occurs while generating the query.
            """
            return generate_query(query, self.config)


def create_client(config: dict) -> CryptoComAiAgentClient:
    """
    Creates a new client for interacting with the CDC AI Agent Service.

    Args:
        config (dict): Configuration for the client, including OpenAI API key, blockchain details, explorer API key.

    Returns:
        CryptoComAiAgentClient: A new instance of the CDC AI Agent Client.

    Example:
        >>> config = {
        >>>     'openAI': {'apiKey': 'YOUR_OPEN_AI_API_KEY'},
        >>>     'chain': {'id': 282, 'name': 'Cronos Testnet', 'rpc': 'CHAIN_RPC_URL'},
        >>>     'explorer': {'apiKey': 'EXPLORER_API_KEY'}
        >>> }
        >>> client = create_client(config)
        >>> response = client.agent.generate_query('What is the latest block?')
        >>> print(response.result)
    """
    return CryptoComAiAgentClient(config)
