'''
Author: Thoma411
Date: 2023-06-09 20:17:57
LastEditTime: 2023-06-15 00:11:22
Description: 
'''
import numpy as np

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
WHT = 0  # 白
YEL = 5  # 黄
GRE = 1  # 绿
BLU = 4  # 蓝
RED = 2  # 红
ORG = 3  # 橙

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

# *终端输出定义
OUT_NONE = 0  # 不输出任何内容
OUT_ERRO = 1  # 仅输出错误
OUT_MVLS = 2  # 输出打乱公式&错误
OUT_STAT = 3  # 输出逐步打乱状态(全部输出)
