from msilib.schema import Binary
from NPChecker import NPChecker

class List_Values:
    def return_list(self, end_value):
        results = []
        for i in range(0, end_value+1):
            value = bin(i)
            NP_Checker = NPChecker(value[2:])
            NP_Checker.get_next_values()
            result = NP_Checker.list()
            results.append([i, value[2:], result])
        return(results)

