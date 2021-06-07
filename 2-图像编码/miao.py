import os
import PySimpleGUI as sg
from pathlib import Path

r1 = '咪'
r0 = '喵'

txt = Path(__file__).parent / 'temp.txt'
img = Path(__file__).parent / 'img.png'

def decode(p):
    if not isinstance(p, Path):
        p = Path(p)
    out = []
    with p.open('r') as fr:
        s = fr.read().strip().replace('\r', '').replace('\n', '').replace(' ', '')
    b = ''
    for e in s:
        if e == r1:
            b += '1'
        else:
            b += '0'
        if len(b) >= 8:
            out.append(int(b, 2))
            b = ''
    with img.open('wb') as fw:
        fw.write(bytes(out))
    return out


def encode(img_path):
    out = ''
    if not isinstance(img_path, Path):
        img_path = Path(img_path)
    with img_path.open('rb') as fr:
        for b in fr.read():
            b = bin(b)[2:]
            out += r0 * (8 - len(b))
            for i in b:
                if i == '1':
                    out += r1
                else:
                    out += r0
    with txt.open('w') as fw:
        fw.write(out)
    return out


# if __name__ == '__main__':
#     decode()


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.

main_layout = [
    [sg.Button('编码'), sg.Button('解码')]
]

# Create the Window
main_window = sg.Window('喵星人语编解码器', main_layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = main_window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    elif event == '解码':
        decode_layout = [
            [sg.Text('输入喵星人语'), sg.Input(key='miao_input'), sg.FileBrowse()],
            [sg.Button('Ok'), sg.Button('Cancel')]
        ]
        decode_window = sg.Window('解码喵星人语', decode_layout)
        while True:
            event, values = decode_window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
            decode(values['miao_input'])
            decoded_win = sg.Window('解码后', [[sg.Image(img)]])
            while True:
                event, values = decoded_win.read()
                if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                    break
            decoded_win.close()
        decode_window.close()
    elif event == '编码':
        encode_layout = [
            [sg.Text('输入图片地址：'), sg.InputText(key='img_path'), sg.FileBrowse()],
            [sg.Button('Ok'), sg.Button('Cancel')]
        ]
        encode_window = sg.Window('编码喵星人语', encode_layout)
        while True:
            event, values = encode_window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
            encode(values['img_path'])
            os.system(f'start {txt}')
        encode_window.close()

main_window.close()
