'''
Author: Thoma411
Date: 2023-06-02 22:08:08
LastEditTime: 2023-06-09 18:17:29
Description:
'''

import os
import numpy as np
import tkinter as tk

# *基本项
OD = 3  # 阶数
ROW1 = 0  # U层
ROW2 = 1  # E层
ROW3 = 2  # D层
COL1 = 0  # L层
COL2 = 1  # M层
COL3 = 2  # R层

# *块颜色
NULTMP = -1  # 临时交换用 区分其他颜色
WHT = 0
YEL = 5
GRE = 1
BLU = 4
RED = 2
ORG = 3

# *显示设置
SL = 20  # 方形边长
OX = 90  # 定位点x
OY = 90  # 定位点y
IOFF_X = 10  # 面与面间的基础偏移量x
IOFF_Y = 10  # 面与面间的基础偏移量y

OFL_X = OX-IOFF_X-OD*SL  # L偏移量x
OFR_X = OX+OD*SL+IOFF_X  # R偏移量x
OFB_X = OX+(OD*SL+IOFF_X)*2  # B偏移量x
OFU_Y = OY-IOFF_Y-OD*SL  # U偏移量y
OFD_Y = OX+OD*SL+IOFF_Y  # D偏移量y

# *颜色对照表
COLORF = ['white', 'green', 'red', 'orange', 'blue', 'yellow']

# *初始化各面
facetF = np.full((OD, OD), GRE)
facetB = np.full((OD, OD), BLU)
facetU = np.full((OD, OD), WHT)
facetD = np.full((OD, OD), YEL)
facetL = np.full((OD, OD), ORG)
facetR = np.full((OD, OD), RED)


def rtt(mtx, degree=1):  # 矩阵旋转
    return np.rot90(mtx, k=-degree)


def moveF(f, u, r, d, l):  # F
    f = rtt(f, 1)
    tmp = np.full((OD, OD), NULTMP)
    tmp[ROW3] = u[ROW3]
    rttl = rtt(l, 1)  # 将L面临时旋转, 化列为行
    u[ROW3] = rttl[ROW3]
    rttd = rtt(d, 1)  # 将D面临时旋转, 化行为列
    l[:, COL3] = rttd[:, COL3]
    rttr = rtt(r, 1)  # 将L面临时旋转, 化列为行
    d[ROW1] = rttr[ROW1]
    tmp = rtt(tmp, 1)  # 将tmpU面临时旋转, 化行为列
    r[:, COL1] = tmp[:, COL1]
    return f, u, r, d, l


def moveF2(f, u, r, d, l):  # F2
    f = rtt(f, 2)
    tmp_rowu = np.copy(u[ROW3])  # U-D互换
    u[ROW3] = d[ROW1]
    u[ROW3] = u[ROW3, ::-1]  # D->U值反转
    d[ROW1] = tmp_rowu
    d[ROW1] = d[ROW1, ::-1]  # U->D值反转
    tmp_colr = np.copy(r[:, COL1])  # L-R互换
    r[:, COL1] = l[:, COL3]
    r[:, COL1] = r[::-1, COL1]  # L->R值反转
    l[:, COL3] = tmp_colr
    l[:, COL3] = l[::-1, COL3]  # R->L值反转
    return f, u, r, d, l


def moveF_(f, u, r, d, l):  # F'
    f = rtt(f, -1)
    tmp = np.full((OD, OD), NULTMP)
    tmp[ROW3] = u[ROW3]
    rttr = rtt(r, -1)  # 将R面临时旋转, 化列为行
    u[ROW3] = rttr[ROW3]
    rttd = rtt(d, -1)  # 将D面临时旋转, 化行为列
    r[:, COL1] = rttd[:, COL1]
    rttl = rtt(l, -1)  # 将L面临时旋转, 化列为行
    d[ROW1] = rttl[ROW1]
    tmp = rtt(tmp, -1)  # 将tmpU面临时旋转, 化行为列
    l[:, COL3] = tmp[:, COL3]
    return f, u, r, d, l


