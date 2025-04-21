from flask import Flask, render_template, request
import os
from ai_model.parser import parse_resume
from web3 import Web3
from blockchain.contract_info import abi, contract_address

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# Load Smart Contract
contract = w3.eth.contract(address=contract_address, abi=abi)

@app.route("/", methods=["GET", "POST"])
def index():
    print("Received request:", request.method)
    if request.method == "POST":
        try:
            resume = request.files["resume"]
            path = os.path.join(UPLOAD_FOLDER, resume.filename)
            resume.save(path)
            print("Resume saved at:", path)

            # Parse resume
            result = parse_resume(path)
            print("Parse result:", result)

            score, feedback_list = result
            reviewer = "AI Resume Bot"
            feedback = "; ".join(feedback_list)

            address = w3.eth.accounts[0]
            tx_hash = contract.functions.setEvaluation(score, reviewer, feedback).transact({'from': address})
            w3.eth.wait_for_transaction_receipt(tx_hash)

            return render_template("index.html", score=score, feedback=feedback, feedback_list=feedback_list)
        except Exception as e:
            print("Error occurred:", e)

    return render_template("index.html", success=False)

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)
