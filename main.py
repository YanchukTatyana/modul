

from application.db.people import *
from application.salary import *
from datetime import datetime




if __name__ == '__main__':
    print(get_employees())
    print(calculate_salary())
    print(datetime.now())


