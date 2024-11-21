from models.food_record_model import FoodRecordModel

class FoodRecordController:
    @staticmethod
    def create_record(data):
        # 檢查必填欄位
        required_fields = ['eat_date', 'id', 'fid']
        missing_fields = [field for field in required_fields if field not in data or not data[field]]
        if missing_fields:
            return {"error": f"缺少必要欄位: {', '.join(missing_fields)}"}, 400

        try:
            # 嘗試新增紀錄
            FoodRecordModel.create_record(data)
            return {"message": "紀錄新增成功"}, 201
        except Exception as e:
            return {"error": f"新增紀錄失敗: {str(e)}"}, 500

    @staticmethod
    def get_records(user_id):
        try:
            # 嘗試查詢紀錄
            records = FoodRecordModel.get_records_by_user(user_id)
            if not records:
                return {"message": "無紀錄"}, 404
            return {"data": records}, 200
        except Exception as e:
            return {"error": f"查詢失敗: {str(e)}"}, 500

    @staticmethod
    def delete_record(user_id, eat_date, fID):
        try:
            # 嘗試刪除紀錄
            FoodRecordModel.delete_record(user_id, eat_date, fID)
            return {"message": "紀錄刪除成功"}, 200
        except Exception as e:
            return {"error": f"刪除失敗: {str(e)}"}, 500
