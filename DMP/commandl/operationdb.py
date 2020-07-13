# parent class
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class adminDB:
    def __init__(self, **kwargs):
        # set default value
        arguments = {'host':'0.0.0.0', 
                     'port':5432,
                     'dbname':'',
                     'user':'postgres',
                     'password':'secrect'
                     }
        # call update value
        arguments.update(kwargs)
        self.host = arguments['host']
        self.port = arguments['port']
        self.dbname = arguments['dbname']
        self.user = arguments['user']
        self.password = arguments['password']

    # instance method for connection db
    def connectiondb(self):  
        
        conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        
        return conn.cursor()

    # instance method for show all databases
    def alldb(self):
        try:
            sh= adminDB()
            cursor= sh.connectiondb()
            cursor.execute('SELECT datname FROM pg_database')
            record= cursor.fetchall()
            print("all database you have is - ", record,"\n")
        except (Exception) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing databases connection.
            if(sh.connectiondb()):
                cursor.close()
                sh.connectiondb().close()

    # instance method for create database
    def create_db(self, dbname):
        try:
            sh= adminDB()
            cursor= sh.connectiondb()
            cursor.execute("select 1 from pg_catalog.pg_database where datname = '{}'".format(dbname))
            exists = cursor.fetchone()
            if not exists:
                cursor.execute("create database {}".format(dbname))
                print("done")
        except (Exception) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
            if(sh.connectiondb()):
                cursor.close()
                sh.connectiondb().close()

    # instance method for remove database
    def remove_db(self, dbname):
        try:
            sh= adminDB()
            cursor= sh.connectiondb()
            cursor.execute("drop database if exists {}".format(dbname))
            print("remove database {} done".format(dbname))
        except (Exception) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
            if(sh.connectiondb()):
                cursor.close()
                sh.connectiondb().close()

    # instance method for create table
    def cr_table(self, dbname, tabname, colname):
        try:
            sh= adminDB(dbname="{}".format(dbname))
            cursor= sh.connectiondb()
            cursor.execute("CREATE TABLE IF NOT EXISTS {} ({})".format(tabname, colname))
            print("table {} has been successfully created in {}".format(tabname, dbname))
        except (Exception) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
            if(sh.connectiondb()):
                cursor.close()
                sh.connectiondb().close()