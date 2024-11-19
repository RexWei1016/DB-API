from models.user_model import AppUserModel

class UserController:
    @staticmethod
    def register_user(account, username, password, birth, sex, cname, use, number, phones):
        # 檢查所有必填欄位的完整性
        required_fields = [account, username, password, birth, sex, cname, use, number]
        if not all(required_fields):
            return {"error": "所有欄位皆為必填，請確認已填寫完整"}, 400

        # 檢查帳號是否存在
        if AppUserModel.is_account_existing(account):
            return {"error": "帳號已存在!"}, 409

        # 新增會員資料
        try:
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

            # 新增電話資料
            if phones:
                AppUserModel.add_user_phones(account, phones)

            return {"message": "Registration successful"}, 201
        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def login_user(account, password):
        # 查詢帳號和密碼
        data = AppUserModel.get_user_by_id(account)
        if data and data[0][1] == password:
            return {"message": "Login successful"}, 200
        return {"error": "*密碼錯誤，請再試一次"}, 401
