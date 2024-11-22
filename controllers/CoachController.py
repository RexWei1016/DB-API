from models.CoachModel import CoachModel
from datetime import date
class CoachController:
    @staticmethod
    def register_coach(cID, password, name, onboarding, exp):
        # 檢查所有必填欄位的完整性
        required_fields = [cID, password, name, onboarding, exp]
        if not all(required_fields):
            return {"error": "所有欄位皆為必填，請確認已填寫完整"}, 400

        # 檢查教練帳號是否存在
        if CoachModel.get_coach_by_id(cID):
            return {"error": "教練帳號已存在!"}, 409

        # 新增教練資料
        try:
            CoachModel.create_coach({
                'cID': cID,
                'pwd': password,
                'name': name,
                'onboarding': onboarding,
                'exp': exp
            })
            return {"message": "教練註冊成功"}, 201
        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def login_coach(cID, password):
        # 查詢教練的帳號與密碼
        data = CoachModel.get_coach_by_id(cID)
        if data and data[0][1] == password:
            return {"message": f"登入成功，歡迎 {data[0][2]}"}, 200
        return {"error": "*密碼錯誤，請再試一次"}, 401


    @staticmethod
    def get_all_coaches():
        try:
            # 查詢所有教練資料
            coaches = CoachModel.get_all_coaches()
            if not coaches:
                return {"message": "目前沒有教練資料"}, 200
            
            # 整理資料格式
            coach_list = []
            for coach in coaches:
                coach_list.append({
                    'cID': coach[0],
                    'name': coach[2],
                    'onboarding': coach[3].isoformat() if isinstance(coach[3], date) else coach[3],
                    'exp': coach[4]
                })

            return {"coaches": coach_list}, 200
        except Exception as e:
            return {"error": str(e)}, 500
