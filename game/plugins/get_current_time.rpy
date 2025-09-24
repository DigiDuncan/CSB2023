init python:
    import datetime
    import calendar

    def get_current_time():
        return datetime.datetime.now()

    def get_today():
        return calendar.day_name[datetime.date.today().weekday()]
