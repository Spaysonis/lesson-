from datetime import datetime, timedelta




def schedule_generator(days, work_days, rest_days, start_date=None):
    #  Функция возвращает расписание рабочих дней сотрудника, которое генерируется начиная с start_date на days дней вперед,
    #  учитывая что сотрудник чередует рабочие дни(work_days) и дни отдыха (rest_days).
    if start_date is None:
        start_date = datetime(2020,1, 30)

    task_list = []
    currency_date = start_date
    total_day = 0

    while total_day < days - rest_days:
        for _ in range(work_days):
            if total_day < days:
                task_list.append(currency_date)
                currency_date += timedelta(days=1)
                total_day += 1

        for _ in range(rest_days):
            currency_date += timedelta(days=1)

    return task_list



import unittest
from datetime import datetime

class TestScheduleGenerator(unittest.TestCase):

    def test_schedule(self):
        # Проверим расписание на 5 дней с 2 рабочими днями и 1 выходным
        expected_result = [
            datetime(2020, 1, 30),  # Рабочий день 1
            datetime(2020, 1, 31),  # Рабочий день 2
            datetime(2020, 2, 2),   # Выходной день 1
            datetime(2020, 2, 3)    # Рабочий день 3
        ]
        result = schedule_generator(days=5, work_days=2, rest_days=1, start_date=datetime(2020, 1, 30))
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

