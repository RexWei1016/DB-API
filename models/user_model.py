from db.database import fetch_data, modify_data

class AppUserModel:
    @staticmethod
    def get_user_by_id(user_id):
        query = "SELECT ID, pwd FROM AppUser WHERE ID = %s"
        return fetch_data(query, (user_id,))

    @staticmethod
    def is_account_existing(account):
        query = "SELECT 1 FROM AppUser WHERE ID = %s"
        result = fetch_data(query, (account,))
        return bool(result)  # 如果有結果，表示帳號存在

    @staticmethod
    def create_user(data):
        query = '''
            INSERT INTO AppUser (ID, pwd, birth, Sex, name, cname, use, number)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        params = (data['ID'], data['pwd'], data['birth'], data['Sex'], 
                  data['name'], data['cname'], data['use'], data['number'])
        modify_data(query, params)

    @staticmethod
    def add_user_phones(user_id, phones):
        query = '''
            INSERT INTO UserPhone (id, phone, phone_type)
            VALUES (%s, %s, %s)
        '''
        for phone in phones:
            params = (user_id, phone['phone'], phone['phone_type'])
            modify_data(query, params)


    @staticmethod
    def get_all_users():
        query = "SELECT ID, name FROM AppUser"
        return fetch_data(query)