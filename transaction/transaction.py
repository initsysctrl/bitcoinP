"""
@file: transaction
@author: initsysctrl
@license: Apache Licence 
@contact: initsysctrl@163.com
@time: 2018/11/5 5:29 PM
@describe: 
"""

import time

# 版本号
VERSION_NUMBER = 0


class Transction:
    class Input:
        pass

    class Outputs:
        pass

    def __init__(self, _inputs=(), _outputs=()):
        self.version = VERSION_NUMBER
        self.input_count = len(_inputs)
        self.inputs = _inputs
        self.output_count = len(_outputs)
        self.outputs = _outputs
        self.timestamp = time.time_ns()

    def __str__(self) -> str:
        return str(self.__dict__)


if __name__ == '__main__':
    t = Transction()
    print(t)
    pass
