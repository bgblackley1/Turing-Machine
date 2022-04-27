import tkinter as tk
from tkinter.constants import END

class tkinterclass:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Turing Machine")
        file = open("rules.txt","r+")
        self.set_delay = 1000
        self.delay = 1000
        file.truncate(0)
        file.close()
        self.rules_type_input()

    def rules_type_input(self):
        self.label = tk.Label(self.window, text="How would you like to input the rules?", font = ("Calbri Body", 10))
        self.label.grid(column=0, row=0, columnspan=2)
        self.single_button = tk.Button(text ="One at a time", command = self.One_input_at_a_time)
        self.single_button.grid(column = 0, row = 1)
        self.single_button = tk.Button(text ="Many in a text box", command = self.Many_inputs)
        self.single_button.grid(column = 1, row = 1)
        self.window.mainloop()

    def One_input_at_a_time(self):
        self.window.destroy()
        self.window = tk.Tk()
        self.label = tk.Label(self.window, text="Inputting one rule at a time")
        self.label.grid(column=0, row=0)
        self.state_1_label = tk.Label(self.window, text="Current State (eg q0):")
        self.state_1_label.grid(column= 0 , row = 1)
        self.state_1 = tk.Entry()
        self.state_1.grid(column = 1, row = 1)

        self.value = tk.Label(self.window, text="Current Value (eg 0):")
        self.value.grid(column= 2 , row = 1)
        self.value_input = tk.Entry()
        self.value_input.grid(column = 3, row = 1)

        self.state_2_label = tk.Label(self.window, text="Next State (eg q1):")
        self.state_2_label.grid(column= 4 , row = 1)
        self.state_2 = tk.Entry()
        self.state_2.grid(column = 5, row = 1)

        self.value2 = tk.Label(self.window, text="Next Value (eg 1):")
        self.value2.grid(column= 6 , row = 1)
        self.value_input2 = tk.Entry()
        self.value_input2.grid(column = 7, row = 1)

        self.direction = tk.Label(self.window, text="Direction to Move (eg >):")
        self.direction.grid(column= 8 , row = 1)
        self.direction_entry = tk.Entry()
        self.direction_entry.grid(column = 9, row = 1)

        self.single_button = tk.Button(text ="Submit Rule", command = self.fetch_input)
        self.single_button.grid(column = 0, row = 2)

        self.single_button = tk.Button(text ="Next", command = self.starting_tape)
        self.single_button.grid(column = 1, row = 2)

    def fetch_input(self):
        v1 = self.state_1.get()
        v2 = self.value_input.get()
        v3 = self.state_2.get()
        v4 = self.value_input2.get()
        v5 = self.direction_entry.get()
        f = open("rules.txt", "a")
        f.writelines(v1+','+v2+','+v3+','+v4+','+v5 +'\n')
        f.close()
        row = 3
        self.labels = []
        with open('rules.txt') as f:
            data = f.readlines()
        for rule in data:
            self.rule = tk.Label(self.window, text = rule)
            self.rule.grid(row = row, column = 0)
            row += 1

    def fetch_inputs(self):
        v = self.text_box.get("0.0",END)
        f = open("rules.txt", "a")
        f.write(v)
        f.close()

    def Many_inputs(self):
        self.window.destroy()
        self.window = tk.Tk()
        self.label2 = tk.Label(self.window, text="Here is an example input:")
        self.label2.grid(column = 0, row = 0)
        self.label1 = tk.Label(self.window, text="'q0,0,q1,0,>', please follow this format, I would advise using clear accepted and rejected state")
        self.label1.grid(column = 0, row = 1)
        self.label1 = tk.Label(self.window, text="please finish program with direction being -")
        self.label1.grid(column = 0, row = 2)
        self.text_box = tk.Text()
        self.text_box.grid(column = 0, row = 3)
        self.submit = tk.Button(text ="submit", command = self.fetch_inputs)
        self.submit.grid(column = 0, row = 4)
        self.single_button = tk.Button(text ="Next", command = self.starting_tape)
        self.single_button.grid(column = 1, row = 4)
        clicked = tk.StringVar()
        clicked.set( "Pre-set" )
        options = ['Divisible_by_3', 'Even_number_of_zeroes', 'Palindrome_checker']
        self.presets = tk.OptionMenu(self.window ,clicked , *options, command=self.input_preset)
        self.presets.grid(column=1, row=3)

    def input_preset(self, option):
        with open(option+'.txt') as f:
            data = f.readlines()
        self.text_box.delete(0.0, 'end')
        f = open("rules.txt", "a")
        for i in range(len(data)):
            f.write(data[i])
            self.text_box.insert(float(i+1), data[i])
        f.close
        
    def starting_tape(self):
        self.window.destroy()
        self.window = tk.Tk()
        self.tape = []
        self.label = tk.Label(self.window, text="Turing machine", font = ("Calbri Body", 20))
        self.label.grid(column = 9, row = 0, columnspan = 5, sticky = 'nsew')
        self.state = tk.Label(self.window, text="state: q0", font = ("Calbri Body", 15))
        self.state.grid(column = 14, row = 0, columnspan = 5, sticky = 'nsew')
        for x in range(1, 22):
            tape_tile = tk.Button(text = '', command = None, height = 3, width = 6, font = ("Calbri Body", 12))
            tape_tile.grid(row = 4, column = x)
            self.tape.append(tape_tile)
        self.label = tk.Label(self.window, text="V", font = ("Calbri Body", 15))
        self.label.grid(column = 11, row = 2)
        self.label1 = tk.Label(self.window, text="What data would you like on the tape:", font = ("Calbri Body", 15))
        self.label1.grid(column = 5, row = 6, columnspan = 7)
        self.entry = tk.Entry(font = ("Calbri Body", 15))
        self.entry.grid(column = 11, row = 6, columnspan=6, ipadx=7, ipady=7)
        self.button = tk.Button(text ="Submit", command = self.add_input_to_tape, height=2,width=6,font = ("Calbri Body", 10))
        self.button.grid(column = 17, row = 6)
        self.button = tk.Button(text ="Run", command = self.setup_machine, height=2,width=6,font = ("Calbri Body", 10))
        self.button.grid(column = 20, row = 6)
        self.speed = tk.Scale(self.window, from_=0, to=1000, orient='horizontal', command=self.change_delay)
        self.speed.grid(column = 5, row = 0, columnspan=3, sticky='we')
        self.speedlabel = tk.Label(self.window, text="speed (%): ", font = ("Calbri Body", 15))
        self.speedlabel.grid(column = 2, row = 0, columnspan=3)

    def add_input_to_tape(self):
            self.input_to_tape = self.entry.get()
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
        self.state['text'] = 'state: q0'
        self.machine = Turing_Machine()
        self.direction = None
        self.input_to_tape = list(self.input_to_tape)
        self.window.after(10, self.run_machine)

    def run_machine(self):
        if self.direction != '-' and self.runs < 1000:
            state, self.value, self.direction = self.machine.run_machine(self.tape[10]['text'])
            self.state['text'] = 'state: ' + state
            self.runs += 1
            self.window.after(self.delay, self.update_pointer_value)
        elif self.runs >= 1000:
            self.state['text'] = 'state: Timout'
            
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

