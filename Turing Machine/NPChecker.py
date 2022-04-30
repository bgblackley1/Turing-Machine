from Turing_machine import Turing_Machine

class NPChecker:
    
    def __init__(self, input):
        self.runs = 0
        self.final_state = 'qReject'
        self.input = input
        self.pointer = 0
        self.machine = Turing_Machine()
        self.direction = '>'
        self.input_to_tape = list(input)

    def get_next_values(self):
        if self.direction != '-' and self.runs < 1000:
            try:
                state, self.value, self.direction = self.machine.run_machine(self.input_to_tape[self.pointer])
                self.runs += 1
            except:
                if self.pointer < 0: 
                    self.input_to_tape.insert(0, '')
                else:
                    self.input_to_tape.append('')
                state, self.value, self.direction = self.machine.run_machine(self.input_to_tape[self.pointer])
                self.runs += 1
            if self.machine.state == 'qReject' or self.machine.state == 'qAccept':
                self.final_state = self.machine.state    
            self.update_tape()

    def update_tape(self):            
        if self.pointer < len(self.input_to_tape) and self.pointer >= 0:
            self.input_to_tape[self.pointer] = self.value
        elif self.pointer > len(self.input_to_tape):
            if self.value != '':
                self.input_to_tape.append(self.value)
        else:
            if self.value != '':
                self.input_to_tape.insert(0, self.value)
        self.update_pointer()
    
    def update_pointer(self):
        if self.direction == '>':
            self.pointer += 1
        elif self.direction == '<':
            self.pointer -= 1
        self.get_next_values()
        
    def NP(self):
        if self.runs < len(self.input)**2:
            return('P', self.runs)
        else:
            return('NP', self.runs)

    def list(self): 
        return(self.final_state)

class Turing_Machine:
    
    def __init__(self):
        self.state = 'q0'
        self.rules = []
        self.create_dictionary()

    def create_dictionary(self):
        with open('rules.txt') as f:
            data = f.readlines()
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
        

