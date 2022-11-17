import random
import multiprocessing
import time

def waitSeconds(seconds):
    print(f"waiting for {seconds} seconds\n")
    time.sleep(seconds)
    print("My wait is done!")

def interrupt(phrase):
    print(f"I jumped in to say {phrase}")

if __name__ =="__main__":

    randNum = random.randint(1,5)

    thread1 = multiprocessing.Process(target=waitSeconds, args=(randNum,))
    thread2 = multiprocessing.Process(target=interrupt, args=("we are the knights who say \n NEE!",))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Done")