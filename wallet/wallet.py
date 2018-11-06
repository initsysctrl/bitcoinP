"""
@file: wallet
@author: initsysctrl
@license: Apache Licence 
@contact: initsysctrl@163.com
@time: 2018/11/1 11:01 AM
@describe: 
"""
import bitcoin
import secrets


class Wallet:
    def __init__(self, privatea_key=None):
        if privatea_key is None:
            raise ValueError('privatea_key==null')

        self.private_key = privatea_key
        if privatea_key is not None:
            self.public_key = bitcoin.privkey_to_pubkey(privatea_key)
            self.address = bitcoin.privkey_to_address(privatea_key)
        else:
            self.public_key = None
            self.address = None


def generate_wallet() -> Wallet:
    """
    :rtype: 新的比特币钱包
    """
    # 1. 随机数

    orige_private_key = bitcoin.random_key()  # getStartKey();
    print("orige_private_key=", orige_private_key)
    # 私钥
    dec_privatekey = bitcoin.decode_privkey(orige_private_key, 'hex')
    print("decPrivatekey=", dec_privatekey)
    secrets.randbits(256)
    return Wallet(privatea_key=dec_privatekey)


if __name__ == '__main__':
    w = Wallet()
    print(w.__dict__)
    w = generate_wallet()
    print(w.__dict__)
