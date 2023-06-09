'''
Author: Thoma411
Date: 2023-06-01 22:44:04
LastEditTime: 2023-06-09 20:22:00
Description: 
'''
from baseDefine import *
import tkinter as tk


def printUI(f=facetF, b=facetB, u=facetU, d=facetD, l=facetL, r=facetR):  # 状态输出至UI
    root = tk.Tk()
    cv = tk.Canvas(root)
    cv.pack()
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
    root.mainloop()
