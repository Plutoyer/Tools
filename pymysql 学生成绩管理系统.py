import pymysql
db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db='python',
        charset='utf8')
cur = db.cursor()
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS StuSys")
cur.execute("use python;")
# 建表
cur.execute("create table StuSys(name char(20),"
            "chinese char(20),english char(20) ,math char(20),total char(20))character set utf8;")



def appendStudentInfo():
    db = pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',db='python', charset='utf8')
    cursor = db.cursor()#利用db方法创建游标对象
    name = input("请输入学生姓名：")
    chinese = input("请输入语文成绩：")
    math = input("请输入数学成绩：")
    english = input("请输入英语成绩：")
    total = int(chinese) + int(math) + int(english)
    sql = """INSERT INTO StuSys(NAME,CHINESE,ENGLISH,MATH,TOTAL)VALUES (%s,%s,%s,%s,%s)"""
    try:
        cursor.execute(sql, (name,chinese,english,math,total))
        db.commit()
    except:
        db.rollback()
    db.close()

def delstudent(delstudentname):
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='python', charset='utf8')
    cursor = db.cursor()
    sql = "DELETE FROM StuSys WHERE Name='" + delstudentname + "'"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()
    print("删除成功")


def querystudent(studentname):
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='python', charset='utf8')
    cursor = db.cursor()
    sql = 'select * from StuSys where NAME="%s"' % studentname
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print("NAME=%s,CHINESE=%s,ENGLISH=%s,MATH=%s,TOTAL=%s" % \
          (results[0][0], results[0][1], results[0][2], results[0][3], results[0][4]))
        return True
    except:
        db.rollback()


def modifystudentifo(Nname,Nchinese,Nenglish,Nmath):
        total = int(Nchinese) + int(Nmath) + int(Nenglish)
        Ntotal = str(total)
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='python', charset='utf8')
        cursor = db.cursor()

        sql = "UPDATE StuSys SET MATH='%s',CHINESE='%s',ENGLISH='%s',TOTAL='%s' WHERE NAME = '%s'"%(Nmath,Nchinese,Nenglish,Ntotal,Nname)

        try:
            cursor.execute(sql)

            db.commit()
        except:
            db.rollback()

        db.close()


def allinfo():
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='python', charset='utf8')
    cursor = db.cursor()
    sql = "select * from StuSys"
    cursor.execute(sql)
    results = cursor.fetchall()
    # print(results)
    dict_num={}
    i=0
    print("偏科的有：")
    for row in results:
        NAME = row[0]
        CHINESE = int(row[1])
        ENGLISH = int(row[2])
        MATH = int(row[3])
        AVE = int(row[4])/3
        dict_num[i]=int(row[4])
        i=i+1
        if abs(int(CHINESE-ENGLISH))>20 or abs(int(CHINESE-MATH))>20 or abs(int(ENGLISH-MATH))>20:

            print("NAME=%s,CHINESE=%s,ENGLISH=%s,MATH=%s,AVE=%s" % (NAME, CHINESE, ENGLISH, MATH,AVE))
    d1 = sorted(dict_num.items(), key=lambda dict_num: dict_num[1], reverse=False)
    print("排序：")
    for row in d1:
        name=results[int(row[0])][0]
        chinese = int(results[int(row[0])][1])
        english = int(results[int(row[0])][2])
        math = int(results[int(row[0])][3])
        total=int(results[int(row[0])][4])

        print("NAME=%s,CHINESE=%s,ENGLISH=%s,MATH=%s,TOTAL=%s" % (name, chinese, english, math,total))


def studentMenu():
    print("=" * 30)
    print("学生管理系统")
    print("1、添加学生信息")
    print("2、删除学生信息")
    print("3、查询学生信息")
    print("4、修改学生信息")
    print("5、全部学生信息")
    print("6、退出")
    print("=" * 30)


if __name__ == '__main__':

    while True:
        studentMenu()
        menuindex = input("请输入选项序号：")
        while not menuindex.isdigit():
            menuindex = input("输入错误，请重新输入：")
        if int(menuindex) == 1:
            appendStudentInfo()
        elif int(menuindex) == 2:
            delstudentname = input("请输入要删除的学生姓名：")
            delstudent(delstudentname)
        elif int(menuindex) == 3:
            studentname = input("请输入要查询的学生名字：")
            querystudent(studentname)
        elif int(menuindex) == 4:

            Nname = input("要修改成绩的学生姓名：")
            Nchinese = input("请重新输入语文成绩：")
            Nmath = input("请重新输入数学成绩：")
            Nenglish = input("请重新输入英语成绩：")
            modifystudentifo(Nname,Nchinese,Nenglish,Nmath)
        elif int(menuindex) == 5:
            allinfo()
        elif int(menuindex) == 6:
            break
        else:
            print("输入序号无效")