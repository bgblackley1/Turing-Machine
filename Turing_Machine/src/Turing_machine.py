from msilib.schema import File
from FileHandling import FileHandling

class Turing_Machine:
    
    def __init__(self):
        self.state = 'q0'
        self.rules = []
        self.file_handler = FileHandling()
        self.create_dictionary()

    def create_dictionary(self):
        data = self.file_handler.get_rules()
        for rule in data:
            self.rules.append(rule.split(','))
        self.rules_dict = {}
        for rule in self.rules:
            key = rule[0]+rule[1]
            value = (rule[2], rule[3], rule[4][0])
            self.rules_dict[key] = value

    def run_machine(self, value):
        try:
            current = self.rules_dict[self.state+value]
            self.state = current[0]
            return(current[0], current[1], current[2])
        except:
            self.state = 'qReject'
            return('qReject', value, '-')

    def set_file_handler(self, handler):
        self.file_handler = handler