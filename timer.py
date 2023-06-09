'''
Author: Thoma411
Date: 2023-06-09 19:49:33
LastEditTime: 2023-06-09 20:08:09
Description: 
'''
import time as tm
import keyboard as kb

start_time = 0
end_time = 0
elapsed_time = 0
stopwatch_running = False

print("Press space to start the stopwatch")

while not kb.is_pressed('space'):
    pass

start_time = tm.time()
stopwatch_running = True

print("\nStopwatch has started")

while stopwatch_running:
    elapsed_time = tm.time() - start_time
    print("Elapsed time: {:.2f} seconds".format(elapsed_time), end="\r")
    tm.sleep(0.1)
    if kb.is_pressed('space'):  # 按下空格键立即停止计时器
        end_time = tm.time()
        elapsed_time = end_time - start_time
        print("\nElapsed time: {:.2f} seconds".format(elapsed_time))
        stopwatch_running = False
