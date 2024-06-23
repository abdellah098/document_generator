import uuid
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

fake_patients_table = {
  uuid.UUID('33a976a7-3e24-4bf0-af51-371aa794d3b4') : {'first_name': 'John', 'last_name': 'Doe', 'age': 45},
  uuid.UUID('3c00811f-44a3-466b-8a70-bc5d8e68531c') : {'first_name': 'Jane', 'last_name': 'Smith',  'age': 30},
  uuid.UUID('b1fa1bfd-6ac4-4254-acae-825e15efe81b') : {'first_name': 'Emily', 'last_name': 'Johnson', 'age': 27},
}

class PatientList(Resource):
  def get(self):
    return {str(key): fake_patients_table[key] for key in fake_patients_table}
  
  def post(self):
    data = request.json
    id = uuid.uuid4()
    fake_patients_table[id] = data

    return {str(id): data}, 201

class Patient(Resource):
  def get(self, patient_id):
    return {patient_id : fake_patients_table.get(uuid.UUID(patient_id))}, 200

  def delete(self, patient_id):
    del fake_patients_table[uuid.UUID(patient_id)]
    return '', 204
  
  def put(self, patient_id):
    data = request.json
    fake_patients_table[uuid.UUID(patient_id)] = data
    return {patient_id: data}, 201


api.add_resource(PatientList,
    '/patients/',
    '/patients')

api.add_resource(Patient,
    '/patients/<string:patient_id>')

if __name__ == '__main__':
  app.run(port=8000, debug=True)