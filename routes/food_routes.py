from flask import Blueprint
from flask_restx import Api, Resource, fields, Namespace
from controllers.FoodController import FoodController
from utils.validation import validate_json

# 創建 Blueprint 和 Namespace
food_blueprint = Blueprint('food', __name__)
food_api = Namespace('食物管理API', description='管理食物資料的API')

# 定義數據模型
food_model = food_api.model('Food', {
    'food_type': fields.String(required=True, description='Food type (e.g., Rice, Chicken)'),
    'food_calories': fields.Float(required=True, description='Calories per 100g (kcal)')
})

@food_api.route('/')
class Food(Resource):
    @food_api.expect(food_model)
    def post(self):
        """
        新增食物
        """
        data = validate_json()
        response, status = FoodController.create_food(data)
        return response, status

    def get(self):
        """
        查詢所有食物
        """

        response, status = FoodController.get_all_foods()
        print(response)
        return response, status

@food_api.route('/<int:fid>')
class FoodByID(Resource):
    def delete(self, fid):
        """
        刪除指定食物
        """
        response, status = FoodController.delete_food(fid)
        return response, status
