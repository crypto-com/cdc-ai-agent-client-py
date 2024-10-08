import json
from typing import Any, Dict

import requests

from .cdc_ai_agent_interface import CryptoComAiAgentResponse


def generate_query(query: str, options: Dict[str, Any]) -> CryptoComAiAgentResponse:
    """
    Sends a query to the CDC AI Agent service and returns the AI-generated response.

    Args:
        query (str): The query string to send to the CDC AI Agent service.
        options (Dict[str, Any]): A dictionary containing configuration options including OpenAI details,
                                  chain ID, explorer keys, context, signer app URL, and custom RPC.

    Returns:
        CryptoComAiAgentResponse: A response object that contains the AI-generated message and related data.

    Raises:
        Exception: If the response status code is not successful (not in [200, 201, 202]),
                   or if there's an issue sending the request or parsing the response.

    Example:
        >>> options = {
        >>>     'openAI': {'apiKey': 'YOUR_OPEN_AI_API_KEY', 'model': 'gpt-4-turbo'},
        >>>     'chainId': 25,
        >>>     'explorerKeys': {
        >>>         'cronosTestnetKey': 'CRONOS_TESTNET_API_KEY',
        >>>         'cronosZkEvmKey': 'CRONOS_ZKEVM_API_KEY',
        >>>         'cronosZkEvmTestnetKey': 'CRONOS_ZKEVM_TESTNET_API_KEY'
        >>>     },
        >>>     'context': [],
        >>>     'signerAppUrl': 'https://my-signer-app',
        >>>     'customRPC': 'https://rpc.vvs.finance'
        >>> }
        >>> query = "What is the latest block?"
        >>> response = generate_query(query, options)
        >>> print(response.result)
    """
    url = 'https://ai-agent-api.crypto.com/api/v1/cdc-ai-agent-service/query'
    payload = {'query': query, 'options': options}

    try:
        response = requests.post(url, json=payload)
        if response.status_code not in [200, 201, 202]:
            raise Exception(f"""Error with status code: {
                            response.status_code}, message: {json.dumps(response.json(), indent=2)}""")

        data = response.json()
        return CryptoComAiAgentResponse(**data)

    except Exception as e:
        raise Exception(f"Failed to generate response: {str(e)}")