def moveB(b, u, r, d, l):  # B
    b = rtt(b, 1)
    tmp = np.full((OD, OD), NULTMP)
    tmp[ROW1] = u[ROW1]
    rttr = rtt(r, -1)  # 将R面临时旋转, 化列为行
    u[ROW1] = rttr[ROW1]
    rttd = rtt(d, -1)  # 将D面临时旋转, 化行为列
    r[:, COL3] = rttd[:, COL3]
    rttl = rtt(l, -1)  # 将L面临时旋转, 化列为行
    d[ROW3] = rttl[ROW3]
    tmp = rtt(tmp, -1)  # 将tmpU面临时旋转, 化行为列
    l[:, COL1] = tmp[:, COL1]
    return b, u, r, d, l


def moveB2(b, u, r, d, l):  # B2
    b = rtt(b, 2)
    tmp_rowu = np.copy(u[ROW1])  # U-D互换
    u[ROW1] = d[ROW3]
    u[ROW1] = u[ROW1, ::-1]  # D->U值反转
    d[ROW3] = tmp_rowu
    d[ROW3] = d[ROW3, ::-1]  # U->D值反转
    tmp_colr = np.copy(r[:, COL3])  # L-R互换
    r[:, COL3] = l[:, COL1]
    r[:, COL3] = r[::-1, COL3]  # L->R值反转
    l[:, COL1] = tmp_colr
    l[:, COL1] = l[::-1, COL1]  # R->L值反转
    return b, u, r, d, l


def moveB_(b, u, r, d, l):  # B'
    b = rtt(b, -1)
    tmp = np.full((OD, OD), NULTMP)
    tmp[ROW1] = u[ROW1]
    rttl = rtt(l, 1)  # 将L面临时旋转, 化列为行
    u[ROW1] = rttl[ROW1]
    rttd = rtt(d, 1)  # 将D面临时旋转, 化行为列
    l[:, COL1] = rttd[:, COL1]
    rttr = rtt(r, 1)  # 将R面临时旋转, 化列为行
    d[ROW3] = rttr[ROW3]
    tmp = rtt(tmp, 1)  # 将tmpU面临时旋转, 化行为列
    r[:, COL3] = tmp[:, COL3]
    return b, u, r, d, l


def moveU(u, f, r, b, l):  # U
    u = rtt(u, 1)
    tmp_rowf = np.copy(f[ROW1])
    f[ROW1] = r[ROW1]
    r[ROW1] = b[ROW1]
    b[ROW1] = l[ROW1]
    l[ROW1] = tmp_rowf
    return u, f, r, b, l


def moveU2(u, f, r, b, l):  # U2
    u = rtt(u, 2)
    tmp_rowf = np.copy(f[ROW1])
    f[ROW1] = b[ROW1]
    b[ROW1] = tmp_rowf
    tmp_rowl = np.copy(l[ROW1])
    l[ROW1] = r[ROW1]
    r[ROW1] = tmp_rowl
    return u, f, r, b, l


def moveU_(u, f, r, b, l):  # U'
    u = rtt(u, -1)
    tmp_rowf = np.copy(f[ROW1])
    f[ROW1] = l[ROW1]
    l[ROW1] = b[ROW1]
    b[ROW1] = r[ROW1]
    r[ROW1] = tmp_rowf
    return u, f, r, b, l


def moveD(d, f, r, b, l):  # D
    d = rtt(d, 1)
    tmp_rowf = np.copy(f[ROW3])
    f[ROW3] = l[ROW3]
    l[ROW3] = b[ROW3]
    b[ROW3] = r[ROW3]
    r[ROW3] = tmp_rowf
    return d, f, r, b, l


def moveD2(d, f, r, b, l):  # D2
    d = rtt(d, 2)
    tmp_rowf = np.copy(f[ROW3])
    f[ROW3] = b[ROW3]
    b[ROW3] = tmp_rowf
    tmp_rowl = np.copy(l[ROW3])
    l[ROW3] = r[ROW3]
    r[ROW3] = tmp_rowl
    return d, f, r, b, l


def moveD_(d, f, r, b, l):  # D'
    d = rtt(d, -1)
    tmp_rowf = np.copy(f[ROW3])
    f[ROW3] = r[ROW3]
    r[ROW3] = b[ROW3]
    b[ROW3] = l[ROW3]
    l[ROW3] = tmp_rowf
    return d, f, r, b, l


