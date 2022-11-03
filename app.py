# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/cs440'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# CORS(app)  

# class status(db.Model):
#     __tablename__ = 'ransomware'

#     id = db.Column(db.Integer, primary_key=True)
#     status = db.Column(db.Integer)

#     def __init__(self, id, status):
#         self.id = id
#         self.status = status

#     def json(self):
#         return {"id": self.id, "status": self.status}



# @app.route("/getstatus")
# def getstatus(id):
#     status = status.query.filter_by(id=id).first()
#     if status:
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": status.json()
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "message": "No status found"
#         }
#     ), 404


# @app.route("/changestatus/<int:id>", methods=['POST'])
# def create_book(isbn13):
#     if (status.query.filter_by(id=id).first()):
#         return jsonify(
#             {
#                 "code": 400,
#                 "data": {
#                     "id": id
#                 },
#                 "message": "status already exist"
#             }
#         ), 400

#     data = request.get_json()
#     status = status(id, **data)

#     try:
#         db.session.add(status)
#         db.session.commit()
#     except:
#         return jsonify(
#             {
#                 "code": 500,
#                 "data": {
#                     "id": id
#                 },
#                 "message": "An error occurred status."
#             }
#         ), 500

#     return jsonify(
#         {
#             "code": 201,
#             "data": status.json()
#         }
#     ), 201



# if __name__ == '__main__':
#     app.run(port=5000, debug=True)


from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world!'
