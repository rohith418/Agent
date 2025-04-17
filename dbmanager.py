import psycopg2
from psycopg2 import pool
import psycopg2.extensions
import logging as LOG
import os
from util.config import Config
"""
Connection Pooling Best Practices
Here are some best practices to keep in mind when using connection pooling in Python:
Use a connection pool for each database that your application uses
Always return connections to the pool when you are finished using them. Failing to do so can lead to resource leaks and reduced performance
Use the with statement when working with connections and cursors. This ensures that they are properly closed and returned to the pool when you are finished using t
Avoid creating more connections than you need. This can lead to resource contention and reduced performance
Be mindful of connection timeouts. If a connection is idle for too long, it may be closed by the database server, which can cause errors in your application
"""
class DBManager:
"""DB Manager provides ThreadedConnectionPool as per configuration
Its has below Static methods
Pool()--> Provides pool accessThreadedConnectionPool
getConn()--> Gets
shared_instance = 'NotInitialized
threaded_conn_pool:pool.ThreadedConnectionPool = None
DBConnPoolSettings:dict={}
@staticmethod
def Pool() -> pool.ThreadedConnectionPool:
"""Gets Default Connection Pool"""
if DBManager.__shared_instance == NotInitialized
DBManager()


return DBManager.__shared_instance.threaded_conn_pool


@staticmethod


def initConfig(config:Config):
DBManager .DBConnPoolSettings["host"]-config.get("Database", "host",default="localhost")
DBManager.DBConnPoolSettings["port"]=config.get("Database","port",default="5432")
DBManager.DBConnPoolSettings["database"]-config.get("Database","database",default="postgres")
uName:str = config.get("Database", "username",default="postgres")
uPwd:str= config.get("Database","password",default="VCG#123") #TODO - This needs to be


decrepted once the password is encrypted in config


if uName.startswith("ENVVAR.'):
uName=os.environ.get(uName.split(".")[1],"postgres')
if uPwd.startswith("ENVAR.'):
uPwd=os.environ.get(uPwd.split(".')[1],'")


DBManager.DBConnPoolSettings["user"]- uName
DBManager.DBConnPoolSettings["password"]-uPwd
DBManager .DBConnPoolSettings["minPoolConns"]=config.get("Database","minPoolConns",default="2")
DBManager.DBConnPoolSettings["maxPoolConns"]-config.get("Database","maxPoolConns",default="10")
@staticmethod
def getConn() -> any:
"""Gets One Connection from Default Pool"""
return DBManager.Pool().getconn()


@staticmethod
def putConn(conn):
"""Puts One Connection back to Default Pool"""
DBManager.Pool().putconn(conn)


@staticmethod
def closeall():
"""Close all connections in the Default Pool"""
DBManager.Pool().closeall()


def _init_(self):
"""virtual private constructor"""
if DBManager.__shared_instance != 'NotInitialized':
raise Exception("This class is a singleton class !")


else:
self. initDBPool()
DBManager._shared_instance = self


TODO: Write code to clear unused connections and replace pool in a thread for every 60secs
This will make sure in case of there are all connections in pool are used but not closed.
"""
@staticmethod
def _initDBPool(self):
try:


self.threaded_conn_pool = psycopg2.pool.ThreadedConnectionPool(
int(DBManager.DBConnPoolSettings["minPoolConns"])
int(DBManager.DBConnPoolSettings["maxPoolConns"])
user=DBManager.DBConnPoolSettings["user"]
password=DBManager.DBConnPoolSettings["password"]
host=DBManager.DBConnPoolSettings["host"],
port=DBManager.DBConnPoolSettings["port"]
database=DBManager.DBConnPoolSettings["database"]


if (self.threaded_conn_pool):
LOG. info("Connection pool created successfully")


except (Exception, psycopg2.DatabaseError) as error:
LOG.info("Error while connecting to PostgresQl", error)
raise Exception("Create Pool error", error)


@staticmethod


def executeSP(spName:str, params:tuple, transConn - None) -> any:


conn = 
None
if transConn:
conn = transConn


else:


conn = DBManager.getConn(
returnResults= []
try:
# Create a cursor


with conn.cursor() as cur:
# Call the stored procedure
cur.execute(spName, params)


#retrieve the results from out parameters


results = cur.fetchall()


if results:


returnResults=results[0] # results[0][0], results[0][1]


# Commit the changes
if not transConn:
conn. commit (


# Close the cursor and connection
cur.close(


print("Stored procedure called successfully!")
except Exception as e:
print(f"Error calling stored procedure {spName}: {e}")
finally:
if not transConn:
DBManager.putConn(conn)


return returnResults


@staticmethod
def fetchSQL(selectStatment:str


inputParms: tuple=()) -> any:


conn
DBManager getConn ()
I


returnResults = []


try:
# Create a cursor
cur = conn.cursor(
# Call the stored procedure
cur.execute(selectStatment, inputParms)


#retrieve the results from out parameters
results = cur.fetchall()
if results:
returnResults=results # results[0][0], results[0][1]
# Close the cursor and connection
cur.close()


print("Stored procedure called successfully!")
except Exception as e:


print(f"Error calling stored procedurefselectStatment): fe)")
finally:
DBManager.putConn(conn)


return returnResults


@staticmethod
def insertorUpdate(dmlStatement:str, values:tuple) -> int:

"""
dmlStatement: insert into tablel (col1, col2, col3) values(%s, %d, %s)
values: ("value 1", 23, "3rd param")
"""


conn = DBManager .getConn (
returnResults
try:
# Create a cursor
cur = conn.cursor ()
# Call the stored procedure
cur.execute(dmlStatement, values)
#retrieve the results from out parameters
results = cur.fetchall()
if results:


returnResults=results[0][0] # results[0][0], results[0][1]


# Commit the changes
conn.commit()
# Close the cursor and connection
cur.close()


print("Stored procedure called successfully!")
except Exception as e:


print(f"Error calling stored procedure(dmlStatement): (e)")
finally:
DBManager.putConn(conn)


return returnResults
# main method
if
_name


_main"


# create object of Singleton Class
obj = DBManager()
print(obj)


# pick the instance of the class
obj=DBManager.Pool()
print(obj)
