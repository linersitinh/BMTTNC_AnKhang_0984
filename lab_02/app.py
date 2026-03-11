from flask import Flask, request, jsonify, render_template

from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence.railfence_cipher import encrypt as rail_encrypt, decrypt as rail_decrypt
from cipher.playfair.playfair_cipher import encrypt as playfair_encrypt, decrypt as playfair_decrypt
from cipher.transposition.transposition_cipher import encrypt as trans_encrypt, decrypt as trans_decrypt

app = Flask(__name__)

caesar = CaesarCipher()
vigenere = VigenereCipher()

########################################
# WEB INTERFACE
########################################

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        cipher = request.form["cipher"]
        text = request.form["text"]
        key = request.form["key"]
        action = request.form["action"]

        if cipher == "caesar":

            if action == "encrypt":
                result = caesar.encrypt_text(text, int(key))
            else:
                result = caesar.decrypt_text(text, int(key))

        elif cipher == "vigenere":

            if action == "encrypt":
                result = vigenere.vigenere_encrypt(text, key)
            else:
                result = vigenere.vigenere_decrypt(text, key)

        elif cipher == "railfence":

            if action == "encrypt":
                result = rail_encrypt(text, int(key))
            else:
                result = rail_decrypt(text, int(key))

        elif cipher == "playfair":

            if action == "encrypt":
                result = playfair_encrypt(text, key)
            else:
                result = playfair_decrypt(text, key)

        elif cipher == "transposition":

            if action == "encrypt":
                result = trans_encrypt(text, int(key))
            else:
                result = trans_decrypt(text, int(key))

    return render_template("index.html", result=result)


########################################
# CAESAR API
########################################

@app.route("/api/caesar/encrypt", methods=["POST"])
def api_caesar_encrypt():

    data = request.json
    text = data["plain_text"]
    key = int(data["key"])

    result = caesar.encrypt_text(text, key)

    return jsonify({"result": result})


@app.route("/api/caesar/decrypt", methods=["POST"])
def api_caesar_decrypt():

    data = request.json
    text = data["cipher_text"]
    key = int(data["key"])

    result = caesar.decrypt_text(text, key)

    return jsonify({"result": result})


########################################
# VIGENERE API
########################################

@app.route("/api/vigenere/encrypt", methods=["POST"])
def api_vigenere_encrypt():

    data = request.json
    text = data["plain_text"]
    key = data["key"]

    result = vigenere.vigenere_encrypt(text, key)

    return jsonify({"result": result})


@app.route("/api/vigenere/decrypt", methods=["POST"])
def api_vigenere_decrypt():

    data = request.json
    text = data["cipher_text"]
    key = data["key"]

    result = vigenere.vigenere_decrypt(text, key)

    return jsonify({"result": result})


########################################
# RAILFENCE API
########################################

@app.route('/api/railfence/encrypt', methods=['POST'])
def api_rail_encrypt():
    data = request.json
    text = data["plain_text"]
    key = int(data["key"])

    encrypted = railfence_encrypt(text, key)

    return jsonify({"encrypted_text": encrypted})

@app.route('/api/railfence/decrypt', methods=['POST'])
def api_rail_decrypt():
    data = request.json
    text = data["cipher_text"]
    key = int(data["key"])

    decrypted = railfence_decrypt(text, key)

    return jsonify({"decrypted_text": decrypted})


########################################
# PLAYFAIR API
########################################

@app.route("/api/playfair/encrypt", methods=["POST"])
def api_playfair_encrypt():

    data = request.json
    text = data["text"]
    key = data["key"]

    result = playfair_encrypt(text, key)

    return jsonify({"result": result})


@app.route("/api/playfair/decrypt", methods=["POST"])
def api_playfair_decrypt():

    data = request.json
    text = data["text"]
    key = data["key"]

    result = playfair_decrypt(text, key)

    return jsonify({"result": result})


########################################
# TRANSPOSITION API
########################################

@app.route("/api/transposition/encrypt", methods=["POST"])
def api_trans_encrypt():

    data = request.json
    text = data["text"]
    key = int(data["key"])

    result = trans_encrypt(text, key)

    return jsonify({"result": result})


@app.route("/api/transposition/decrypt", methods=["POST"])
def api_trans_decrypt():

    data = request.json
    text = data["text"]
    key = int(data["key"])

    result = trans_decrypt(text, key)

    return jsonify({"result": result})


########################################

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)