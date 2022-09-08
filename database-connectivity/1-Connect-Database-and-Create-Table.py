#!/bin/python3

import sys
import os
import sqlite3




# Complete the following function:

def main():
    conn = sqlite3.connect('SAMPLE.db')
    #create connection cursor
    cursor = conn.cursor()
    #create table ITEMS using the cursor
    sql = """CREATE TABLE ITEMS (
            ITEM_ID INT, 
            ITEM_NAME VARCHAR, 
            ITEM_DESCRIPTION VARCHAR, 
            ITEM_CATEGORY VARCHAR, 
            QUANTITY_IN_STOCK INT
            )
    """
    cursor.execute(sql)
    #commit connection 
    conn.commit()
    #close connection
    conn.close()


'''To test the code, no input is required'''

if __name__ == "__main__":
    f = open(os.environ['OUTPUT_PATH'], 'w')

    res = main();
    f.write(str(res) + "\n")


    f.close()
