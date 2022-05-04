from FileHandlerAbstractClass import FileHandlerAbstractClass

class FileHandling(FileHandlerAbstractClass):
    
    rules = []

    def set_rule(self, current_state,value_on_tape,next_state,next_value,direction):
        self.rules.append(current_state+','+value_on_tape+','+next_state+','+next_value+','+direction +'\n')

    def set_inputs(self, input):
        self.rules = input

    def get_preset(self, option):
        return(['q0,0,q1,0,>', 'q1,0,q0,0,>', 'q0,1,q0,1,>', 'q1,1,q1,1,>', 'q0,,qAccept,,-'])

    def set_preset(self, data):
        self.rules = [['q0,0,q1,0,>'], ['q1,0,q0,0,>'], ['q0,1,q0,1,>'], ['q1,1,q1,1,>'], ['q0,,qAccept,,-']]

    def get_rules(self):
        return(['q0,0,q1,0,>', 'q1,0,q0,0,>', 'q0,1,q0,1,>', 'q1,1,q1,1,>', 'q0,,qAccept,,-'])

    def clear_file(self):
        self.rules = []