import datetime

class OrderPageHelper():
        
    def get_previous_day(self):
        now = datetime.date.today()-datetime.timedelta(1)
        previous_day = now.day
        if 0 < now.day < 10:
            previous_day = f"0{str(now.day)}"
        else:
            previous_day = str(now.day)
        return previous_day

    def get_next_day(self):
        now = datetime.date.today()+datetime.timedelta(1)
        next_day = now.day
        if 0 < now.day < 10:
            next_day = f"0{str(now.day)}"
        else:
            next_day = str(now.day)
        return next_day

    def select_metro_subinput(self, metro_number):
        if 0 < metro_number < 238:
            return str(metro_number)
        else:
            raise(RuntimeError(f'The passed value {metro_number} does not exist'))
        