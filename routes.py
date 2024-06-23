from models import Patient
from flask_restful import Resource, Api, request

def register_routes(app, db) :
  api = Api(app)

  api.add_resource(PatientList,
    '/patients/',
    '/patients')

  api.add_resource(Patient,
    '/patients/<string:patient_id>')

class PatientList(Resource):
  def get(self):
    return "return get all request", 200
  
  def post(self):
    return "return post request", 201

class Patient(Resource):
  def get(self, patient_id):
    return "get request", 200

  def delete(self, patient_id):
    return "delete request", 204
  
  def put(self, patient_id):
    return "put request", 201
