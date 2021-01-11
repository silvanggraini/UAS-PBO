# import sqlite3
# from connect import connect
import main

class tampilTabel(main.Inti):
    def tampilData(self,tabelInputan):
        query = 'SELECT * from {}'.format(tabelInputan)
        tampil = self.execute(query,True)
        for row in tampil:
            print(row)

