import datetime
import time
from modules_homework.application.salary import calculate_salary
from modules_homework.application.db.people import get_employees

# для 4-го подзадания
from tqdm import tqdm
import random

def date_time_info():
    today = datetime.datetime.today().strftime("%d-%m-%Y")
    now = time.strftime("%H:%M:%S")
    print(f"{today}\n{now}")

# для 4-го подзадания
def progress_bar():
    _list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for _ in tqdm(_list, colour='green', ncols=100):
        time.sleep(random.uniform(0.2, 1))

if __name__ == '__main__':
    date_time_info()
    progress_bar()
    calculate_salary()
    get_employees()



