from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "*** Take Rest ***",
            message = "Rest is importent to your health.",
            timeout = 5)
        time.sleep(20)