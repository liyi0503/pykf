"""
==========================
Author:李轶
Time:2022/6/7 2:50 下午
Project: pykf
=========================
"""
from common.mysqlUtil import MysqlUtil
from student.studentBean import StudentBean


class ManageStudent:

    def __init__(self):
        self.util = MysqlUtil()

    def manage(self):
        while True:
            self.show()
            num = int(input('请输入有效选项'))
            if num == 1:
                # 查询所有信息
                self.selectAll()
            elif num == 2:
                self.selectByName()
            elif num == 3:
                self.add()

            elif num == 4:
                self.deleteByName()
            elif num == 5:
                self.updateByName()
            elif num == 6:
                break

    def show(self):
        print('-----------有效选项-----------')
        print('1:查询所有信息')
        print('2:根据姓名查询信息')
        print('3:添加信息')
        print('4:根据姓名修改删除信息')
        print('5:根据姓名修改信息')
        print('6:退出系统')

    def selectAll(self):
        result = self.util.query('select * from student')
        for r in result:
            s = StudentBean(r['name'], r['sex'], r['age'])
            print(s)

    def selectByName(self):
        pass

    def add(self):
        pass

    def deleteByName(self):
        pass

    def updateByName(self):
        pass
