class TuringMachineFake:
    
    def __init__(self):
        self.state = 'q0'
        self.reject = ('qReject', '0', '-')
        self.rules_dict = {'q00': ('q1', '0', '>'), 'q10': ('q0', '0', '>'), 'q01': ('q0', '1', '>'), 'q11': ('q1', '1', '>'), 'q0': ('qAccept', '', '-')}

    def run_machine(self, value):
        return(self.rules_dict.setdefault(self.state+value, self.reject))

    def set_file_handler(self, handler):
        self.file_handler = handler