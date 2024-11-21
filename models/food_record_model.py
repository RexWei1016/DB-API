from db.database import fetch_data, modify_data

class FoodRecordModel:
    @staticmethod
    def create_record(data):
        query = '''
            INSERT INTO FoodRecord (eat_date, id, fid, food_num, calories)
            VALUES (%s, %s, %s, %s, %s)
        '''
        params = (
            data['eat_date'],
            data['id'],
            data['fid'],
            data.get('food_num', 0),  # 預設為 0
            data.get('calories', 0.0)  # 預設為 0.0
        )
        modify_data(query, params)

    @staticmethod
    def get_records_by_user(user_id):
        query = '''
            SELECT eat_date, fid, food_num, calories 
            FROM FoodRecord 
            WHERE id = %s 
            ORDER BY eat_date DESC
        '''
        return fetch_data(query, (user_id,))

    @staticmethod
    def delete_record(user_id, eat_date, fID):
        query = '''
            DELETE FROM FoodRecord 
            WHERE id = %s AND eat_date = %s AND id = %s
        '''
        modify_data(query, (user_id, eat_date, fID))
