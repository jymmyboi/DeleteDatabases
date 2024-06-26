import pymssql
import sys

excluded_dbs = []
db_list = []
system_dbs = ['master','model','msdb','tempdb']

def get_exclusions():
    with open("excluded_dbs.txt", 'r') as file:
        for line in file:
            excluded_dbs.append(line.strip())

def get_databases(cursor):
    try:
        cursor.execute("SELECT name FROM sys.sysdatabases")
        for row in cursor:
            if row['name'] not in excluded_dbs and row['name'] not in system_dbs:
                db_list.append('[' + row['name'] + ']')
    except Exception as e:
        print("An exception occurred: ", e)
        sys.exit(1)

def delete_databases(cursor):
    try:
        for item in db_list:
            cursor.execute("DROP DATABASE " + item + ';')
            print("DROPPED DATABASE " + item)
    except Exception as e:
        print("An exception occurred: ", e)
        sys.exit(1)
    
def main():
    server = input("Server Name: ")
    user = input("Username: ")
    password = input("Password: ")
    try:
        conn = pymssql.connect(server, user, password, 'master')
        cursor = conn.cursor(as_dict=True)
    except Exception as e:
        print("An exception occurred: ", e)
        sys.exit(1)
    conn.autocommit(True)
    get_exclusions()
    get_databases(cursor)
    delete_databases(cursor)
    conn.close()

if __name__ == "__main__":
    main()