class Database:
    _instance = None

    @staticmethod
    def getInstance():
        if Database._instance == None:
            Database._instance = Database()
        return Database._instance

    def connect(self):
        return "Connecting to the database"
