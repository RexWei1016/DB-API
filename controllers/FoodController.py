from models.FoodModel import FoodModel
from decimal import Decimal

class FoodController:
    @staticmethod
    def create_food(data):
        # 檢查必填欄位
        required_fields = ['food_type', 'food_calories']
        missing_fields = [field for field in required_fields if field not in data or not data[field]]
        if missing_fields:
            return {"error": f"缺少必要欄位: {', '.join(missing_fields)}"}, 400

        try:
            # 嘗試新增食物
            FoodModel.create_food(data)
            return {"message": "食物新增成功"}, 201
        except Exception as e:
            return {"error": f"新增食物失敗: {str(e)}"}, 500

    @staticmethod
    def get_all_foods():
        try:
            # 嘗試查詢所有食物
            foods = FoodModel.get_all_foods()
            if not foods:
                return {"message": "無食物記錄"}, 404

            # 將資料從元組轉換為字典，並將 Decimal 轉換為 float
            formatted_foods = [
                {"fid": food[0], "food_type": food[1], "food_calories": float(food[2])}
                for food in foods
            ]

            print(formatted_foods)  # 用於檢查處理後的資料
            return {"data": formatted_foods}, 200
        except Exception as e:
            # 返回詳細錯誤資訊
            return {"error": f"查詢失敗: {str(e)}"}, 500


    @staticmethod
    def delete_food(fid):
        try:
            # 嘗試刪除食物
            FoodModel.delete_food(fid)
            return {"message": "食物刪除成功"}, 200
        except Exception as e:
            return {"error": f"刪除失敗: {str(e)}"}, 500
