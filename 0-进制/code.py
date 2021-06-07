r1 = '正'
r0 = '反'


def decode(enc=None):
    if not enc:
        enc = input('请输入待解码的内容：')
    out = enc.replace(r1, '1')
    out = out.replace(r0, '0')
    out = int(out, 2)
    print(out)


def encode(dec=None):
    if not dec:
        dec = input('请输入需编码的数字：')
    dec = bin(int(dec))[2:]
    dec = dec.replace('1', r1)
    dec = dec.replace('0', r0)
    print(dec)


if __name__ == '__main__':
    decode()
