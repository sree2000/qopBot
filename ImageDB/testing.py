from datetime import time
import datetime

drop_time = time(11, 00, 00)            # time of drop on Thursdays


def excecute_collection_reboot(day_of_reboot):
    return 0;

def main():
    dropdate = input("When is the date of the next drop? MM-DD-YYYY:\n")
    times = dropdate.split('-')
    date_of_drop = datetime.date(int(times[2]), int(times[0]), int(times[1]))
    db_collection_reboot_day = int(times[1]) - 1
    day_of_reboot = datetime.date(int(times[2]), int(times[0]), db_collection_reboot_day)
    print(day_of_reboot)
    print(date_of_drop)
    excecute_collection_reboot(day_of_reboot)


main()