def moveL(l, f, u, b, d):  # L
    l = rtt(l, 1)
    tmp_colf = np.copy(f[:, COL1])
    f[:, COL1] = u[:, COL1]
    u[:, COL1] = b[:, COL3]  # B面相反
    u[:, COL1] = u[::-1, COL1]  # *B->U面值反转
    b[:, COL3] = d[:, COL1]
    b[:, COL3] = b[::-1, COL3]  # *D->B面值反转
    d[:, COL1] = tmp_colf
    return l, f, u, b, d


def moveL2(l, f, u, b, d):  # L2
    l = rtt(l, 2)
    tmp_colu = np.copy(u[:, COL1])  # U-D互换
    u[:, COL1] = d[:, COL1]
    d[:, COL1] = tmp_colu
    tmp_colf = np.copy(f[:, COL1])  # F-B互换
    f[:, COL1] = b[:, COL3]  # 位置相反
    f[:, COL1] = f[::-1, COL1]  # 值反转
    b[:, COL3] = tmp_colf
    b[:, COL3] = b[::-1, COL3]  # 值反转
    return l, f, u, b, d


def moveL_(l, f, u, b, d):  # L'
    l = rtt(l, -1)
    tmp_colf = np.copy(f[:, COL1])
    f[:, COL1] = d[:, COL1]
    d[:, COL1] = b[:, COL3]  # B面相反
    d[:, COL1] = d[::-1, COL1]  # *B->D面值反转
    b[:, COL3] = u[:, COL1]
    b[:, COL3] = b[::-1, COL3]  # *U->B面值反转
    u[:, COL1] = tmp_colf
    return l, f, u, b, d


def moveR(r, f, u, b, d):  # R
    r = rtt(r, 1)
    tmp_colf = np.copy(f[:, COL3])
    f[:, COL3] = d[:, COL3]
    d[:, COL3] = b[:, COL1]  # B面相反
    d[:, COL3] = d[::-1, COL3]  # *B->D面值反转
    b[:, COL1] = u[:, COL3]
    b[:, COL1] = b[::-1, COL1]  # *U->B面值反转
    u[:, COL3] = tmp_colf
    return r, f, u, b, d


def moveR2(r, f, u, b, d):  # R2
    r = rtt(r, 2)
    tmp_colu = np.copy(u[:, COL3])  # U-D互换
    u[:, COL3] = d[:, COL3]
    d[:, COL3] = tmp_colu
    tmp_colf = np.copy(f[:, COL3])  # F-B互换
    f[:, COL3] = b[:, COL1]  # 位置相反
    f[:, COL3] = f[::-1, COL3]  # 值反转
    b[:, COL1] = tmp_colf
    b[:, COL1] = b[::-1, COL1]  # 值反转
    return r, f, u, b, d


def moveR_(r, f, u, b, d):  # R'
    r = rtt(r, -1)
    tmp_colf = np.copy(f[:, COL3])
    f[:, COL3] = u[:, COL3]
    u[:, COL3] = b[:, COL1]  # B面相反
    u[:, COL3] = u[::-1, COL3]  # *B->U面值反转
    b[:, COL1] = d[:, COL3]
    b[:, COL1] = b[::-1, COL1]  # *D->B面值反转
    d[:, COL3] = tmp_colf
    return r, f, u, b, d


def resetFacet(f, b, u, d, l, r):  # 重置状态
    f = np.full((OD, OD), GRE)
    b = np.full((OD, OD), BLU)
    u = np.full((OD, OD), WHT)
    d = np.full((OD, OD), YEL)
    l = np.full((OD, OD), ORG)
    r = np.full((OD, OD), RED)
    return f, b, u, d, l, r


def printTer(f=facetF, b=facetB, u=facetU, d=facetD, l=facetL, r=facetR):  # 状态输出至terminal
    frbl = np.concatenate((l, f, r, b), axis=1)
    for _u in u:
        print('      ', _u)
    print(frbl)
    for _d in d:
        print('      ', _d)
    print()


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


