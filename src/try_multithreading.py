from time import sleep, time
import threading



def create_task(task_name):
    sleep(3)
    print(f"{task_name} выполнена")


if __name__ == "__main__":
    start_time = time()
    thread1 = threading.Thread(target=create_task, args=("task1",))
    thread2 = threading.Thread(target=create_task, args=("task2",))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    end_time = time()
    print(end_time - start_time)