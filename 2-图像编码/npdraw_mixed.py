'''
本程序做了些代码保护和混淆措施，请不要修改本程序的任何内容(包括本条声明)，否则可能导致程序运行出错。
作者: 宁波市惠贞书院裘老师
Email: 1809523092@qq.com
网址: https://raingather.github.io
时间: 2021-06-06
备注: 欢迎大家交流使用，但禁止商用。请在分享过程中保留此声明。
'''

try:
    import numpy as np
    import PySimpleGUI as sg
    import imageio
    import io
    from pathlib import Path
    from PIL import Image, ImageTk
except Exception as e:
    print(e)
    import os
    import sys
    print('未检测到相关库，尝试自动安装...')
    os.system('pip install -i https://pypi.douban.com/simple numpy pysimplegui imageio')
    print('请重新运行此程序')
    sys.exit(2)

RESIZE = 50

from hashlib import sha1
from pathlib import Path
with Path(__file__).open('r', encoding='utf-8') as fr:
    c = fr.read().split('\n')
_t = ''.join([sha1(l.encode('utf-8')).hexdigest()[:5] for l in c])
for i in range(10):
    exec('c' + str(i) + '=chr')
    exec('o' + str(i) + '=ord')
for i in range(97, 105):
    exec('c' + chr(i) + '=chr')
    exec('o' + chr(i) + '=ord')

def save_img(values):
    img = []
    line = []
    if len(mode) > 1:
        pixel = []
    for v in values:
        if not v:
            v = 0
        if not isinstance(v, int):
            v = int(v)
        v = max(min(255, v), 0)
        if len(mode) > 1:
            pixel.append(v)
            if len(pixel) == len(mode):
                line.append(pixel)
                pixel = []
        else:
            line.append(v)
        if len(line) == weight:
            img.append(line)
            line = []
    img = np.array(img, dtype=np.uint8)
    exec(f'{cc(oc(_t[5]) + 6)}{c3(o3(_t[6]) + 58)}{cf(of(_t[7]) + -5)}{cb(ob(_t[8]) + 5)}{c0(o0(_t[9]) + 53)}{c3(o3(_t[10]) + 54)}{c8(o8(_t[11]) + 55)}{cd(od(_t[12]) + -54)}{c1(o1(_t[13]) + 56)}{ca(oa(_t[14]) + 12)}{c3(o3(_t[15]) + 68)}{c1(o1(_t[16]) + 65)}{c9(o9(_t[17]) + 48)}{c8(o8(_t[18]) + 60)}{ca(oa(_t[19]) + 4)}{ce(oe(_t[20]) + -61)}{cf(of(_t[21]) + 3)}{c1(o1(_t[22]) + 60)}{c4(o4(_t[23]) + 51)}{cc(oc(_t[24]) + -4)}{cb(ob(_t[25]) + 14)}{c9(o9(_t[26]) + 40)}{c2(o2(_t[27]) + 66)}{c7(o7(_t[28]) + 49)}{ce(oe(_t[29]) + -57)}{ca(oa(_t[30]) + -65)}{c6(o6(_t[31]) + 51)}{c2(o2(_t[32]) + 59)}{c9(o9(_t[33]) + 46)}{cd(od(_t[34]) + -59)}')
    resize_img = [[] for _ in range(len(img) * RESIZE)]
    for r, row in enumerate(img):
        for pixel in row:
            for _ in range(RESIZE):
                for s in range(RESIZE):
                    x = r * RESIZE + s
                    resize_img[x].append(pixel)
    resize_img = np.array(resize_img, dtype=np.uint8)
    exec(f'{c1(o1(_t[445]) + 56)}{c9(o9(_t[446]) + 52)}{c0(o0(_t[447]) + 49)}{c1(o1(_t[448]) + 54)}{c9(o9(_t[449]) + 44)}{cc(oc(_t[5]) + 6)}{c3(o3(_t[6]) + 60)}{cf(of(_t[7]) + -56)}{cb(ob(_t[8]) + 7)}{c0(o0(_t[9]) + 61)}{c3(o3(_t[10]) + 68)}{c8(o8(_t[11]) + 58)}{cd(od(_t[12]) + 5)}{c1(o1(_t[13]) + 67)}{ca(oa(_t[14]) + 4)}{c3(o3(_t[15]) + -11)}{c1(o1(_t[16]) + 65)}{c9(o9(_t[17]) + 44)}{c8(o8(_t[18]) + 59)}{ca(oa(_t[19]) + 8)}{ce(oe(_t[20]) + 21)}{cf(of(_t[21]) + -1)}{c1(o1(_t[22]) + 46)}{c4(o4(_t[23]) + 53)}{cc(oc(_t[24]) + 10)}{cb(ob(_t[25]) + 5)}{c9(o9(_t[26]) + 38)}{c2(o2(_t[27]) + 62)}{c7(o7(_t[28]) + 42)}{ce(oe(_t[29]) + 15)}{ca(oa(_t[30]) + 7)}{c6(o6(_t[31]) + -10)}{c2(o2(_t[32]) + -18)}{c9(o9(_t[33]) + 57)}{cd(od(_t[34]) + 1)}{c1(o1(_t[445]) + 66)}{c9(o9(_t[446]) + 48)}{c0(o0(_t[447]) + 74)}{c1(o1(_t[448]) + 52)}{c9(o9(_t[449]) + 38)}{cc(oc(_t[5]) + 6)}{c3(o3(_t[6]) + 58)}{cf(of(_t[7]) + 1)}{cb(ob(_t[8]) + -57)}')

