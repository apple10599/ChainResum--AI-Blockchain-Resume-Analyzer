// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ResumeEvaluation {
    struct Evaluation {
        uint256 score;
        string reviewer;
        string feedback;
    }

    mapping(address => Evaluation) public evaluations;

    function setEvaluation(uint256 _score, string memory _reviewer, string memory _feedback) public {
        evaluations[msg.sender] = Evaluation(_score, _reviewer, _feedback);
    }

    function getEvaluation(address _addr) public view returns (uint256, string memory, string memory) {
        Evaluation memory eval = evaluations[_addr];
        return (eval.score, eval.reviewer, eval.feedback);
    }
}
