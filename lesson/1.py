#
#
# class WashingMachine:
#     def __init__(self, brand: str, capacity: int):
#         self.brand = brand
#         self.capacity = brand
#         self.__is_running =False
#         self.level_water = 0
#
#
#
#     def start(self):
#         if self.__is_running:
#             print(f"{self.brand} working")
#         elif self.level_water < 100:
#             print('level water is no 100')
#             self.auto_fill_water()
#             self.__is_running = True
#             print(f"{self.brand} srating")
#         else:
#             self.__is_running = True
#             print(f"{self.brand} start washing")
#
#     def stop(self):
#         if self.__is_running:
#             self.__is_running = False
#             print(f"{self.brand} Stop")
#         else:
#             print(f"{self.brand} dont work")
#
#     def water_level(self, level: int):
#         if 0 <= level <= 100:
#             self.level_water = level
#             print(f'{level} is good')
#         else:
#             print(f'level water error (0 - 100)')
#
#     def auto_fill_water(self):
#         self.level_water = 100
#         print(f"Water = 100%")
#
#
#
#     def __str__(self):
#         return  f"WashingMachine {self.brand}, {self.capacity}"
#
# machine = WashingMachine("LG", 7)
# machine.__is_running = True
# print(machine)
# machine.water_level(50)
# print(machine)
# machine.start()
# machine.start()
# machine.stop()
# machine.stop()
# machine.water_level(120)
#



def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
array = [1,2,3,4,5,6]
target = 3

index_el = binary_search(array, target)

if index_el != -1:
    print(f"Element = {target} position = {index_el}")
else:
    print("Errro")