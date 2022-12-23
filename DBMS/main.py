import tkinter as tk
import logging
import pymysql
import argparse

from tkinter import scrolledtext,END
from tkinter import ttk
from PIL import Image, ImageTk
root_register = 0
root_window = 0

def init_main_GUI():
    def borrow():
        #进行借书操作
        def do_borrow():
            student_id = entry1.get() #学生学号
            book_id = entry2.get()  #书籍编号
            cursor = conn.cursor()
            # 使用 execute()方法执行 SQL 查询
            #查找学生借阅数目
            sql = "select snum from student_borrow where sno = " + student_id
            cursor.execute(sql)
            try:
                num_borrow = cursor.fetchall()[0][0]
            except:
                num_borrow = 0
            #查询书籍借阅数目
            sql = "select bremain from book_borrow where bno = " + book_id
            cursor.execute(sql)
            try:
                num_remain = cursor.fetchall()[0][0]
            except:
                num_remain = 0
            if (int)(num_borrow) > 5 :
                result = "请先退还书籍"
                # 将计算的结果显示在Label控件上
                label.config(text=result)
            if (int)(num_remain) == 0 :
                result = "借阅书籍不足"
                label.config(text=result)
            #检查基本数据完毕，进行借出操作
            #修改student_book
            sql = "insert into student_book (sno, bno, time ) VALUES(" + str(student_id)+", " + book_id + "," + "'2022/12/23'"+ ");"
            cursor.execute(sql)
            print(sql)
            #修改student_borrow
            sql = 'update student_borrow set snum = snum + 1 where sno = '+ str(student_id) + ";"
            print(sql)
            cursor.execute(sql)
            #修改book_borrow
            sql = 'update book_borrow set bremain = bremain - 1 where bno = '+ str(book_id) + ";"
            print(sql)
            cursor.execute(sql)
            conn.commit()
            print("ok")
        root_borrow = tk.Tk()
        root_borrow.title('图书馆管理系统')
        root_borrow.geometry('450x300')
        label = tk.Label(root_borrow)
        text = tk.Label(root_borrow, text="借 书", bg="yellow", fg="red", font=('Times', 20, 'bold italic'))
        label1 = tk.Label(root_borrow, text="学生学号：")
        entry1 = tk.Entry(root_borrow)
        label2 = tk.Label(root_borrow, text="书籍编号：")
        entry2 = tk.Entry(root_borrow)
        button = tk.Button(root_borrow, text="执行", command=do_borrow)
        text.pack()
        label1.pack()
        entry1.pack()
        label2.pack()
        entry2.pack()
        label.pack()
        button.pack()
        root_borrow.mainloop()
    def reback():
        # 进行还书操作
        def do_reback():
            student_id = entry1.get()  # 学生学号
            book_id = entry2.get()  # 书籍编号
            cursor = conn.cursor()
            # 使用 execute()方法执行 SQL 查询
            #删除student_book
            sql = 'delete from student_book where sno = ' +str(student_id) + ' and bno = ' + str(book_id) + ';'
            print(sql)
            cursor.execute(sql)
            #更改student_borrow
            sql = 'update student_borrow set snum = snum - 1 where sno = ' + str(student_id) + ";"
            print(sql)
            cursor.execute(sql)
            #更改book_borrow
            sql = 'update book_borrow set bremain = bremain + 1 where bno = ' + str(book_id) + ";"
            print(sql)
            cursor.execute(sql)
            conn.commit()
            print("ok")
        root_reback = tk.Tk()
        root_reback.title('图书馆管理系统')
        root_reback.geometry('450x300')
        text = tk.Label(root_reback, text="还 书", bg="yellow", fg="red", font=('Times', 20, 'bold italic'))
        label1 = tk.Label(root_reback, text="学生学号：")
        entry1 = tk.Entry(root_reback)
        label2 = tk.Label(root_reback, text="书籍编号：")
        entry2 = tk.Entry(root_reback)
        button = tk.Button(root_reback, text="执行", command=do_reback)
        text.pack()
        label1.pack()
        entry1.pack()
        label2.pack()
        entry2.pack()
        button.pack()
        root_reback.mainloop()
    def add_book():
        # 进行添加书籍操作
        def add():
            bno = entry1.get()
            bname = entry2.get()
            bauthor = entry3.get()
            bnum = entry4.get()
            cursor = conn.cursor()
            # 使用 execute()方法执行 SQL 查询
            # 增加book
            sql = "insert into book (bno, bname, bauthor ) VALUES(" + str(bno)+", '" + str(bname) + "','" + str(bauthor) + "');"
            print(sql)
            cursor.execute(sql)
            # 增加book_borrow
            sql = "insert into book_borrow (bno, bname, bnum, bremain ) VALUES(" + str(bno)+", '" + str(bname) + "'," + str(bnum) +"," + str(bnum)+  ");"
            print(sql)
            cursor.execute(sql)
            conn.commit()
            print("ok")
        def modeify():
            bno = entry1.get()
            bname = entry2.get()
            bauthor = entry3.get()
            bnum = entry4.get()
            cursor = conn.cursor()
            #删除book
            sql = 'delete from book where bno = ' +str(bno) + ';'
            print(sql)
            cursor.execute(sql)
            #删除book_borrow
            sql = 'delete from book_borrow where bno = ' + str(bno) + ';'
            print(sql)
            cursor.execute(sql)
            #添加新book
            add()
        def delete():
            bno = entry1.get()
            bname = entry2.get()
            bauthor = entry3.get()
            bnum = entry4.get()
            cursor = conn.cursor()
            # 删除book
            sql = 'delete from book where bno = ' + str(bno) + ';'
            print(sql)
            cursor.execute(sql)
            # 删除book_borrow
            sql = 'delete from book_borrow where bno = ' + str(bno) + ';'
            print(sql)
            cursor.execute(sql)
            # 删除student_borrow
            sql = 'delete from student_book where bno = ' + str(bno) + ';'
            cursor.execute(sql)
            conn.commit()
        root_add_book = tk.Tk()
        root_add_book.title('图书馆管理系统')
        root_add_book.geometry('450x300')
        text = tk.Label(root_add_book, text="管理书籍", bg="yellow", fg="red", font=('Times', 20, 'bold italic'))
        label1 = tk.Label(root_add_book, text="书号：")
        entry1 = tk.Entry(root_add_book)
        label2 = tk.Label(root_add_book, text="书名：")
        entry2 = tk.Entry(root_add_book)
        label3 = tk.Label(root_add_book, text="作者：")
        entry3 = tk.Entry(root_add_book)
        label4 = tk.Label(root_add_book, text="数量：")
        entry4 = tk.Entry(root_add_book)
        button1 = tk.Button(root_add_book, text="添加", command=add)
        button2 = tk.Button(root_add_book, text="修改", command=modeify)
        button3 = tk.Button(root_add_book, text="删除", command=delete)
        text.pack()
        label1.pack()
        entry1.pack()
        label2.pack()
        entry2.pack()
        label3.pack()
        entry3.pack()
        label4.pack()
        entry4.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        root_add_book.mainloop()
    def add_student():
        # 进行修改学生操作
        def add():
            sno = entry1.get()
            sname = entry2.get()
            sgender = entry3.get()
            sdepart = entry4.get()
            cursor = conn.cursor()
            # 使用 execute()方法执行 SQL 查询
            # 增加student
            sql = "insert into student (sno, sname, sgender,sdepart ) VALUES(" + str(sno) + ", '" + str(sname) + "','" + str(
                sgender) +"', '" + str(sdepart) + "');"
            print(sql)
            cursor.execute(sql)
            # 增加student_borrow
            sql = "insert into student_borrow (sno, snum ) VALUES(" + str(sno) + ", "+ "0);"
            print(sql)
            cursor.execute(sql)
            print("ok")
        def modeify():
            sno = entry1.get()
            sname = entry2.get()
            sgender = entry3.get()
            sdepart = entry4.get()
            cursor = conn.cursor()
            # 使用 execute()方法执行 SQL 查询
            # 删除student
            sql = 'delete from student where sno = ' +str(sno) + ';'
            print(sql)
            cursor.execute(sql)
            #增加student
            sql = "insert into student (sno, sname, sgender,sdepart ) VALUES(" + str(sno) + ", '" + str(sname) + "','" + str(
                sgender) +"', '" + str(sdepart) + "');"
            print(sql)
            cursor.execute(sql)
            conn.commit()
            print("ok")
        def delete():
            sno = entry1.get()
            sname = entry2.get()
            sgender = entry3.get()
            sdepart = entry4.get()
            cursor = conn.cursor()
            # 使用 execute()方法执行 SQL 查询
            # 删除student
            sql = 'delete from student where sno = ' + str(sno) + ';'
            print(sql)
            cursor.execute(sql)
            # 删除student_borrow
            sql = 'delete from student_borrow where sno = ' + str(sno) + ';'
            print(sql)
            cursor.execute(sql)
            # 删除student_book
            sql = 'delete from student_book where sno = ' + str(sno) + ';'
            conn.commit()
            print("ok")
        root_add_student = tk.Tk()
        root_add_student.title('图书馆管理系统')
        root_add_student.geometry('450x300')
        text = tk.Label(root_add_student, text="管理学生", bg="yellow", fg="red", font=('Times', 20, 'bold italic'))
        label1 = tk.Label(root_add_student, text="学号：")
        entry1 = tk.Entry(root_add_student)
        label2 = tk.Label(root_add_student, text="姓名：")
        entry2 = tk.Entry(root_add_student)
        label3 = tk.Label(root_add_student, text="性别：")
        entry3 = tk.Entry(root_add_student)
        label4 = tk.Label(root_add_student, text="专业：")
        entry4 = tk.Entry(root_add_student)
        button1 = tk.Button(root_add_student, text="增加", command=add)
        button2 = tk.Button(root_add_student, text="修改", command=modeify)
        text.pack()
        label1.pack()
        entry1.pack()
        label2.pack()
        entry2.pack()
        label3.pack()
        entry3.pack()
        label4.pack()
        entry4.pack()
        button1.pack()
        button2.pack()
        root_add_student.mainloop()
    def query_book():
        # 进行查询图书操作操作
        def submmit():
            bno = entry1.get()
            bname = entry2.get()
            cursor = conn.cursor()
            # 使用 execute()方法执行 SQL 查询
            # 查询book
            sql = "select * from book where bno = " + str(bno) + ";"
            print(sql)
            cursor.execute(sql)
            data = cursor.fetchall()
            print(data)
            # 查询book_borrow
            sql = "select * from book_borrow where bno = " + str(bno) + ";"
            print(sql)
            cursor.execute(sql)
            data1 = cursor.fetchall()
            print(data1)
            if data[0][1] == bname :
                result = "书号: " + str(data[0][0])+"\n"
                result = result + "书名: "+ str(data[0][1])+"\n"
                result = result + "作者: " + str(data[0][2]) + "\n"
                result = result + "馆存个数: " + str(data1[0][2]) + "\n"
                result = result + "现存个数: " + str(data1[0][3]) + "\n"
                if data1[0][2] !=data1[0][3]:
                    result = result + "借阅人: \n"
                    sql = "select * from student_book where bno = " + str(bno) + ";"
                    print(sql)
                    cursor.execute(sql)
                    data1 = cursor.fetchall()
                    for t in data1:
                        result = result + "学号: " + str(t[1]) + "   借阅时间: "+str(t[2]) + "\n"
            else:
                result = '请确定书名或编号是否正确'
            label.config(text=result)
            print("ok")
        root_query_book = tk.Tk()
        root_query_book.title('图书馆管理系统')
        root_query_book.geometry('450x300')
        label = tk.Label(root_query_book)
        text = tk.Label(root_query_book, text="查询书籍", bg="yellow", fg="red", font=('Times', 20, 'bold italic'))
        label1 = tk.Label(root_query_book, text="书号：")
        entry1 = tk.Entry(root_query_book)
        label2 = tk.Label(root_query_book, text="书名：")
        entry2 = tk.Entry(root_query_book)
        button = tk.Button(root_query_book, text="执行", command=submmit)
        text.pack()
        label1.pack()
        entry1.pack()
        label2.pack()
        entry2.pack()
        button.pack()
        label.pack()
        root_query_book.mainloop()
    def query_student():
        # 进行查询学生操作操作
        def submmit():
            sno = entry1.get()
            sname = entry2.get()
            cursor = conn.cursor()
            # 使用 execute()方法执行 SQL 查询
            # 查询student
            sql = "select * from student where sno = " + str(sno) + ";"
            print(sql)
            cursor.execute(sql)
            data = cursor.fetchall()
            print(data)
            #查询student_borrow
            sql = "select * from student_borrow where sno = " + str(sno) + ";"
            print(sql)
            cursor.execute(sql)
            data1 = cursor.fetchall()
            print(data1)
            if data[0][1] == sname :
                result = "学号: " + str(data[0][0])+"\n"
                result = result + "姓名: "+ str(data[0][1])+"\n"
                result = result + "性别: " + str(data[0][2]) + "\n"
                result = result + "专业: " + str(data[0][3]) + "\n"
                if data1[0][1] != 0:
                    result = result + "借阅记录: \n"
                    sql = "select * from student_book where sno = " + str(sno) + ";"
                    print(sql)
                    cursor.execute(sql)
                    data1 = cursor.fetchall()
                    for t in data1:
                        result = result + "借阅时间: "+str(t[2]) + "\n"
            else:
                result = '请确定姓名或学号是否正确'
            label.config(text=result)
            print("ok")
        root_query_student = tk.Tk()
        root_query_student.title('图书馆管理系统')
        root_query_student.geometry('450x300')
        label = tk.Label(root_query_student)
        text = tk.Label(root_query_student, text="查询学生", bg="yellow", fg="red", font=('Times', 20, 'bold italic'))
        label1 = tk.Label(root_query_student, text="学号：")
        entry1 = tk.Entry(root_query_student)
        label2 = tk.Label(root_query_student, text="姓名：")
        entry2 = tk.Entry(root_query_student)
        button = tk.Button(root_query_student, text="执行", command=submmit)
        text.pack()
        label1.pack()
        entry1.pack()
        label2.pack()
        entry2.pack()
        button.pack()
        label.pack()
        root_query_student.mainloop()
    #界面设置
    root_window = tk.Tk()
    root_window.title('图书馆管理系统')
    root_window.geometry('450x300')
    text = tk.Label(root_window, text="图书馆管理系统", bg="yellow", fg="red", font=('Times', 20, 'bold italic'))
    text.pack()
    #功能键
    button1 = tk.Button(root_register, text="借   书", command=borrow)
    button1.pack()
    button2 = tk.Button(root_register, text="还   书", command=reback)
    button2.pack()
    button3 = tk.Button(root_register, text="管理书籍", command=add_book)
    button3.pack()
    button4 = tk.Button(root_register, text="管理学生", command=add_student)
    button4.pack()
    button5 = tk.Button(root_register, text="查询书籍", command=query_book)
    button5.pack()
    button6 = tk.Button(root_register, text="查询学生", command=query_student)
    button6.pack()
    root_window.mainloop()
