import csv
from importlib.resources import contents
from multiprocessing import connection 
import sqlite3
import pandas as pd 

columns = ['id','MSIND','','', '']

class SavingToSQL:
    def __init__(self, df:pd.DataFrame):
        #initializing model 
        self.df = df
        self.connection = sqlite3.connect('Tellcommunication.db')
        self.cursor = self.connection.cursor()
        print("Automation in action ")


    def create_table(self):
        create_table = '''CREATE TABLE User_experience(id INTEGER PRIMARY KEY AUTOIINCREMENT,
                                        MSIND NUMBER NOT NULL,
                                        ......................,
                                        ......................,
                                         ......................,
                                        )'''

        print('Table creation in action')

        try:
            self.cursor.excute(create_table)

        except sqlite3.OperationalError:
            print('Table already exist...')


    def csv_to_sql(self):
        contents = pd.read_csv(self.df)
        self.connection.commit()
        contents.to_sql('user_experience', self.connection, if_exists='replace', index=True)
        self.connection.commit()


    def sql_fetchall(self):
        self.cursor.execute(''' SELECT * FROM user experience''')
        display=pd.DataFrame(self.cursor.fetchall())
        display.columns=columns
        print(display)
        self.connection.commit()

    def sql_close(self):
        self.connection.close()

def fetchall ():
    connection = sqlite3.connect('telco.db')
    cursor =connection.cursor()
    cursor.execute(''' SELECT * FROM user_experience''')
    display = pd.DataFrame(cursor.fetchall())
    display.columns = columns
    print (display)
    connection.commit()
    connection.close()

	
if __name__ == '__main__':
    file = ''
    fetchall ()
		



