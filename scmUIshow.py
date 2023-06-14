'''
Author: Thoma411
Date: 2023-06-01 22:44:04
LastEditTime: 2023-06-15 00:47:22
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


def updScmUI(cv: tk.Canvas):  # 刷新打乱状态与显示UI
    scm = sm.genScmb3(sm.SCM_LEN_MIN, sm.SCM_LEN_MAX)
    f, b, u, d, l, r = mm.multiStep(mvs=scm, outFlag=OUT_NONE)
    printUI(cv, f, b, u, d, l, r)
    return scm


def uMain():
    def refresh():  # 刷新响应
        scm_ls = updScmUI(cv)
        scm_str = ' '.join(_ for _ in scm_ls)
        algm.config(text=scm_str)

    root = tk.Tk()
    root.title('Cube Scrambles Displayer')
    root.geometry('400x300')
    root.resizable(False, False)
    cv = tk.Canvas(root)
    cv.pack()
    scm_ls = updScmUI(cv)
    scm_str = ' '.join(_ for _ in scm_ls)
    # 显示打乱公式文本
    algm = tk.Label(root, text=scm_str)
    algm.pack(side=tk.LEFT)
    # 刷新按钮
    refs = tk.Button(root, text='refresh', command=refresh)
    refs.pack(side=tk.RIGHT)
    root.mainloop()


if __name__ == '__main__':
    uMain()
