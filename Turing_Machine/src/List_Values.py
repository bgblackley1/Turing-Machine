from msilib.schema import Binary
from NPChecker import NPChecker


class List_Values:
    def __init__(self):
        self.NP_Checker = NPChecker('0')

    def return_list(self, end_value):
        results = []
        for i in range(0, end_value + 1):
            value = bin(i)[2:]
            self.NP_Checker.runs = 0
            self.NP_Checker.final_state = 'qReject'
            self.NP_Checker.machine.state = 'q0'
            self.NP_Checker.input = value
            self.NP_Checker.pointer = 0
            self.NP_Checker.direction = '>'
            self.NP_Checker.input_to_tape = list(value)
            self.NP_Checker.get_next_values()
            result = self.NP_Checker.list()
            results.append([i, value, result])
        return (results)

    def set_np_checker(self, np):
        self.NP_Checker = np
