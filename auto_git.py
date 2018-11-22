import threading
import time
import os

# linux shell 命令
# shell_command = "./test.sh"
shell_command = "./auto_git.sh"

# 定时运行点
timing = 10


def shell(command):
    run_command = os.popen(command).read()
    print(run_command)


def main():
    shell(shell_command)
    global timer
    timer = threading.Timer(5, main)
    timer.start()


def running_time(hour):
    """
    :hour: 需要定位到的时间点，小时
    :return: bool
    """
    now_time = time.localtime(time.time())
    if now_time.tm_hour == hour:
        return True
    else:
        return False


def is_right_time():
    """
    检测时间是否到点了
    """
    if running_time(timing):
        main()
    else:
        print(f"not a good time ---> 等待 {timing} 点")
        global timer_check_time
        timer_check_time = threading.Timer(5, is_right_time)
        timer_check_time.start()


if __name__ == '__main__':
    # main()
    is_right_time()