'''
Author: Thoma411
Date: 2023-06-09 17:55:09
LastEditTime: 2023-06-09 18:08:30
Description: 
'''
import scrambler as sm
import moveMethod as mm

if __name__ == '__main__':
    s1 = sm.genScmb3(sm.SCM_LEN_MIN, sm.SCM_LEN_MAX)
    mm.multiStep(s1)
