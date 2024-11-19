from flask import Blueprint
from flask_restx import Api, Resource, fields, Namespace
from controllers.exercise_record_controller import ExerciseRecordController
from utils.validation import validate_json

# 創建 Blueprint 和 Namespace
exercise_record_blueprint = Blueprint('exercise_record', __name__)
exercise_record_api = Namespace('運動紀錄', description='運動紀錄API')

# 定義數據模型
exercise_record_model = exercise_record_api.model('ExerciseRecord', {
    'exe_date': fields.String(required=True, description='Exercise date (YYYY-MM-DD)'),
    'id': fields.String(required=True, description='User ID'),
    'exe_type': fields.String(description='Exercise type (e.g., Running, Swimming)'),
    'calories': fields.Float(description='Calories burned (kcal)')
})

@exercise_record_api.route('/')
class ExerciseRecord(Resource):
    @exercise_record_api.expect(exercise_record_model)
    def post(self):
        data = validate_json()
        response, status = ExerciseRecordController.create_record(data)
        return response, status

@exercise_record_api.route('/<string:user_id>')
class ExerciseRecordByUser(Resource):
    def get(self, user_id):
        response, status = ExerciseRecordController.get_records(user_id)
        return response, status

@exercise_record_api.route('/<string:user_id>/<string:exe_date>')
class DeleteExerciseRecord(Resource):
    def delete(self, user_id, exe_date):
        response, status = ExerciseRecordController.delete_record(user_id, exe_date)
        return response, status
