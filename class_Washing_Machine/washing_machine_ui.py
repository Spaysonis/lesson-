

from wahs_power_on import WashingMachine

class UiWashingMachine:

    def __init__(self, core:WashingMachine):
        self.core = core


    def run(self):

        while True:
            print('WASHING MACHINE\n')
            print('1 = POWER ON')
            print('2 = POWER OFF')
            print('3 = SELECT MODE\n')
            choice = int(input('--> '))

            if choice == 1:
                print(self.core.power_on(True))
            elif choice == 2:
                print(self.core.power_on(False))
                break
            elif choice == 3:
                print(self.core.select_mode(self.list_mode()))
            else:
                break


    def list_mode(self):
        if self.core.power:
            print('---LIST MODE---')
            print('1 = БЫСТРАЯ СТИРКА')
            print('2 = ДОЛГАЯ СТИРКА')
            choice = int(input('-->'))
            if choice == 1:
                return 'БЫСТРАЯ СТИРКА'
            elif choice == 2:
                return 'ДОЛГАЯ СТИРКА'




