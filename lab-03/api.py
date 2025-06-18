from flask import Flask, request, jsonify
from cipher.rsa import RSACipher
from cipher.ecc import ECCCipher

app = Flask(__name__)

# RSA CIPHER ALGORITHM
rsa_cipher = RSACipher()

@app.route('/api/rsa/generate_keys', methods=['GET'])
def rsa_generate_keys():
    rsa_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route("/api/rsa/encrypt", methods=["POST"])
def rsa_encrypt():
    data = request.json
    message = data['message']
    key_type = data['key_type']
    private_key, public_key = rsa_cipher.load_keys()
    if key_type == 'public':
        key = public_key
    elif key_type == 'private':
        key = private_key
    else:
        return jsonify({'error': 'Invalid key type'}), 400
    encrypted_message = rsa_cipher.encrypt(message, key)
    encrypted_hex = encrypted_message.hex()
    return jsonify({'encrypted_message': encrypted_hex})

@app.route("/api/rsa/decrypt", methods=["POST"])
def rsa_decrypt():
    data = request.json
    ciphertext_hex = data['ciphertext']
    key_type = data['key_type']
    private_key, public_key = rsa_cipher.load_keys()
    if key_type == 'public':
        key = public_key
    elif key_type == 'private':
        key = private_key
    else:
        return jsonify({'error': 'Invalid key type'}), 400
    ciphertext = bytes.fromhex(ciphertext_hex)
    decrypted_message = rsa_cipher.decrypt(ciphertext, key)
    return jsonify({'decrypted_message': decrypted_message})

# Caesar CIPHER ALGORITHM (Add Caesar Cipher logic here)
@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_message = caesar_cipher_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_message})

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_message = caesar_cipher_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_message})

def caesar_cipher_encrypt(plain_text, key):
    # Caesar Cipher encryption logic
    result = ""
    for char in plain_text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) + key - shift) % 26 + shift)
        else:
            result += char
    return result

def caesar_cipher_decrypt(cipher_text, key):
    # Caesar Cipher decryption logic
    result = ""
    for char in cipher_text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - key - shift) % 26 + shift)
        else:
            result += char
    return result

# ECC CIPHER ALGORITHM
ecc_cipher = ECCCipher()

@app.route('/api/ecc/generate_keys', methods=['GET'])
def ecc_generate_keys():
    ecc_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route('/api/ecc/sign', methods=['POST'])
def ecc_sign_message():
    data = request.json
    message = data['message']
    private_key, _ = ecc_cipher.load_keys()
    signature = ecc_cipher.sign(message, private_key)
    signature_hex = signature.hex()
    return jsonify({'signature': signature_hex})

@app.route('/api/ecc/verify', methods=['POST'])
def ecc_verify_signature():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    public_key, _ = ecc_cipher.load_keys()
    signature = bytes.fromhex(signature_hex)
    is_verified = ecc_cipher.verify(message, signature, public_key)
    return jsonify({'is_verified': is_verified})

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)