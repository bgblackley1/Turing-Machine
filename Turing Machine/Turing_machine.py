import tkinter as tk
from tkinter.constants import END

class tkinterclass:

    def __init__(self):
        self.window = tk.Tk()
        self.file_handler = FileHandling()
        self.window.title("Turing Machine")
        file = open("rules.txt","r+")
        self.set_delay = 1000
        self.delay = 1000
        file.truncate(0)
        file.close()
        self.rules_type_input()

    def rules_type_input(self):
        self.input_type_question_label = tk.Label(self.window, text="How would you like to input the rules?", font = ("Calbri Body", 10))
        self.input_type_question_label.grid(column=0, row=0, columnspan=2)
        self.single_input_button = tk.Button(text ="One at a time", command = self.One_input_at_a_time)
        self.single_input_button.grid(column = 0, row = 1)
        self.many_input_button = tk.Button(text ="Many in a text box", command = self.Many_inputs)
        self.many_input_button.grid(column = 1, row = 1)
        self.window.mainloop()

    def One_input_at_a_time(self):
        self.window.destroy()
        self.window = tk.Tk()
        self.title_label = tk.Label(self.window, text="Inputting one rule at a time")
        self.title_label.grid(column=0, row=0)

        self.current_state_label = tk.Label(self.window, text="Current State (eg q0):")
        self.current_state_label.grid(column= 0 , row = 1)
        self.current_state = tk.Entry()
        self.current_state.grid(column = 1, row = 1)

        self.value_on_tape_label = tk.Label(self.window, text="Current Value (eg 0):")
        self.value_on_tape_label.grid(column= 2 , row = 1)
        self.value_on_tape = tk.Entry()
        self.value_on_tape.grid(column = 3, row = 1)

        self.next_state_label = tk.Label(self.window, text="Next State (eg q1):")
        self.next_state_label.grid(column= 4 , row = 1)
        self.next_state = tk.Entry()
        self.next_state.grid(column = 5, row = 1)

        self.next_value_label = tk.Label(self.window, text="Next Value (eg 1):")
        self.next_value_label.grid(column= 6 , row = 1)
        self.next_value = tk.Entry()
        self.next_value.grid(column = 7, row = 1)

        self.direction_label = tk.Label(self.window, text="Direction to Move (eg >):")
        self.direction_label.grid(column= 8 , row = 1)
        self.direction = tk.Entry()
        self.direction.grid(column = 9, row = 1)

        self.submit = tk.Button(text ="Submit Rule", command = self.fetch_input)
        self.submit.grid(column = 0, row = 2)

        self.next = tk.Button(text ="Next", command = self.starting_tape)
        self.next.grid(column = 1, row = 2)

    def fetch_input(self):
        current_state = self.current_state.get()
        value_on_tape = self.value_on_tape.get()
        next_state = self.next_state.get()
        next_value = self.next_value.get()
        direction = self.direction.get()
        self.file_handler(current_state,value_on_tape,next_state,next_value,direction)
        self.display_rules()

    def display_rules(self):
        row = 3
        with open('rules.txt') as file:
            rules = file.readlines()
        for rule in rules:
            self.rule = tk.Label(self.window, text = rule)
            self.rule.grid(row = row, column = 0)
            row += 1

    def Many_inputs(self):
        self.window.destroy()
        self.window = tk.Tk()
        self.example_label = tk.Label(self.window, text="Here is an example input:")
        self.example_label.grid(column = 0, row = 0)
        self.format_example_label = tk.Label(self.window, text="'q0,0,q1,0,>', please follow this format, I would advise using clear accepted and rejected state")
        self.format_example_label.grid(column = 0, row = 1)
        self.ending_instruction_label = tk.Label(self.window, text="please finish program with direction being -")
        self.ending_instruction_label.grid(column = 0, row = 2)
        self.text_box = tk.Text()
        self.text_box.grid(column = 0, row = 3)
        self.submit = tk.Button(text ="submit", command = self.fetch_inputs)
        self.submit.grid(column = 0, row = 4)
        self.next = tk.Button(text ="Next", command = self.starting_tape)
        self.next.grid(column = 1, row = 4)
        pre_set = tk.StringVar()
        pre_set.set( "Pre-set" )
        options = ['Divisible_by_3', 'Even_number_of_zeroes', 'Palindrome_checker']
        self.presets = tk.OptionMenu(self.window ,pre_set , *options, command=self.input_preset)
        self.presets.grid(column=1, row=3)

    def fetch_inputs(self):
        text_entry = self.text_box.get("0.0",END)
        self.file_handler.set_inputs(text_entry)
    
    def input_preset(self, option):
        data = self.file_handler.get_preset(option)
        self.text_box.delete(0.0, 'end')
        for i in range(len(data)):
            self.text_box.insert(float(i+1), data[i])
        self.file_handler.set_preset(data)
        
    def starting_tape(self):
        self.window.destroy()
        self.window = tk.Tk()
        self.tape = []
        self.title_label = tk.Label(self.window, text="Turing machine", font = ("Calbri Body", 20))
        self.title_label.grid(column = 9, row = 0, columnspan = 5, sticky = 'nsew')
        self.state_label = tk.Label(self.window, text="state: q0", font = ("Calbri Body", 15))
        self.state_label.grid(column = 14, row = 0, columnspan = 5, sticky = 'nsew')
        for x in range(1, 22):
            tape_tile = tk.Button(text = '', command = None, height = 3, width = 6, font = ("Calbri Body", 12))
            tape_tile.grid(row = 4, column = x)
            self.tape.append(tape_tile)
        self.pointer_label = tk.Label(self.window, text="V", font = ("Calbri Body", 15))
        self.pointer_label.grid(column = 11, row = 2)
        self.input_label = tk.Label(self.window, text="What data would you like on the tape:", font = ("Calbri Body", 15))
        self.input_label.grid(column = 5, row = 6, columnspan = 7)
        self.input_entry = tk.Entry(font = ("Calbri Body", 15))
        self.input_entry.grid(column = 11, row = 6, columnspan=6, ipadx=7, ipady=7)
        self.submit = tk.Button(text ="Submit", command = self.add_input_to_tape, height=2,width=6,font = ("Calbri Body", 10))
        self.submit.grid(column = 17, row = 6)
        self.run = tk.Button(text ="Run", command = self.setup_machine, height=2,width=6,font = ("Calbri Body", 10))
        self.run.grid(column = 20, row = 6)
        self.speed_scale = tk.Scale(self.window, from_=0, to=1000, orient='horizontal', command=self.change_delay)
        self.speed_scale.grid(column = 5, row = 0, columnspan=3, sticky='we')
        self.speed_scale_label = tk.Label(self.window, text="speed (%): ", font = ("Calbri Body", 15))
        self.speed_scale_label.grid(column = 2, row = 0, columnspan=3)

    def add_input_to_tape(self):
            self.input_to_tape = self.input_entry.get()
            for i in range(len(self.tape)):
                self.tape[i]['text'] = ''
            for i in range(10, 21):
                try: 
                    self.tape[i]['text'] = self.input_to_tape[i-10]
                except: 
                    self.tape[i]['text'] = ''

    def setup_machine(self):
        self.runs = 0
        self.back_pointer = 10
        self.state_label['text'] = 'state: q0'
        self.machine = Turing_Machine()
        self.direction = None
        self.input_to_tape = list(self.input_to_tape)
        self.window.after(10, self.run_machine)

    def run_machine(self):
        if self.direction != '-' and self.runs < 1000:
            state, self.value, self.direction = self.machine.run_machine(self.tape[10]['text'])
            self.state_label['text'] = 'state: ' + state
            self.runs += 1
            self.window.after(self.delay, self.update_pointer_value)
        elif self.runs >= 1000:
            self.state_label ['text'] = 'state: Timout'
            
    def update_pointer_value(self):
        self.tape[10]['text'] = self.value
        if 10-self.back_pointer < len(self.input_to_tape) and 10-self.back_pointer >= 0:
            self.input_to_tape[10-self.back_pointer] = self.value
        elif 10-self.back_pointer < len(self.input_to_tape):
            if self.value != '':
                self.input_to_tape.append(self.value)
        else:
            if self.value != '':
                self.input_to_tape.insert(0, self.value)
        self.window.after(self.delay, self.update_tape)
    
    def update_tape(self):
        if self.direction == '>':
            self.back_pointer -= 1
            for i in range(self.back_pointer, 21):
                if i >= 0:
                    try: 
                        self.tape[i]['text'] = self.input_to_tape[i-self.back_pointer]
                    except: 
                        self.tape[i]['text'] = ''
        elif self.direction == '<':
            self.back_pointer += 1
            for i in range(self.back_pointer, 21):
                if i >= 0:
                    try: 
                        self.tape[i]['text'] = self.input_to_tape[i-self.back_pointer]
                    except: 
                        self.tape[i]['text'] = ''
        self.window.after(self.delay, self.run_machine)
    
    def change_delay(self, slider):
        try:
            self.delay = int(self.set_delay / (int(slider) / 100))
        except:
            self.delay = self.set_delay / 100
            
class FileHandling():
        
    def set_rule(self, current_state,value_on_tape,next_state,next_value,direction):
        rules = open("rules.txt", "a")
        current_state,value_on_tape,next_state,next_value,direction = self.fetch_input()
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
    
    def input_preset(self, option):
        data = self.get_preset(option)
        self.text_box.delete(0.0, 'end')
        for i in range(len(data)):
            self.text_box.insert(float(i+1), data[i])
        self.set_preset(data)

    def set_preset(self,data):
        file = open("rules.txt", "a")
        for i in range(len(data)):
            file.write(data[i])
        file.close

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

machine = tkinterclass()