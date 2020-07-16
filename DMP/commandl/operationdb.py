# library
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# parent class
class adminDB:
    def __init__(self, **kwargs):
        # set default value for connection db
        arguments = {'host':'0.0.0.0', 
                     'port':5432,
                     'dbname':'',
                     'user':'',
                     'password':''
                     }
        # call update value for connection db
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


# Child class (inherits from adminDB class)
class steward(adminDB):
    # instance method for show all databases
    def alldb(self):
        try:
            sh= steward(
                host="{}".format(self.host),
                port="{}".format(self.port),
                dbname="{}".format(self.dbname),
                user="{}".format(self.user),
                password="{}".format(self.password)
            )       
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
            sh= steward(
                host="{}".format(self.host),
                port="{}".format(self.port),
                dbname="{}".format(self.dbname),
                user="{}".format(self.user),
                password="{}".format(self.password)
            )
            cursor= sh.connectiondb()
            cursor.execute("select 1 from pg_catalog.pg_database where datname = '{}'".format(dbname))
            exists = cursor.fetchone()
            if not exists:
                cursor.execute("create database {}".format(dbname))
                print("done writing the database '{}'".format(dbname))
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
            sh= steward(
                host="{}".format(self.host),
                port="{}".format(self.port),
                dbname="{}".format(self.dbname),
                user="{}".format(self.user),
                password="{}".format(self.password)
            )
            cursor= sh.connectiondb()
            cursor.execute("""
                            select pg_terminate_backend (pg_stat_activity.pid)
                            from pg_stat_activity
                            where pg_stat_activity.datname = '{}';
                           """.format(dbname),
                           """
                            drop database if exists {};
                           """.format(dbname)
                    )
            print("remove database '{}' done".format(dbname))
        except (Exception) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
            if(sh.connectiondb()):
                cursor.close()
                sh.connectiondb().close()

    # instance method for create table
    def cr_table(self, tabname, colname):
        try:
            sh= steward(
                host="{}".format(self.host),
                port="{}".format(self.port),
                dbname="{}".format(self.dbname),
                user="{}".format(self.user),
                password="{}".format(self.password)
            )
            cursor= sh.connectiondb()
            cursor.execute("""
                    drop table if exists {};
                    create table if not exists {} ({})""".format(tabname, tabname, colname)
                    )
            print("table '{}' has been successfully created".format(tabname))
        except (Exception) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
            if(sh.connectiondb()):
                cursor.close()
                sh.connectiondb().close()

    def multicr_table(self, commands):
        try:
            sh= steward(
                host="{}".format(self.host),
                port="{}".format(self.port),
                dbname="{}".format(self.dbname),
                user="{}".format(self.user),
                password="{}".format(self.password)
            )
            cursor= sh.connectiondb()
            for command in commands:
                cursor.execute(command["SQL"])
                print("Executed {}".format(command["Description"]))
        except (Exception) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
            if(sh.connectiondb()):
                cursor.close()
                sh.connectiondb().close()

    # instance method for show all tables
    def show_tables(self):
        try:
            sh= steward(
                host="{}".format(self.host),
                port="{}".format(self.port),
                dbname="{}".format(self.dbname),
                user="{}".format(self.user),
                password="{}".format(self.password)
            )       
            cursor= sh.connectiondb()
            cursor.execute("""SELECT table_name 
                              FROM information_schema.tables
                              WHERE table_schema = 'public'
                           """
                        )
            record= cursor.fetchall()
            print("all tables you have is - ", record,"\n")
        except (Exception) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing databases connection.
            if(sh.connectiondb()):
                cursor.close()
                sh.connectiondb().close()

    # instance method for show name and data type columns in specific table
    def det_table(self, tabname):
        try:
            sh= steward(
                host="{}".format(self.host),
                port="{}".format(self.port),
                dbname="{}".format(self.dbname),
                user="{}".format(self.user),
                password="{}".format(self.password)
            )       
            cursor= sh.connectiondb()
            cursor.execute("""SELECT column_name, data_type
                              FROM INFORMATION_SCHEMA.COLUMNS 
                              WHERE table_name = '{}';
                           """.format(tabname)
                        )
            record= cursor.fetchall()
            print("info column in table '{}' - ".format(tabname), record,"\n")
        except (Exception) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing databases connection.
            if(sh.connectiondb()):
                cursor.close()
                sh.connectiondb().close()

    # instance method for insert row data
    def insert_rows(self, tabname, colname, rows):
        try:
            sh= steward(
                host="{}".format(self.host),
                port="{}".format(self.port),
                dbname="{}".format(self.dbname),
                user="{}".format(self.user),
                password="{}".format(self.password)
            )       

            cursor= sh.connectiondb()

            t= '({})'.format(colname)
            argument_string = ",".join('{}'.format(len(colname.split(", "))* ("%s",)) % t for t in rows)

            cursor.execute("INSERT INTO {table} VALUES".format(table=tabname) + argument_string)

            print("insert data into table '{}'".format(tabname))
        except (Exception) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing databases connection.
            if(sh.connectiondb()):
                cursor.close()
                sh.connectiondb().close()