def init_register_GUI():
    def check():
        user = entry1.get()
        pw = entry2.get()
        user = "root"
        pw = "yyh20021024"
        try:
            global conn
            conn = pymysql.connect(
                host='localhost',
                port=3306,
                user=user,
                password=pw,
                database='library',
                charset='utf8'
            )
            print("ok")
            root_register.destroy()
        except Exception as e:
            logging.exception(e)
    root_register = tk.Tk()
    root_register.title('图书馆管理系统')
    root_register.geometry('450x300')
    text = tk.Label(root_register, text="图书馆管理系统", bg="yellow", fg="red", font=('Times', 20, 'bold italic'))
    text.pack()
    #用户信息
    label1 = tk.Label(root_register, text="账号：")
    label2 = tk.Label(root_register, text="密码：")
    var1 = tk.StringVar()
    var2 = tk.StringVar()
    entry1 = tk.Entry(root_register,textvariable=var1)
    entry2 = tk.Entry(root_register,textvariable=var2)
    # 登入按钮
    button = tk.Button(root_register, text="登入", command=check)
    button.pack(side="bottom")
    label1.pack()
    label2.pack()
    entry1.pack()
    entry2.pack()
    root_register.mainloop()
def StartGui():
    init_register_GUI()
    init_main_GUI()

if __name__ == '__main__':
    StartGui()
