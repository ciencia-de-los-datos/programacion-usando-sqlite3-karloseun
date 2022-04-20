import pprint as pp
import sqlite3

def load_data():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    with open("create_tables.sql", encoding="utf-8") as file:
        cur.executescript(file.read())

    return conn, cur

def pregunta_01():
    conn, _ = load_data()

    q01 = _.execute("SELECT SUM(c12) FROM tbl1;").fetchall()

    return q01

def pregunta_02():
    conn, _ = load_data()

    q02 = _.execute("SELECT COUNT(*) FROM tbl1;").fetchall()

    return q02

def pregunta_03():
    conn, _ = load_data()

    q03 = _.execute("SELECT * FROM tbl1 ORDER BY c14 ASC LIMIT 5;").fetchall()

    return q03

def pregunta_04():
    conn, _ = load_data()

    q04 = _.execute("SELECT K0, c16 FROM tbl1 WHERE K0 = substr(c16,1,1);").fetchall()

    return q04

def pregunta_05():
    conn, _ = load_data()

    q05 = _.execute("SELECT * FROM tbl0 WHERE c02 = 100 OR c02 = 600;").fetchall()

    return q05

def pregunta_06():
    conn, _ = load_data()

    q06 = _.execute("SELECT * FROM tbl1 WHERE K0 = 'A' ORDER BY c14;").fetchall()

    return q06

def pregunta_07():
    conn, _ = load_data()

    q07 = _.execute("SELECT * FROM tbl1 WHERE K0 NOT IN ('A','B') AND c13 NOT IN (200,900) ORDER BY c14;").fetchall()

    return q07

def pregunta_08():
    conn, _ = load_data()

    q08 = _.execute("SELECT strftime('%Y',c23) as year, AVG(c21) FROM tbl2 GROUP BY strftime('%Y',c23);").fetchall()

    return q08

def pregunta_09():
    conn, _ = load_data()

    q09 = _.execute("SELECT K1, MIN(c21) as c21, c22, c23, c24, c25 FROM tbl2;").fetchall()

    return q09

def pregunta_10():
    conn, _ = load_data()

    q10 = _.execute("SELECT * FROM tbl0 WHERE c02 >=300;").fetchall()

    return q10

def pregunta_11():
    conn, _ = load_data()

    q11 = _.execute("SELECT strftime('%Y',c14) as YEAR, COUNT(K1) as CANT FROM tbl1 GROUP BY YEAR HAVING YEAR = '2018';").fetchall()

    return q11

def pregunta_12():
    conn, _ = load_data()

    q12 = _.execute("SELECT K0, MAX(c12), min(C12) FROM tbl1 GROUP BY K0;").fetchall()

    return q12

def pregunta_13():
    conn, _ = load_data()

    q13 = _.execute("SELECT K0, avg(c12) FROM tbl1 WHERE c13 > 400 GROUP BY K0;").fetchall()

    return q13

def pregunta_14():
    conn, _ = load_data()

    q14 = _.execute("SELECT tbl1.K0 as K0, avg(tbl2.c21) as 'avg(c21)' FROM tbl1, tbl2 WHERE tbl1.K1 = tbl2.K1 and tbl1.c13 > 400 GROUP BY tbl1.K0;").fetchall()

    return q14

print ("\n* * * * * * * * * * * * * * * * * * Result Q01 ---> \n") 
pp.pprint( pregunta_01() )
print ("\n* * * * * * * * * * * * * * * * * * Result Q02 ---> \n") 
pp.pprint( pregunta_02() )
print ("\n* * * * * * * * * * * * * * * * * * Result Q03 ---> \n") 
pp.pprint( pregunta_03() )
print ("\n* * * * * * * * * * * * * * * * * * Result Q04 ---> \n") 
pp.pprint( pregunta_04() )
print ("\n* * * * * * * * * * * * * * * * * * Result Q05 ---> \n") 
pp.pprint( pregunta_05() )
print ("\n* * * * * * * * * * * * * * * * * * Result Q06 ---> \n") 
pp.pprint( pregunta_06() )
print ("\n* * * * * * * * * * * * * * * * * * Result Q07 ---> \n") 
pp.pprint( pregunta_07() )
print ("\n* * * * * * * * * * * * * * * * * * Result Q08 ---> \n") 
pp.pprint( pregunta_08() )
print ("\n* * * * * * * * * * * * * * * * * * Result Q09 ---> \n") 
pp.pprint( pregunta_09() )
print ("\n* * * * * * * * * * * * * * * * * * Result Q10 ---> \n") 
pp.pprint( pregunta_10() )
print ("\n* * * * * * * * * * * * * * * * * * Result Q11 ---> \n") 
pp.pprint( pregunta_11() )
print ("\n* * * * * * * * * * * * * * * * * * Result Q12 ---> \n") 
pp.pprint( pregunta_12() )
print ("\n* * * * * * * * * * * * * * * * * * Result Q13 ---> \n") 
pp.pprint( pregunta_13() )
print ("\n* * * * * * * * * * * * * * * * * * Result Q14 ---> \n") 
pp.pprint( pregunta_14() )
