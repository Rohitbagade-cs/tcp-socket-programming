# TCP Socket Programming with Encryption

A Python implementation of TCP client-server communication with custom encryption.

## Features

- TCP client-server architecture
- Custom encryption/decryption for secure communication
- Simple message exchange protocol

## Files

- `client.py` - TCP client implementation
- `server.py` - TCP server implementation  
- `crypto_utils.py` - Encryption/decryption utilities

## Usage

1. Start the server:
   ```bash
   python server.py
   ```

2. Run the client:
   ```bash
   python client.py
   ```

3. Enter a message when prompted (e.g., "SetA-Two")

## Requirements

- Python 3.x
- Standard library modules only

## How it works

1. Client connects to server on localhost:5555
2. Client encrypts and sends a message
3. Server receives, processes, and responds
4. All communication is encrypted using custom crypto utilities
