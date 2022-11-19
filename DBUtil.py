import pymysql


class DBUtil:
    endpoint = 'todotoronto.cvi29upq4yqe.us-east-1.rds.amazonaws.com'
    username = 'admin'
    password = '123itisMe!'
    dbName = 'prod'

    connection = pymysql.connect(host=endpoint, user=username,
                                 password=password, database=dbName)

    def executeQuery(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)

        results = cursor.fetchall()
        return results
