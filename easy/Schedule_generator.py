from datetime import datetime

#  days: 5, work_days: 2, rest_days: 1, start_date: datetime(2020, 1, 30) ->
# [

# ]
def schedule_generator(days=5, work_days=2, rest_days=1, start_date=None):

    if start_date is None:
        start_date = datetime(2020, 1, 30)

    schedule = []

    current_data = start_date

    while len(schedule) < days:
        pass



