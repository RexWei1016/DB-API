from db.database import fetch_data, modify_data

class AppUserModel:
    @staticmethod
    def get_user_by_id(user_id):
        query = "SELECT ID, pwd FROM AppUser WHERE ID = %s"
        return fetch_data(query, (user_id,))

    @staticmethod
    def is_account_existing(account):
        query = "SELECT ID FROM AppUser WHERE ID = %s"
        return fetch_data(query, (account,))

    @staticmethod
    def create_user(data):
        query = '''
            INSERT INTO AppUser (ID, pwd, birth, Sex, name, cname, use, number)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        params = (data['ID'], data['pwd'], data['birth'], data['Sex'], 
                  data['name'], data['cname'], data['use'], data['number'])
        modify_data(query, params)
