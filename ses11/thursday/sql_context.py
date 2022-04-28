from sqlite3 import connect
from contextlib import contextmanager


@contextmanager
def create_tbl(cur):
        cur.execute('CREATE TABLE students(id int PRIMARY KEY, name text, cpr text)')
        yield 12
        cur.execute('DROP TABLE students')


with connect('testfiles/school.db') as conn:
    cur = conn.cursor()
    
    with create_tbl(cur) as x:

        print(type(x))
        # cur.execute('CREATE TABLE students(id int PRIMARY KEY, name text, cpr text)')
        cur.execute('INSERT INTO students(id, name, cpr) VALUES (1, "Claus", "223344-5566")')
        cur.execute('INSERT INTO students(id, name, cpr) VALUES (2, "Julie", "111111-1111")')
        cur.execute('INSERT INTO students(id, name, cpr) VALUES (3, "Hannah", "222222-2222")')

        for i in cur.execute('SELECT * FROM students'):
            print(i)

        # cur.execute('DROP TABLE students')

