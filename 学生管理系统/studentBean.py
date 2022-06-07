"""
==========================
Author:李轶
Time:2022/6/7 2:35 下午
Project: pykf
=========================
"""


class StudentBean:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def __str__(self):
        return f'{self.name},{self.sex},{self.age}'















if __name__ == '__main__':
    s = StudentBean('叮当', '女', '2')
    print(s)
