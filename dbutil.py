from dbmanager import DBManager


class DBUtil:


@staticmethod
def excuteNonQuery (nonQuerySQL) -> None:


# getconn( is used to get an available connection from the connection pool
with DBManager.getConn( as conn:
if (conn):
ps_cursor = conn.cursor()
ps_cursor.execute("SELECT * FROM emp_info_schema.employee_details")
employees_detail = ps_cursor.fetchall()
print("Displaying rows from mobile table")
for row in employees_detail:
print(row)
ps_cursor.close()
+ with the use of this method we can release the connection object and send it back to the connection pool
DBManager.putConn(conn)
print("Put away a PostgresQL connection")


@staticmethod
def excuteQuery(sqlQuery) -> list:
rows:list = []
# getconn() is used to get an available connection from the connection pool
with DBManager getConn() as conn:
if (conn):


ps_cursor = conn.cursor()
ps_cursor.execute(sqlQuery)
employees_detail = ps_cursor.fetchall()


for row in employees_detail:
rows.append(row)


ps_cursor.close(
# with the use of this method we can release the connection object and send it back to the connection pool
DBManager.putConn(conn)


return rows
