from time import sleep, time
import multiprocessing

def create_task(task_name):
    sleep(3)
    print(f"{task_name} выполнена")




if __name__ == "__main__":
    start = time()
    process1 = multiprocessing.Process(target=create_task, args=("task1",))
    process2 = multiprocessing.Process(target=create_task, args=("task2",))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end = time()
    print(end - start)