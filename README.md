# Ethereum Sender

The Ethereum Sender project allows you to automatically send ETH from one wallet to another. By providing a private key for your ETH wallet and a recipient's public key, the script will monitor the wallet for incoming ETH and automatically initiate transfers to the specified recipient.

## Features

- Automatic ETH transfer from one wallet to another.
- Real-time monitoring of the wallet balance.
- Configurable transaction threshold for initiating transfers.
- private key management.

## Requirements

- Ethereum wallet with a private key.
- Python 3.x installed on your system.
- Web3.py library for Ethereum interaction.

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using the following command:
 `pip install -r requirements.txt`
3. Open the `config.py` file and update the following information:
- `private_key`: Your Ethereum wallet private key.
- `recipient_address`: The public key of the recipient's Ethereum wallet.
- `threshold_amount`: The minimum ETH balance required to initiate a transfer.

## Usage

1. Make sure you have configured the `config.py` file with the correct information.
2. Run the script using the following command: python eth_sender.py
3. The script will start monitoring the specified wallet for incoming ETH.
4. When the wallet balance reaches the configured threshold amount, the script will initiate a transfer to the recipient's wallet automatically.
5. The script will continue to monitor the wallet balance and initiate transfers as necessary.

## Contribution

Contributions to this project are highly appreciated. You can contribute by submitting pull requests or by reporting issues and suggestions for improvement. You can also ask your questions in the Issues section.

## License

This project is licensed under the [MIT License](LICENSE). For more information about the license, please refer to the `LICENSE` file.

## Contact

- For more information, you can visit [my website](http://sobhan.hashnode.dev).
- For questions and suggestions, you can contact me via email: xd3vman@gmail.com
