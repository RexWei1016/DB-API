from models.food_record_model import FoodRecordModel
import datetime
import decimal
# 這是自定義的 JSON 轉換函數

def custom_json_serializer(obj):
    if isinstance(obj, datetime.date):
        return obj.isoformat()  # 將日期轉換為 'YYYY-MM-DD' 格式的字串
    if isinstance(obj, decimal.Decimal):
        return float(obj)  # 將 Decimal 轉換為 float
    # 這裡處理 int 類型，雖然通常不需要特別處理 int，但如果出現問題可以加以捕捉
    if isinstance(obj, int):
        return obj  # int 會自動被 JSON 序列化，不需要做特殊處理
    # 如果還有其他未處理的類型，可以在這裡加入處理邏輯
    raise TypeError(f"Type {type(obj)} not serializable")

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
            print(records)
            # 更新正確的欄位名稱，對應資料庫結構
            columns = ["eat_date", "fid", "food_num", "calories"]

            # 這裡進行資料的轉換，將日期和 Decimal 轉換為可序列化的格式
            records_serialized = [
                {columns[i]: custom_json_serializer(value) for i, value in enumerate(record)}
                for record in records
            ]
            return {"data": records_serialized}, 200
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
