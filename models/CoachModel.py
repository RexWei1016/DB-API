from db.database import fetch_data, modify_data

class CoachModel:
    @staticmethod
    def get_coach_by_id(cID):
        query = "SELECT cID, pwd, name FROM Coach WHERE cID = %s"
        return fetch_data(query, (cID,))

    @staticmethod
    def create_coach(data):
        query = '''
            INSERT INTO Coach (cID, pwd, name, onboarding, exp)
            VALUES (%s, %s, %s, %s, %s)
        '''
        params = (data['cID'], data['pwd'], data['name'], data['onboarding'], data['exp'])
        modify_data(query, params)

    @staticmethod
    def get_all_coaches():
        query = "SELECT cID, pwd, name, onboarding, exp FROM Coach"
        return fetch_data(query)
