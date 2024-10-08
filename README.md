# Crypto.com AI Agent Client.py

The Crypto.com AI Agent Client.py is a Python library designed to facilitate easy and efficient interactions with the Crypto.com AI Agent Service API. This client library provides methods to send queries and fetch responses from the Crypto.com AI Agent Service seamlessly.

![PyPI](https://img.shields.io/pypi/v/crypto-com-ai-agent-client)

## Features

- Simple and intuitive API for interacting with the Crypto.com AI Agent.
- Supports sending queries and receiving AI-generated responses.
- Configurable client instances tailored to your specific endpoint and security needs.
- **Currently in beta**: Expect frequent updates and potential changes in future releases.

## Installation

To install the package, run the following command:

```bash
pip install crypto_com_ai_agent_client
```

## Usage

Here’s how you can use the Crypto.com AI Agent Client in your project:

### Configuring the Client

```py
from crypto_com_ai_agent_client import create_client

client = create_client({
    'openAI': {
        'apiKey': 'YOUR_OPEN_AI_API_KEY',
        'model': 'gpt-4o'  # Optional, defaults to 'gpt-4-turbo'
    },
    'chainId': 25,  # e.g., for the Cronos EVM Mainnet
    'explorerKeys': {
        'cronosMainnetKey': 'CRONOS_MAINNET_API_KEY',
        'cronosTestnetKey': 'CRONOS_TESTNET_API_KEY',
        'cronosZkEvmKey': 'CRONOS_ZKEVM_API_KEY',
        'cronosZkEvmTestnetKey': 'CRONOS_ZKEVM_TESTNET_API_KEY'
    },
    'context': [],  # Optional
    'signerAppUrl': 'https://my-signer-app',  # Optional
    'customRPC': 'https://rpc.vvs.finance'  # Optional, if not provided, the default RPC for the chainId will be used
})
```

### Sending a Query

```py
import json

def send_query(query):
    try:
        response = client.agent.generate_query(query)
        print('Crypto.com AI Agent Response:', json.dumps(response.to_dict(), indent=2))
    except Exception as e:
        print(f"Error sending query: {str(e)}")

send_query("What is the latest block?")
```

## API

### Client Methods

- `generate_query(query)`: Generates a query that is sent to the Crypto.com AI Agent Service and returns a response.

### Configuration Options

- `openAI`: Dictionary containing OpenAI configuration
  - `apiKey`: Your OpenAI API key
  - `model`: (Optional) The model to use (defaults to 'gpt-4-turbo')
- `chainId`: The ID of the blockchain network (25 for Cronos EVM Mainnet, 338 for Cronos EVM Testnet, 388 for Cronos ZkEVM Mainnet, 282 for Cronos ZkEVM Testnet)
- `explorerKeys`: Dictionary of API keys for different explorers, ensure that the keys match the chainId
  - `cronosMainnetKey`: (Optional) API key for Cronos Mainnet
  - `cronosTestnetKey`: (Optional) API key for Cronos Testnet
  - `cronosZkEvmKey`: (Optional) API key for Cronos ZkEVM
  - `cronosZkEvmTestnetKey`: (Optional) API key for Cronos ZkEVM Testnet
- `signerAppUrl`: (Optional) URL for the signer app
- `context`: (Optional) List of context items for the query
- `customRPC`: (Optional) Custom RPC URL, if not provided, the default RPC for the chainId will be used

## Licensing

The code in this project is licensed under the MIT license.

## Contact

If you have any questions or comments about the library, please feel free to open an issue or a pull request on our GitHub repository.
