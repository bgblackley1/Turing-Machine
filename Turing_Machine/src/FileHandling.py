from File import File
 
class FileHandling(File):
        
    def set_rule(self, current_state,value_on_tape,next_state,next_value,direction):
        rules = open("rules.txt", "a")
        rules.writelines(current_state+','+value_on_tape+','+next_state+','+next_value+','+direction +'\n')
        rules.close()

    def set_inputs(self, input):
        file = open("rules.txt", "a")
        file.write(input)
        file.close()

    def get_preset(self, option):
        with open(option+'.txt') as file:
            data = file.readlines()
        return(data)

    def set_preset(self, data):
        file = open("rules.txt", "a")
        for i in range(len(data)):
            file.write(data[i])
        file.close

    def get_rules(self):
        with open('rules.txt') as file:
            data = file.readlines()
        return(data)

    def clear_file(self):
        file = open("rules.txt", "r+")
        file.truncate(0)
        file.close()