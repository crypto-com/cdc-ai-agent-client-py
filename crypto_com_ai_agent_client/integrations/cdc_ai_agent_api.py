import requests
from .cdc_ai_agent_interface import CryptoComAiAgentResponse


def generate_query(query: str, options: dict) -> CryptoComAiAgentResponse:
    """
    Sends a query to the CDC AI Agent service and returns the AI-generated response.

    Args:
        query (str): The query string to send to the CDC AI Agent service.
        options (dict): A dictionary containing configuration options like OpenAI API key, 
                        chain details, and explorer information.

    Returns:
        CryptoComAiAgentResponse: A response object that contains the AI-generated message and related data.

    Raises:
        Exception: If the response status code is not successful (not in [200, 201, 202]),
                   or if there's an issue sending the request or parsing the response.

    Example:
        >>> config = {'openAI': {'apiKey': 'YOUR_OPEN_AI_API_KEY'}, 
                      'chain': {'id': 'CHAIN_ID, 'name': 'CHAIN_NAME', 'rpc': 'CHAIN_RPC_URL'}, 
                      'explorer': {'apiKey': 'EXPLORER_API_KEY'}}
        >>> query = "What is the latest block?"
        >>> response = generate_query(query, config)
        >>> print(response.result)
    """
    url = 'https://ai-agent-api.crypto.com/api/v1/cdc-ai-agent-service/query'
    payload = {'query': query, 'options': options}

    try:
        response = requests.post(url, json=payload)

        if response.status_code not in [200, 201, 202]:
            raise Exception(f"HTTP error! Status: {response.status_code}")

        data = response.json()
        return CryptoComAiAgentResponse(**data)

    except Exception as e:
        print(f"[CryptoComAiAgent/generate_query] - {str(e)}")
        raise Exception(f"Failed to generate response: {str(e)}")
