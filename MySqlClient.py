import pymysql


class MySqlClient:

    def __init__(self, host, user, password, database, autocommit=True):
        """
        :param host:
        :param user:
        :param password:
        :param database:
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self._connection(autocommit)

    def _connection(self, autocommit):
        self.connection = pymysql.connect(host=self.host,
                                          user=self.user,
                                          password=self.password,
                                          db=self.database,
                                          charset='utf8mb4',
                                          autocommit=autocommit,
                                          cursorclass=pymysql.cursors.DictCursor)

    def execute(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            res = cursor.fetchall()
            return res
