from class_Washing_Machine.washing_machine_ui import UiWashingMachine
from class_Washing_Machine.wahs_power_on import WashingMachine



if __name__ == '__main__':
    machine = WashingMachine()
    ui = UiWashingMachine(machine)
    ui.run()