from flask import Flask, request, session, jsonify

app = Flask(__name__)
app.secret_key = "dev-secret"

USERS = {"piotr": "1234"}

@app.route("/login", methods=["POST"])
def login():
    data = request.json

    if USERS.get(data["username"]) == data["password"]:
        session["user"] = data["username"]
        return jsonify({"msg": "OK"}), 200

    return jsonify({"msg": "fail"}), 401


@app.route("/me")
def me():
    if "user" not in session:
        return jsonify({"msg": "no access"}), 403

    return jsonify({"user": session["user"]})


@app.route("/logout")
def logout():
    session.clear()
    return jsonify({"msg": "logged out"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)