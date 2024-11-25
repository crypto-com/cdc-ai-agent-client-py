import json
from typing import Any, Dict, List, Optional

from crypto_com_ai_agent_client.client import create_client
from crypto_com_ai_agent_client.integrations.cdc_ai_agent_interface import (
    CryptoComAiAgentResponse,
)

client = create_client({
    'openAI': {
        'apiKey': 'YOUR_OPEN_AI_API_KEY',
        'model': 'gpt-4-turbo'
    },
    'chainId': 388,  # e.g., for the Cronos EVM main
    'explorerKeys': {
        'cronosZkEvmKey': 'YOUR_CRONOS_ZKEVM_API_KEY',
    },
})


def send_query(query: str) -> None:
    try:
        response: CryptoComAiAgentResponse = client.agent.generate_query(query)
        print('Crypto.com AI Agent Response:',
              json.dumps(response.to_dict(), indent=2))
    except Exception as e:
        print(f"Error sending query: {str(e)}")


send_query("Get the latest block number, and its corresponding transaction details")