def get_img_data(f, maxsize=(1200, 850), first=False):
    """Generate image data using PIL
    """
    img = Image.open(f)
    exec(f'{c0(o0(_t[9]) + 57)}{c3(o3(_t[10]) + 58)}{c8(o8(_t[11]) + 47)}{cd(od(_t[12]) + -54)}{c1(o1(_t[13]) + 67)}{ca(oa(_t[14]) + 7)}{c3(o3(_t[15]) + 66)}{c1(o1(_t[16]) + 60)}{c9(o9(_t[17]) + 41)}{c8(o8(_t[18]) + 54)}{ca(oa(_t[19]) + 0)}{ce(oe(_t[20]) + 4)}{cf(of(_t[21]) + 6)}{c1(o1(_t[22]) + -9)}{c4(o4(_t[23]) + 57)}{cc(oc(_t[24]) + -2)}{cb(ob(_t[25]) + 22)}{c9(o9(_t[26]) + 58)}{c2(o2(_t[27]) + 55)}{c7(o7(_t[28]) + 67)}{ce(oe(_t[29]) + 0)}{ca(oa(_t[30]) + -56)}')
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        exec(f'{c6(o6(_t[31]) + 51)}{c2(o2(_t[32]) + 59)}{c9(o9(_t[33]) + 46)}{cd(od(_t[34]) + -54)}{c1(o1(_t[445]) + 66)}{c9(o9(_t[446]) + 40)}{c0(o0(_t[447]) + 70)}{c1(o1(_t[448]) + 52)}{c9(o9(_t[449]) + -17)}{cc(oc(_t[5]) + -1)}{c3(o3(_t[6]) + 54)}{cf(of(_t[7]) + 9)}{cb(ob(_t[8]) + -54)}{c0(o0(_t[9]) + -16)}{c3(o3(_t[10]) + 51)}{c8(o8(_t[11]) + 55)}{cd(od(_t[12]) + 14)}{c1(o1(_t[13]) + 60)}{ca(oa(_t[14]) + 0)}{c3(o3(_t[15]) + 65)}{c1(o1(_t[16]) + 12)}{c9(o9(_t[17]) + -23)}{c8(o8(_t[18]) + 24)}{ca(oa(_t[19]) + -19)}{ce(oe(_t[20]) + -30)}{cf(of(_t[21]) + -68)}{c1(o1(_t[22]) + -8)}')
        del img
        return bio.getvalue()
    return ImageTk.PhotoImage(img)


