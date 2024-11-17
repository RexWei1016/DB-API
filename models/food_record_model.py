from db.database import fetch_data, modify_data

class FoodRecordModel:
    @staticmethod
    def create_record(data):
        query = '''
            INSERT INTO FoodRecord (eat_date, ID, fID, food_num, calories)
            VALUES (%s, %s, %s, %s, %s)
        '''
        params = (
            data['eat_date'], data['ID'], data['fID'],
            data.get('food_num'), data.get('calories')
        )
        modify_data(query, params)

    @staticmethod
    def get_records_by_user(user_id):
        query = "SELECT * FROM FoodRecord WHERE ID = %s ORDER BY eat_date DESC"
        return fetch_data(query, (user_id,))

    @staticmethod
    def delete_record(user_id, eat_date, fID):
        query = "DELETE FROM FoodRecord WHERE ID = %s AND eat_date = %s AND fID = %s"
        modify_data(query, (user_id, eat_date, fID))
