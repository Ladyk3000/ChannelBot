from datetime import datetime
from pytz import timezone


class Timer:
    def __init__(self, start_time='11:00', end_time='14:00'):
        self.__tz = timezone('Europe/Moscow')
        self.__start_post_time = self.__str_to_time(start_time)
        self.__end_post_time = self.__str_to_time(end_time)
        self.posted_today = False

    def __str_to_time(self, str_time: str):
        time_obj = datetime.strptime(str_time, '%H:%M')
        time_to_eq = datetime(datetime.today().year,
                              datetime.today().month,
                              datetime.today().day,
                              time_obj.hour,
                              time_obj.minute, 0)
        return self.__tz.localize(time_to_eq)

    def should_post(self):
        now = self.__tz.localize(datetime.now())
        if self.__start_post_time <= now <= self.__end_post_time and not self.posted_today:
            self.posted_today = True
            return True
        if self.__tz.localize(datetime.now().replace(hour=0, minute=0)) < now < self.__start_post_time:
            self.posted_today = False
        return False
