# -*- coding: utf-8 -*-
import xlwt
import pymysql


def mysql_execute():
    # 连接 mysql 数据库
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db="student_data", charset="utf8")
    curs = conn.cursor()
    sql = '''select * from students'''
    curs.execute(sql)
    rows = curs.fetchall()

    w = xlwt.Workbook()
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = u"微软雅黑"
    style.font = font  # 为样式设置字体
    ws = w.add_sheet(u"学生信息", cell_overwrite_ok=True)

    # 将 title 作为 Excel 的列名
    title = u"id, 姓名, 年龄, 学号"
    title = title.split(",")
    for i in range(len(title)):
        ws.write(0, i, title[i], style)
    #  # 开始写入数据库查询到的数据
    for i in range(len(rows)):
        row = rows[i]
        for j in range(len(row)):
            if row[j]:
                item = row[j]
                ws.write(i + 1, j, item, style)

    # 写文件完成，开始保存xls文件
    path = 'student.xls'
    w.save(path)
    conn.close()
    return path


if __name__ == '__main__':
    path = mysql_execute()
