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
            return('qReject', value, '-')
