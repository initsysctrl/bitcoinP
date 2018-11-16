"""
@file: markle
@author: initsysctrl
@license: Apache Licence 
@contact: initsysctrl@163.com
@time: 2018/11/16 5:33 PM
@describe: 默克尔数
"""


class Markle:
    def __int__(self, datas):
        if datas is None:
            raise TypeError('datas is None!')
        if not isinstance(datas, tuple):
            raise TypeError('datas type only is tuple or list')
        self.datas = datas

    @classmethod
    def get_root(cls):
        pass

    def get_node(self):
        pass


if __name__ == '__main__':
    pass
