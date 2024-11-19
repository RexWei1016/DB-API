from flask import Blueprint
from flask_restx import Api, Resource, fields, Namespace
from controllers.food_record_controller import FoodRecordController
from utils.validation import validate_json

food_record_blueprint = Blueprint('food_record', __name__)
food_record_api = Namespace('飲食紀錄API', description='紀錄專用API')

food_record_model = food_record_api.model('FoodRecord', {
    'eat_date': fields.String(required=True, description='Eating date (YYYY-MM-DD)'),
    'id': fields.String(required=True, description='User ID'),
    'fid': fields.Integer(required=True, description='Food ID'),
    'food_num': fields.Integer(description='Number of food items'),
    'calories': fields.Float(description='Calories (kcal)')
})

@food_record_api.route('/')
class FoodRecord(Resource):
    @food_record_api.expect(food_record_model)
    def post(self):
        data = validate_json()
        response, status = FoodRecordController.create_record(data)
        return response, status

@food_record_api.route('/<string:user_id>')
class FoodRecordByUser(Resource):
    def get(self, user_id):
        response, status = FoodRecordController.get_records(user_id)
        return response, status

@food_record_api.route('/<string:user_id>/<string:eat_date>/<int:fid>')
class DeleteFoodRecord(Resource):
    def delete(self, user_id, eat_date, fid):
        response, status = FoodRecordController.delete_record(user_id, eat_date, fid)
        return response, status
