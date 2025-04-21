# Replace with actual ABI from Remix
abi = [
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_score",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_reviewer",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_feedback",
				"type": "string"
			}
		],
		"name": "setEvaluation",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "evaluations",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "score",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "reviewer",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "feedback",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_addr",
				"type": "address"
			}
		],
		"name": "getEvaluation",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

# Replace with deployed contract address from Remix
contract_address = "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4"
