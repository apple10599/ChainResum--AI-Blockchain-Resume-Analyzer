from web3 import Web3
import json

def send_to_blockchain(score, reviewer, feedback):
    with open("blockchain/contract_config.json") as f:
        config = json.load(f)

    contract_address = Web3.to_checksum_address(config["address"])
    abi = config["abi"]

    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))  # Ganache or Remix VM via HTTP
    contract = w3.eth.contract(address=contract_address, abi=abi)

    sender = w3.eth.accounts[0]
    feedback = ", ".join(feedback)
    tx = contract.functions.setEvaluation(score, reviewer, feedback).build_transaction({
        "from": sender,
        "gas": 300000,
        "nonce": w3.eth.get_transaction_count(sender),
    })

    signed = w3.eth.account.sign_transaction(tx, private_key="your_private_key_here")
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    w3.eth.wait_for_transaction_receipt(tx_hash)

    return tx_hash.hex()