def moveMatch(mv, f=facetF, b=facetB, u=facetU, d=facetD, l=facetL, r=facetR, outFlag=True):  # 移动匹配
    # F moves
    if mv == "F":
        f, u, r, d, l = moveF(f, u, r, d, l)
    elif mv == "F2":
        f, u, r, d, l = moveF2(f, u, r, d, l)
    elif mv == "F'":
        f, u, r, d, l = moveF_(f, u, r, d, l)
    # B moves
    elif mv == "B":
        b, u, r, d, l = moveB(b, u, r, d, l)
    elif mv == "B2":
        b, u, r, d, l = moveB2(b, u, r, d, l)
    elif mv == "B'":
        b, u, r, d, l = moveB_(b, u, r, d, l)
    # U moves
    elif mv == "U":
        u, f, r, b, l = moveU(u, f, r, b, l)
    elif mv == "U2":
        u, f, r, b, l = moveU2(u, f, r, b, l)
    elif mv == "U'":
        u, f, r, b, l = moveU_(u, f, r, b, l)
    # D moves
    elif mv == "D":
        d, f, r, b, l = moveD(d, f, r, b, l)
    elif mv == "D2":
        d, f, r, b, l = moveD2(d, f, r, b, l)
    elif mv == "D'":
        d, f, r, b, l = moveD_(d, f, r, b, l)
    # L moves
    elif mv == "L":
        l, f, u, b, d = moveL(l, f, u, b, d)
    elif mv == "L2":
        l, f, u, b, d = moveL2(l, f, u, b, d)
    elif mv == "L'":
        l, f, u, b, d = moveL_(l, f, u, b, d)
    # R moves
    elif mv == "R":
        r, f, u, b, d = moveR(r, f, u, b, d)
    elif mv == "R2":
        r, f, u, b, d = moveR2(r, f, u, b, d)
    elif mv == "R'":
        r, f, u, b, d = moveR_(r, f, u, b, d)
    # settings
    elif mv == "0":
        f, b, u, d, l, r = resetFacet(f, b, u, d, l, r)
    else:
        print('not a move.')
        return None
    # os.system('cls')
    if outFlag:
        printTer(f, b, u, d, l, r)
    return f, b, u, d, l, r


def singleStep(f=facetF, b=facetB, u=facetU, d=facetD, l=facetL, r=facetR, outFlag=True):  # 单步移动
    outRet = True
    while 1:
        moves_str = input('move opt: ').upper()
        move_ls = moves_str.split()
        print('move-list:', move_ls)
        for mv in move_ls:
            inRet = moveMatch(mv, f, b, u, d, l, r, outFlag)
            if inRet is not None:
                f, b, u, d, l, r = inRet
                printUI(f, b, u, d, l, r)
            else:
                outRet = False
                break
        if not outRet:
            break


def multiStep(mvs, f=facetF, b=facetB, u=facetU, d=facetD, l=facetL, r=facetR, outFlag=True):  # 多步移动
    move_ls = None
    if type(mvs) == str:  # 类型识别与转换
        moves_str = mvs.upper()
        move_ls = moves_str.split()
    elif type(mvs) == list:
        move_ls = mvs
    else:
        print('unexpected type of "mvs"')
    print('move-list:', move_ls)

    for mv in move_ls:
        ret = moveMatch(mv, f, b, u, d, l, r, outFlag)
        if ret is not None:
            f, b, u, d, l, r = ret
        else:
            break
    printUI(f, b, u, d, l, r)


'''
# 定义一个二维数组
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 获取元素 5 的下标
index = np.where(array == 5)
print(index) # 输出: (array([1]), array([1]))

lst = array.tolist()
print(type(lst)) # 输出: <class 'list'>
'''

if __name__ == '__main__':
    f = facetF
    b = facetB
    u = facetU
    d = facetD
    l = facetL
    r = facetR
    # printConsole(f, b, u, d, l, r)
    # printUI(f, b, u, d, l, r)
    singleStep(f, b, u, d, l, r)
    # chs = input('move opt: ')
    # chl = ['U2', 'F', "B'", 'L']
    # multiStep(chs, f, b, u, d, l, r)
