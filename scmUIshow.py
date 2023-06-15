'''
Author: Thoma411
Date: 2023-06-01 22:44:04
LastEditTime: 2023-06-15 23:40:27
Description: 
'''
from baseDefine import *
import scrambler as sm
import moveMethod as mm
import tkinter as tk


def printUI(cv: tk.Canvas, f=facetF, b=facetB, u=facetU, d=facetD, l=facetL, r=facetR):  # 状态输出至UI
    for fi in range(OD):
        for fj in range(OD):
            cv.create_rectangle(OX+fi*SL, OY+fj*SL, OX+(fi+1)*SL, OY+(fj+1)*SL,
                                fill=COLORF[f[fj][fi]], outline='black')
            cv.create_rectangle(OFB_X+fi*SL, OY+fj*SL, OFB_X+(fi+1)*SL, OY+(fj+1)*SL,
                                fill=COLORF[b[fj][fi]], outline='black')
            cv.create_rectangle(OX+fi*SL, OFU_Y+fj*SL, OX+(fi+1)*SL, OFU_Y+(fj+1)*SL,
                                fill=COLORF[u[fj][fi]], outline='black')
            cv.create_rectangle(OX+fi*SL, OFD_Y+fj*SL, OX+(fi+1)*SL, OFD_Y+(fj+1)*SL,
                                fill=COLORF[d[fj][fi]], outline='black')
            cv.create_rectangle(OFL_X+fi*SL, OY+fj*SL, OFL_X+(fi+1)*SL, OY+(fj+1)*SL,
                                fill=COLORF[l[fj][fi]], outline='black')
            cv.create_rectangle(OFR_X+fi*SL, OY+fj*SL, OFR_X+(fi+1)*SL, OY+(fj+1)*SL,
                                fill=COLORF[r[fj][fi]], outline='black')


def updScmUI(cv: tk.Canvas, scm):  # 刷新打乱状态与显示UI
    f, b, u, d, l, r = mm.multiStep(mvs=scm, outFlag=OUT_NONE)
    printUI(cv, f, b, u, d, l, r)


def uMain():
    def refresh():  # 刷新响应
        scm_ls = sm.genScmb3(sm.SCM_LEN_MIN, sm.SCM_LEN_MAX)  # 随机生成打乱公式
        updScmUI(cv, scm_ls)
        scm_str = ' '.join(_ for _ in scm_ls)  # list[str]->str
        algm.delete(1.0, 'end')  # 清空text
        algm.insert(tk.INSERT, scm_str)  # 输出新的公式

    def inputScm():  # 读取自定义打乱
        inpScm = algm.get(1.0, 'end').replace(
            '\n', '').split(' ')  # 获取text内的公式
        updScmUI(cv, inpScm)

    # 主窗口
    root = tk.Tk()
    root.title('Cube Scrambles Displayer')
    root.geometry('420x300')

    # 显示画布
    cv = tk.Canvas(root)
    cv.pack(side=tk.BOTTOM)
    scm_ls = sm.genScmb3(sm.SCM_LEN_MIN, sm.SCM_LEN_MAX)  # 随机生成打乱公式
    updScmUI(cv, scm_ls)
    scm_str = ' '.join(_ for _ in scm_ls)  # list[str]->str

    # 显示打乱公式文本
    algm = tk.Text(root, width=50, height=1, undo=True)
    algm.config(font=('Arial', 10))
    algm.insert(tk.INSERT, scm_str)
    algm.pack(side=tk.LEFT)

    # 刷新按钮
    refs = tk.Button(root, text='rfs', command=refresh)
    refs.pack(side=tk.RIGHT)

    # 自定义打乱按钮
    rset = tk.Button(root, text='set', command=inputScm)
    rset.pack(side=tk.RIGHT)
    root.mainloop()


if __name__ == '__main__':
    uMain()
