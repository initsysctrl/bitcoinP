"""
@file: crypto
@author: initsysctrl
@license: Apache Licence 
@contact: initsysctrl@163.com
@time: 2018/11/12 8:22 AM
@describe: 
"""
import hashlib
from binascii import hexlify, unhexlify

Base58Alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def base58decode(base58data) -> str:
    """
    base58 解码
    :param base58data:
    :return:
    """
    result = 0

    for d in base58data:
        char_index = Base58Alphabet.find(d)

        result = result * len(Base58Alphabet)
        result = result + char_index

    decoded = hex(result)

    return decoded


def base58encode(hexstring):
    result = []
    x = int(hexstring, 16)
    base = 58

    zero = 0

    while x != zero:
        x, mod = divmod(x, base)
        result.append(Base58Alphabet[mod])
    return "".join(result[::-1])


def ripemd160(s):
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(unhexlify(s))
    return ripemd160.digest()


# https://steemitimages.com/0x0/https://steemitimages.com/DQmR6osyE59XryeuQyffbf74WoMcN9vcMs8xYnQ9qDMH3tP/image.png
def base58_check_encode(version, payload):
    s = ('%.2x' % version) + payload
    print('s=', s)
    dh = doublesha256(s)
    print('double hash s =', dh.hex())
    checksum = dh[:4]
    print('checksum=', checksum.hex())
    result = s + hexlify(checksum).decode('ascii')
    print('result=', result)
    return base58encode(result)
    # s = version + payload
    # checksum = doublesha256(s)[:4]
    # result = s + hexlify(checksum).decode('ascii')
    # return base58encode(result)


def doublesha256(s):
    h1 = hashlib.sha256(s.encode()).digest().hex()
    # print('h1=', h1)
    h2 = hashlib.sha256(h1.encode()).digest()
    # print('h2=', h2.hex())
    return h2


def base58_check_decode(s):
    s = unhexlify(base58decode(s))
    dec = hexlify(s[:-4]).decode('ascii')
    checksum = doublesha256(dec)[:4]
    assert (s[-4:] == checksum)
    return dec[2:]
