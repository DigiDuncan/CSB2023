init python:
    import datetime
    import calendar

    def get_current_time():
        return datetime.datetime.now()

    def get_today():
        return calendar.day_name[datetime.date.today().weekday()]
    
    class Timer:
        def __init__(self, seconds: float):
            self.seconds = seconds

            self.start_time = get_current_time()

            self.duration = datetime.timedelta(seconds = seconds)
            self.end_time = self.start_time + self.duration

        def get_remaining(self):
            return self.end_time - datetime.datetime.now()
