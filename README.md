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
        'apiKey': 'YOUR_OPEN_AI_API_KEY'
    },
    'chain': {
        'id': 'CHAIN_ID', # e.g. 240 for the Cronos ZkEVM Testnet
        'name': 'CHAIN_NAME',
        'rpc': 'CHAIN_RPC_URL',
    },
    'explorer': {
        'apiKey': 'EXPLORER_API_KEY',
    }
})
```

### Sending a Query

```py
def send_query(query):
    try:
        response = client.agent.generate_query(query)
        print('Crypto.com AI Agent Response:', response)
    except Exception as e:
        print(f"Error sending query: {str(e)}")

send_query("What is the latest block?")
```

## API

### Client Methods

- `generate_query(query)`: Generates a query that is send to the Crypto.com AI Agent Service and returns a response.

## Licensing

The code in this project is licensed under the MIT license.

## Contact

If you have any questions or comments about the library, please feel free to open an issue or a pull request on our GitHub repository.
