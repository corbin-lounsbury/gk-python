import threading
import time

def waitSeconds(seconds):
    print(f"waiting for {seconds} seconds\n")
    time.sleep(seconds)
    print("My wait is done!")

def interrupt(phrase):
    print(f"I jumped in to say {phrase}")

thread1 = threading.Thread(target=waitSeconds, args=(3,))
thread2 = threading.Thread(target=interrupt, args=("NEE!",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()