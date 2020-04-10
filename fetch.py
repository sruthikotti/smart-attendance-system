import sqlite3
conn=sqlite3.connect('test.db')
print("opened db success")
cursor=conn.execute("select * FROM stu_attendance");
for row in cursor:
    print("name=",row[0])
    print("status=",row[1])
conn.close()