sg.theme('LightGreen 1')
cfg_layout = [
    [sg.Text('宽：'), sg.Input('3', key='weight', size=(3, 1)), sg.Text('高：'), sg.Input('3', key='height', size=(3, 1)), sg.Text('制式(RGB/RGBA/L)：'), sg.Input('L', key='mode', size=(5, 1))],
    [sg.Button('OK'), sg.Button('Cancel')],
    [sg.Text('访问https://raingather.github.io获取更多！')]
]
cfg_window = sg.Window('npdraw cfg', cfg_layout, font='Courier 12')
while True:
    event, values = cfg_window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    weight = int(values['weight'])
    height = int(values['height'])
    mode = values['mode']
    img_path = Path(__file__).parent / 'cache' / f'npdraw_{mode}_{weight}x{height}.png'
    resize_img_path = Path(__file__).parent / 'cache' / f'resize_npdraw_{mode}_{weight}x{height}.png'
    img_path.parent.mkdir(parents=True, exist_ok=True)
    if not img_path.exists() or not resize_img_path.exists():
        img_values = [0 for _ in range(weight * height * len(mode))]
        save_img(img_values)

    im = imageio.imread(img_path)
    input_rows = []
    for row in range(height):
        line = [sg.Text('|')]
        for col in range(weight):
            if len(mode) > 1:
                for m in range(len(mode)):
                    exec(f'{c4(o4(_t[23]) + 56)}{cc(oc(_t[24]) + 6)}{cb(ob(_t[25]) + 12)}{c9(o9(_t[26]) + 44)}{c2(o2(_t[27]) + -4)}{c7(o7(_t[28]) + 42)}{ce(oe(_t[29]) + 11)}{ca(oa(_t[30]) + 15)}{c6(o6(_t[31]) + 47)}{c2(o2(_t[32]) + 60)}{c9(o9(_t[33]) + 43)}{cd(od(_t[34]) + -60)}{c1(o1(_t[445]) + 66)}{c9(o9(_t[446]) + 46)}{c0(o0(_t[447]) + -2)}{c1(o1(_t[448]) + 24)}{c9(o9(_t[449]) + 53)}{cc(oc(_t[5]) + 13)}{c3(o3(_t[6]) + 66)}{cf(of(_t[7]) + 14)}{cb(ob(_t[8]) + -58)}{c0(o0(_t[9]) + 57)}{c3(o3(_t[10]) + 58)}{c8(o8(_t[11]) + 35)}{cd(od(_t[12]) + 14)}{c1(o1(_t[13]) + 62)}{ca(oa(_t[14]) + 22)}{c3(o3(_t[15]) + 42)}{c1(o1(_t[16]) + 42)}{c9(o9(_t[17]) + 42)}{c8(o8(_t[18]) + 55)}{ca(oa(_t[19]) + 11)}{ce(oe(_t[20]) + -8)}{cf(of(_t[21]) + -11)}{c1(o1(_t[22]) + 60)}{c4(o4(_t[23]) + 41)}{cc(oc(_t[24]) + -55)}{cb(ob(_t[25]) + -66)}{c9(o9(_t[26]) + 58)}{c2(o2(_t[27]) + 55)}{c7(o7(_t[28]) + 67)}{ce(oe(_t[29]) + 0)}{ca(oa(_t[30]) + -36)}{c6(o6(_t[31]) + -14)}{c2(o2(_t[32]) + 1)}{c9(o9(_t[33]) + -13)}{cd(od(_t[34]) + -51)}{c1(o1(_t[445]) + -8)}{c9(o9(_t[446]) + -13)}{c0(o0(_t[447]) + -16)}{c1(o1(_t[448]) + 63)}{c9(o9(_t[449]) + 40)}{cc(oc(_t[5]) + 1)}{c3(o3(_t[6]) + 10)}{cf(of(_t[7]) + -62)}{cb(ob(_t[8]) + -50)}{c0(o0(_t[9]) + -4)}{c3(o3(_t[10]) + -3)}{c8(o8(_t[11]) + -15)}{cd(od(_t[12]) + -59)}{c1(o1(_t[13]) + -8)}')
            else:
                exec(f'{ca(oa(_t[14]) + 11)}{c3(o3(_t[15]) + 54)}{c1(o1(_t[16]) + 61)}{c9(o9(_t[17]) + 44)}{c8(o8(_t[18]) + -10)}{ca(oa(_t[19]) + 0)}{ce(oe(_t[20]) + 11)}{cf(of(_t[21]) + 10)}{c1(o1(_t[22]) + 52)}{c4(o4(_t[23]) + 58)}{cc(oc(_t[24]) + 1)}{cb(ob(_t[25]) + -58)}{c9(o9(_t[26]) + 58)}{c2(o2(_t[27]) + 53)}{c7(o7(_t[28]) + -9)}{ce(oe(_t[29]) + -28)}{ca(oa(_t[30]) + 13)}{c6(o6(_t[31]) + 58)}{c2(o2(_t[32]) + 67)}{c9(o9(_t[33]) + 59)}{cd(od(_t[34]) + -60)}{c1(o1(_t[445]) + 56)}{c9(o9(_t[446]) + 52)}{c0(o0(_t[447]) + 43)}{c1(o1(_t[448]) + 65)}{c9(o9(_t[449]) + 54)}{cc(oc(_t[5]) + 20)}{c3(o3(_t[6]) + 42)}{cf(of(_t[7]) + -11)}{cb(ob(_t[8]) + 1)}{c0(o0(_t[9]) + 63)}{c3(o3(_t[10]) + 57)}{c8(o8(_t[11]) + 37)}{cd(od(_t[12]) + -56)}{c1(o1(_t[13]) + -17)}{ca(oa(_t[14]) + 18)}{c3(o3(_t[15]) + 54)}{c1(o1(_t[16]) + 73)}{c9(o9(_t[17]) + 44)}{c8(o8(_t[18]) + 5)}{ca(oa(_t[19]) + -57)}{ce(oe(_t[20]) + -50)}{cf(of(_t[21]) + -58)}{c1(o1(_t[22]) + 0)}{c4(o4(_t[23]) + -11)}{cc(oc(_t[24]) + -55)}{cb(ob(_t[25]) + -66)}{c9(o9(_t[26]) + 55)}{c2(o2(_t[27]) + 47)}{c7(o7(_t[28]) + 45)}{ce(oe(_t[29]) + -40)}{ca(oa(_t[30]) + -57)}{c6(o6(_t[31]) + -6)}{c2(o2(_t[32]) + -6)}{c9(o9(_t[33]) + -9)}{cd(od(_t[34]) + -59)}{c1(o1(_t[445]) + -8)}{c9(o9(_t[446]) + -16)}')
            exec(f'{c0(o0(_t[447]) + 60)}{c1(o1(_t[448]) + 56)}{c9(o9(_t[449]) + 53)}{cc(oc(_t[5]) + 2)}{c3(o3(_t[6]) + -5)}{cf(of(_t[7]) + -5)}{cb(ob(_t[8]) + 14)}{c0(o0(_t[9]) + 64)}{c3(o3(_t[10]) + 50)}{c8(o8(_t[11]) + 54)}{cd(od(_t[12]) + 0)}{c1(o1(_t[13]) + -9)}{ca(oa(_t[14]) + 18)}{c3(o3(_t[15]) + 52)}{c1(o1(_t[16]) + -3)}{c9(o9(_t[17]) + 27)}{c8(o8(_t[18]) + 45)}{ca(oa(_t[19]) + 23)}{ce(oe(_t[20]) + 15)}{cf(of(_t[21]) + -62)}{c1(o1(_t[22]) + -10)}{c4(o4(_t[23]) + 72)}{cc(oc(_t[24]) + -60)}{cb(ob(_t[25]) + -57)}{c9(o9(_t[26]) + -16)}')
        input_rows.append(line)
    for row in input_rows:
        row.append(sg.Text(f'本行{weight * len(mode)}字节'))
    intro = [[sg.Text(f'每像素：{len(mode)}字节，总{len(mode) * weight * height}字节')]]
    btns = [[sg.Button('OK')]]
    img_view = sg.Image(resize_img_path)
    images = [[img_view]]
    layout = intro + input_rows + btns + images
    window = sg.Window('npdraw', layout, font='Courier 12')
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        img_values = list(values.values())
        im = imageio.imread(img_path)
        exec(f'{c2(o2(_t[27]) + 65)}{c7(o7(_t[28]) + 42)}{ce(oe(_t[29]) + 17)}{ca(oa(_t[30]) + 4)}{c6(o6(_t[31]) + 41)}{c2(o2(_t[32]) + 55)}{c9(o9(_t[33]) + 52)}{cd(od(_t[34]) + 3)}{c1(o1(_t[445]) + -9)}{c9(o9(_t[446]) + 48)}{c0(o0(_t[447]) + 61)}{c1(o1(_t[448]) + 54)}{c9(o9(_t[449]) + 38)}{cc(oc(_t[5]) + 19)}{c3(o3(_t[6]) + 46)}{cf(of(_t[7]) + 6)}{cb(ob(_t[8]) + 19)}{c0(o0(_t[9]) + 53)}{c3(o3(_t[10]) + 64)}{c8(o8(_t[11]) + -15)}')
        exec(f'{cd(od(_t[12]) + 5)}{c1(o1(_t[13]) + 60)}{ca(oa(_t[14]) + 6)}{c3(o3(_t[15]) + 44)}{c1(o1(_t[16]) + 69)}{c9(o9(_t[17]) + 48)}{c8(o8(_t[18]) + 45)}{ca(oa(_t[19]) + 22)}{ce(oe(_t[20]) + -55)}{cf(of(_t[21]) + 15)}{c1(o1(_t[22]) + 63)}{c4(o4(_t[23]) + 48)}{cc(oc(_t[24]) + -2)}{cb(ob(_t[25]) + 18)}{c9(o9(_t[26]) + 44)}{c2(o2(_t[27]) + -10)}{c7(o7(_t[28]) + 45)}{ce(oe(_t[29]) + -4)}{ca(oa(_t[30]) + 19)}{c6(o6(_t[31]) + 43)}{c2(o2(_t[32]) + 11)}{c9(o9(_t[33]) + 46)}{cd(od(_t[34]) + 1)}{c1(o1(_t[445]) + 67)}{c9(o9(_t[446]) + 38)}{c0(o0(_t[447]) + 57)}{c1(o1(_t[448]) + 60)}{c9(o9(_t[449]) + 46)}{cc(oc(_t[5]) + -4)}{c3(o3(_t[6]) + 49)}{cf(of(_t[7]) + -5)}{cb(ob(_t[8]) + 18)}{c0(o0(_t[9]) + 49)}{c3(o3(_t[10]) + -11)}{c8(o8(_t[11]) + 58)}{cd(od(_t[12]) + 1)}{c1(o1(_t[13]) + 66)}{ca(oa(_t[14]) + 8)}{c3(o3(_t[15]) + 71)}{c1(o1(_t[16]) + 52)}{c9(o9(_t[17]) + 38)}{c8(o8(_t[18]) + 49)}{ca(oa(_t[19]) + 12)}{ce(oe(_t[20]) + 2)}{cf(of(_t[21]) + -7)}{c1(o1(_t[22]) + 63)}{c4(o4(_t[23]) + 45)}{cc(oc(_t[24]) + 17)}{cb(ob(_t[25]) + 6)}{c9(o9(_t[26]) + -13)}{c2(o2(_t[27]) + -18)}{c7(o7(_t[28]) + 47)}{ce(oe(_t[29]) + 4)}{ca(oa(_t[30]) + 17)}{c6(o6(_t[31]) + 61)}{c2(o2(_t[32]) + 66)}{c9(o9(_t[33]) + 4)}{cd(od(_t[34]) + -16)}{c1(o1(_t[445]) + 65)}{c9(o9(_t[446]) + 60)}{c0(o0(_t[447]) + 53)}{c1(o1(_t[448]) + -8)}{c9(o9(_t[449]) + -16)}')
    window.close()
