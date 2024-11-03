from models.user_model import AppUserModel

class UserController:
    @staticmethod
    def register_user(account, username, password, birth, sex, cname, use, number):
        # 檢查所有必填欄位的完整性
        if not all([account, username, password, birth, sex, cname, use, number]):
            return {"error": "所有欄位皆為必填，請確認已填寫完整"}, 400

        # 檢查帳號是否存在
        if AppUserModel.is_account_existing(account):
            return {"error": "帳號已存在!"}, 409
        
        # 新增會員資料
        AppUserModel.create_user({
            'ID': account,
            'pwd': password,
            'birth': birth,
            'Sex': sex,
            'name': username,
            'cname': cname,
            'use': use,
            'number': number
        })
        return {"message": "Registration successful"}, 201

    @staticmethod
    def login_user(account, password):
        # 查詢帳號和密碼
        data = AppUserModel.get_user_by_id(account)
        if data and data[0][1] == password:
            return {"message": "Login successful"}, 200
        return {"error": "*密碼錯誤，請再試一次"}, 401
