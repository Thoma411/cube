'''
Author: Thoma411
Date: 2023-06-09 11:07:34
LastEditTime: 2023-06-09 17:42:59
Description:
'''
import random as rd
import flque as fq

SCM_LEN_MIN = 17
SCM_LEN_MAX = 20

# 移动方位字典
optDict = {
    "optF": ["F", "F2", "F'"],
    "optB": ["B", "B2", "B'"],
    "optU": ["U", "U2", "U'"],
    "optD": ["D", "D2", "D'"],
    "optL": ["L", "L2", "L'"],
    "optR": ["R", "R2", "R'"]
}


def genScmb(lmin: int, lmax: int):  # 生成打乱公式
    '''
    生成算法应满足以下两点:\n
    1.任意连续两次选择的移动操作不得来自同一方位列表(即禁止"... U2 U' ..."一类操作的出现)\n
    2.任意连续三次选择的移动操作不得来自同一组相对面(即禁止"... F2 B' F' ..."一类操作的出现)
    '''
    scrambles = []
    rd_key = None
    ls3moves = fq.FixedQueue(2)  # 保存近3次移动
    optKey = list(optDict)
    for i in range(rd.randint(lmin, lmax)):
        if i == 0:  # 第1次选择
            rd_key = rd.choice(optKey)
        elif i == 1:  # 第2次选择
            rmRange = optKey.copy()  # 创建临时选择列表
            rmRange.remove(ls3moves.get(0))  # 移除上次所选列表
            rd_key = rd.choice(rmRange)  # 从剩余可选列表中选择
        else:  # 第>2次选择
            rmRange = optKey.copy()  # 创建临时选择列表
            rmRange.remove(ls3moves.get(0))  # 移除上次、上上次所选列表
            rmRange.remove(ls3moves.get(1))
            rd_key = rd.choice(rmRange)  # 从剩余可选列表中选择
        rd_move = rd.choice(optDict[rd_key])
        ls3moves.add(rd_key)
        scrambles.append(rd_move)
    return scrambles


if __name__ == '__main__':
    for _ in range(20):
        s1 = genScmb(17, 20)
        print(s1, len(s1))
