import pyodbc
from util.PropertyUtil import PropertyUtil

class DBConnection:

    @staticmethod
    def getConnection():
        try:
            connection_string=PropertyUtil.getPropertyString()
            connection=pyodbc.connect(connection_string)
            print("Connected successfully")
            return connection
        except Exception as e:
            print(str(e) + '--Database is not connected--')
            return None

