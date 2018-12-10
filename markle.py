"""
@file: markle
@author: initsysctrl
@license: Apache Licence 
@contact: initsysctrl@163.com
@time: 2018/11/16 5:33 PM
@describe: 默克尔数
"""


class MarkleTree:
    def __init__(self, dates):
        if dates is None:
            raise TypeError('datas is None!')
        if not isinstance(dates, tuple):
            raise TypeError('datas type only is tuple or list')
        self.datas = datas

    def __str__(self) -> str:
        return str(self.__dict__)


if __name__ == '__main__':
    datas = ('a', 'b', 'c', 'd', 'e')
    m = MarkleTree(datas)
    print(m.datas)
    # m.get_root()
    pass
