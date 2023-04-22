import datetime


def get_current_datetime():
    current_datetime = datetime.datetime.now()
    return current_datetime.strftime("%Y-%m-%d-%H-%M-%S")
