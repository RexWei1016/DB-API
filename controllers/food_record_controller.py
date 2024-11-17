from models.food_record_model import FoodRecordModel

class FoodRecordController:
    @staticmethod
    def create_record(data):
        # 檢查必填欄位
        required_fields = ['eat_date', 'ID', 'fID']
        if not all(field in data and data[field] for field in required_fields):
            return {"error": "eat_date、ID 和 fID 為必填欄位"}, 400

        # 建立新紀錄
        try:
            FoodRecordModel.create_record(data)
            return {"message": "紀錄新增成功"}, 201
        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def get_records(user_id):
        try:
            records = FoodRecordModel.get_records_by_user(user_id)
            return {"data": records}, 200
        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def delete_record(user_id, eat_date, fID):
        try:
            FoodRecordModel.delete_record(user_id, eat_date, fID)
            return {"message": "紀錄刪除成功"}, 200
        except Exception as e:
            return {"error": str(e)}, 500
