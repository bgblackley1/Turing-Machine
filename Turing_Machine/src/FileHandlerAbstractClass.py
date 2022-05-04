from abc import ABC, abstractmethod

class FileHandlerAbstractClass(ABC):

    def set_rule(self, current_state,value_on_tape,next_state,next_value,direction):
        pass

    def set_inputs(self, input):
        pass

    def get_preset(self, option):
        pass

    def set_preset(self, data):
        pass

    def get_rules(self):
        pass

    def clear_file(self):
        pass