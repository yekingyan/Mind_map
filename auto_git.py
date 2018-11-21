import threading
import time
import os


def git():
    run_git = os.popen('./test.sh').read()
    print(run_git)


def time_handler():
    running_time(18)
    global timer
    timer = threading.Timer(5, time_handler)
    timer.start()


def running_time(hour):
    now_time = time.localtime(time.time())
    if now_time.tm_hour == hour:
        git()


def is_right_time():
    ...



if __name__ == '__main__':
    time_handler()
    # running_time(18)