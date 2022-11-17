# instructions
# 1. Write a program to implement threading
# 2. Create two functions with parameters to perform certain actions and print
# 3. Create two threads for calling functions and pass arguments
# 4. Run the threads

import random
import threading
import time

def waitSeconds(seconds):
    print(f"waiting for {seconds} seconds\n")
    time.sleep(seconds)
    print("My wait is done!")

def interrupt(phrase):
    print(f"I jumped in to say {phrase}")

randNum = random.randint(1,5)

thread1 = threading.Thread(target=waitSeconds, args=(randNum,))
thread2 = threading.Thread(target=interrupt, args=("we are the knights who say \n NEE!",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()