"""
@file: wallet
@author: initsysctrl
@license: Apache Licence 
@contact: initsysctrl@163.com
@time: 2018/11/1 11:01 AM
@describe: 
"""
import hashlib
import secrets
from binascii import hexlify, unhexlify

import ecdsa.ecdsa

import crypto

"""
类：钱包信息
"""


class Wallet(object):
    def __init__(self, privatea_key_hex=None, base58private=None, wifprivate=None, anyword=None):
        if privatea_key_hex is not None:
            self.private_key = privatea_key_hex
        elif wifprivate is not None:
            self.private_key = crypto.base58_check_decode(base58private)
        elif anyword is not None:
            self.private_key = hashlib.sha256(bytes(anyword, 'utf-8')).digest().hex()

        self.private_key = hex(secrets.randbits(256))[2:] if privatea_key_hex is None else privatea_key_hex
        print(self.private_key)
        public_key = self._creat_publickey(self.private_key)
        self.public_key_compress = public_key[0]
        self.public_key_uncompress = public_key[1]
        self.address = self._creat_address(self.public_key_compress)

    def __str__(self):
        return self.__dict__

    # 私钥生成公钥
    @classmethod
    def _creat_publickey(cls, private_key_hex: str) -> tuple:
        """

        :param private_key_hex: 私钥 hex格式的
        :return: 压缩和未被压缩的公钥
        """
        secret = unhexlify(private_key_hex)
        order = ecdsa.SigningKey.from_string(secret, curve=ecdsa.SECP256k1).curve.generator.order()
        p = ecdsa.SigningKey.from_string(secret, curve=ecdsa.SECP256k1).verifying_key.pubkey.point
        x_str = ecdsa.util.number_to_string(p.x(), order)
        y_str = ecdsa.util.number_to_string(p.y(), order)
        compressed = (bytes(chr(2 + (p.y() & 1)), 'ascii') + x_str).hex()
        uncompressed = (bytes(chr(4), 'ascii') + x_str + y_str).hex()
        p = 115792089237316195423570985008687907853269984665640564039457584007908834671663
        x = int(x_str.hex(), 16)
        print('x=', int(x_str.hex(), 16))
        y = int(y_str.hex(), 16)
        z = (x ** 3 + 7 - y ** 2) % p
        print('x=', x)
        print('y=', y)
        print('z=', z)
        print('compressed = ', compressed)
        print('uncompressed = ', uncompressed)
        return compressed, uncompressed

    # 由公钥生成地址
    @classmethod
    def _creat_address(cls, public_key: str) -> str:
        """

        :param public_key: 公钥
        :return:
        """
        pkbin = unhexlify(public_key)
        addressbin = crypto.ripemd160(hexlify(hashlib.sha256(pkbin).digest()))
        address = crypto.base58_check_encode('0x00', addressbin.hex())
        print('address = ', address)
        return address

    # 导出base58格式的私钥
    def export_base58_privatekey(self) -> str:
        return crypto.base58encode(self.private_key)

    # 导出WIF格式的私钥
    def export_wif_privatekey(self) -> str:
        return crypto.base58_check_encode('0x80', self.private_key)

    # 导出压缩WIF格式的私钥
    def export_compress_privatekey(self) -> str:
        return crypto.base58_check_encode(0x80, self.private_key + '01')


if __name__ == '__main__':
    wallet = Wallet(anyword='cnm li xiao lai')
    # wallet = Wallet(hashlib.sha256(bytes('Hello World', 'utf-8')).digest().hex())
    print('wallet=', wallet.__str__())
