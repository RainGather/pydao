r1 = '正'
r0 = '反'


def decode(enc=None):
    if not enc:
        enc = input('请输入待解码的内容：')
    out = ''
    c = 0
    i = 0
    for e in enc:
        if e == r1:
            c = c * 2 + 1
        elif e == r0:
            c *= 2
        else:
            continue
        i += 1
        if i % 24 == 0:
            out += chr(c)
            c = 0
            i = 0
    print(out)


def encode(dec=None):
    if not dec:
        dec = input('请输入需编码的文字：')
    out = ''
    for i in dec:
        c = ord(i)
        t = [r0 for _ in range(24)]
        for ti, j in enumerate(bin(c)[2:][::-1]):
            if j == '1':
                t[24 - 1 - ti] = r1
        out += ''.join(t)
    print(out)


if __name__ == '__main__':
    decode()
