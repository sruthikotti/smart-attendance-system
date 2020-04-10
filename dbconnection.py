import sqlite3
connection = sqlite3.connect("test.db")
cursor = connection.cursor();
#sql_command = """
#CREATE TABLE stu_attendance(name varchar2(10),status varchar2(10));"""
#cursor.execute(sql_command)
#print("table created")
sql_command = """INSERT INTO stu_attendance VALUES ("sruthi","absent");"""
cursor.execute(sql_command)

#sql_command="""INSERT INTO stu_attendance values("pravalika","absent");"""
#cursor.execute(sql_command)
#sql_command="""update  attendance5 set status="absent" where name="pravalika";"""
#cursor.execute(sql_command)
#sql_command=""" delete from attendance5 where name="sruthi";"""
#cursor.execute(sql_command)

# never forget this, if you want the changes to be saved:
connection.commit()

connection.close()
