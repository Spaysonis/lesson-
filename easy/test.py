from datetime import datetime, timedelta

def schedule_generator(days, work_days, rest_days, start_date=None):
    # Функция возвращает расписание рабочих дней сотрудника, которое генерируется начиная с start_date на days дней вперед,
    # учитывая что сотрудник чередует рабочие дни (work_days) и дни отдыха (rest_days).
    if start_date is None:
        start_date = datetime(2020, 1, 30)

    task_list = []
    currency_date = start_date
    total_day = 0

    while total_day < days:
        # Добавляем рабочие дни
        for _ in range(work_days):
            if total_day < days:
                task_list.append(currency_date)
                currency_date += timedelta(days=1)
                total_day += 1

        # Пропускаем выходные дни, не добавляем их в список
        for _ in range(rest_days):
            if total_day < days:
                currency_date += timedelta(days=1)
                total_day += 1

    return task_list


# Пример использования
import unittest
from datetime import datetime

class TestScheduleGenerator(unittest.TestCase):

    def test_basic_schedule(self):
        # Проверим расписание на 5 дней с 2 рабочими днями и 1 выходным
        expected_result = [
            datetime(2020, 1, 30),  # Рабочий день 1
            datetime(2020, 1, 31),  # Рабочий день 2
            datetime(2020, 2, 1),   # Выходной день 1
            datetime(2020, 2, 2),   # Рабочий день 3
            datetime(2020, 2, 3)    # Рабочий день 4
        ]
        result = schedule_generator(days=5, work_days=2, rest_days=1)
        self.assertEqual(result, expected_result)

    def test_single_workday(self):
        # Проверим расписание на 3 дня с 1 рабочим днем и 1 выходным
        expected_result = [
            datetime(2020, 1, 30),  # Рабочий день 1
            datetime(2020, 1, 31)   # Выходной день 1
        ]
        result = schedule_generator(days=3, work_days=1, rest_days=1)
        self.assertEqual(result, expected_result)

    def test_no_work_days(self):
        # Проверим случай, когда рабочие дни = 0
        result = schedule_generator(days=5, work_days=0, rest_days=1)
        self.assertEqual(result, [])

    def test_edge_case(self):
        # Проверим расписание на 0 дней (пустое расписание)
        result = schedule_generator(days=0, work_days=2, rest_days=1)
        self.assertEqual(result, [])

    def test_long_schedule(self):
        # Проверим расписание на 10 дней с 3 рабочими днями и 1 выходным
        expected_result = [
            datetime(2020, 1, 30),  # Рабочий день 1
            datetime(2020, 1, 31),  # Рабочий день 2
            datetime(2020, 2, 1),   # Выходной день 1
            datetime(2020, 2, 2),   # Рабочий день 3
            datetime(2020, 2, 3),   # Рабочий день 4
            datetime(2020, 2, 4),   # Выходной день 2
            datetime(2020, 2, 5),   # Рабочий день 5
            datetime(2020, 2, 6),   # Рабочий день 6
            datetime(2020, 2, 7),   # Выходной день 3
            datetime(2020, 2, 8)    # Рабочий день 7
        ]
        result = schedule_generator(days=10, work_days=3, rest_days=1)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
