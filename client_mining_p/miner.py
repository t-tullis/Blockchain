import hashlib
import requests

import sys


# TODO: Implement functionality to search for a proof 

def proof_of_work(last_proof):
    proof = 0
    while validate_proof(last_proof, proof) is False:
        proof += 1

    return proof


def validate_proof(last_proof, proof):
    guess = f"{last_proof}{proof}".encode()
    guess_hash = hashlib.sha256(proof_guess).hexdigest()
    return guess_hash[:6] == "000000"


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    coins_mined = 0
    # Run forever until interrupted
    while True:
        # TODO: Get the last proof from the server and look for a new one
        r = requests.get(url = node + '/last_proof')
        data = r.json()
        last_proof = data['last_proof']
        
        new_proof = proof_of_work(last_proof)
        
        proof_data = {'proof': new_proof}
        
        r = requests.post(url = node + '/mine', json= proof_data)
        if r.json()['message'] == 'New Block Forged':
            coins_mined += 1
            print(f"Coins mined: {coins_mined}")
        # TODO: When found, POST it to the server {"proof": new_proof}

        # TODO: If the server responds with 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.
        pass
