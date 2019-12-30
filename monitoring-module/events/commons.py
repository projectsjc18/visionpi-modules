# DB
import sqlite3
# Dates
import datetime


class Dates():
    def formatDate(o):
        if isinstance(o, datetime.datetime):
            return o.__str__()


class Database():
    def __init__(self):
        self.conn = sqlite3.connect('../db/visionpi.db')

    def __del__(self):
        self.conn.close()

    def loadDatabase(self):
        try:
            print('Connection is established: Database is created.')
            # print('checkTable', checkTable(conn))
            if (self.check_table() is True):
                print('Table exist.')
            else:
                # Create table
                self.conn.execute('''CREATE TABLE monitoring_events
                              (account, device, event, type, status,
                              eventdate)''')
                print('Table is created')
        except sqlite3.Error as e:
            print('Database failed: ', e.args[0])
        else:
            self.conn.commit()
            print("Success")
        finally:
            print("Finished")

    def check_table(self):
        c = self.conn.cursor()
        c.execute('''SELECT * FROM sqlite_master
                   WHERE name ='monitoring_events' and type='table' ''')
        # print('rowcount: ', c.fetchone())
        if (c.fetchone() is None):
            return False
        else:
            return True

    def save_event(self, account, device, event, type, status, eventdate):
        c = self.conn.cursor()
        print(account)
        print(device)
        print(event)
        print(type)
        print(status)
        print(eventdate)
        # This is the qmark style:
        c.execute("insert into monitoring_events values (?, ?, ?, ?, ?, ?)",
                  (account, device, event, type, status, eventdate))
        self.conn.commit()
        print('Finished save')
