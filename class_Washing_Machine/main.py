from calss_Pult.washing_machine_ui import UiWashingMachine
from calss_Pult.wahs_power_on import WashingMachine



if __name__ == '__main__':
    machine = WashingMachine()
    ui = UiWashingMachine(machine)
    ui.run()