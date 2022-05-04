import unittest
from unittest.mock import MagicMock
from NonPolynomialChecker import NonPolynomialChecker
from FileHandlingStub import FileHandling
from TuringMachine import TuringMachine

class test_NonPolynomialChecker(unittest.TestCase):

    def test_machine_output_1(self):
        test_machine = NonPolynomialChecker('1001')
        test_machine.machine.rules_dict = {'q00': ('q1', '0', '>'), 'q10': ('q0', '0', '>'), 'q01': ('q0', '1', '>'), 'q11': ('q1', '1', '>'), 'q0': ('qAccept', '', '-')}
        test_machine.get_next_values()
        return_value = test_machine.list()
        self.assertEqual(return_value, 'qAccept')
    
    def test_machine_output_2(self):
        test_machine = NonPolynomialChecker('101001')
        test_machine.machine.rules_dict = {'q00': ('q1', '0', '>'), 'q10': ('q0', '0', '>'), 'q01': ('q0', '1', '>'), 'q11': ('q1', '1', '>'), 'q0': ('qAccept', '', '-')}
        test_machine.get_next_values()
        return_value = test_machine.list()
        self.assertEqual(return_value, 'qReject')

    def test_machine_output_NP(self):
        test_machine = NonPolynomialChecker('1001')
        test_machine.machine.rules_dict = {'q00': ('q1', '0', '>'), 'q10': ('q0', '0', '>'), 'q01': ('q0', '1', '>'), 'q11': ('q1', '1', '>'), 'q0': ('qAccept', '', '-')}
        test_machine.get_next_values()
        return_value = test_machine.NP()
        self.assertEqual(return_value, ('P', 5))


    def test_machine_output_3(self):
        test_machine = NonPolynomialChecker('1111')
        test_machine.machine.rules_dict = {'q00': ('q0', '0', '>'), 'q01': ('q1', '1', '>'), 'q10': ('q2', '0', '>'), 'q11': ('q0', '1', '>'), 'q20': ('q1', '0', '>'), 'q21': ('q2', '1', '>'), 'q0': ('qAccept', '', '-')}
        test_machine.get_next_values()
        return_value = test_machine.list()
        self.assertEqual(return_value, 'qAccept')

    def test_machine_output_4(self):
        test_machine = NonPolynomialChecker('1101')
        test_machine.machine.rules_dict = {'q00': ('q0', '0', '>'), 'q01': ('q1', '1', '>'), 'q10': ('q2', '0', '>'), 'q11': ('q0', '1', '>'), 'q20': ('q1', '0', '>'), 'q21': ('q2', '1', '>'), 'q0': ('qAccept', '', '-')}
        test_machine.get_next_values()
        return_value = test_machine.list()
        self.assertEqual(return_value, 'qReject')

    def test_machine_output_NP_2(self):
        test_machine = NonPolynomialChecker('10101')
        test_machine.machine.rules_dict = {'q00': ('q0', '0', '>'), 'q01': ('q1', '1', '>'), 'q10': ('q2', '0', '>'), 'q11': ('q0', '1', '>'), 'q20': ('q1', '0', '>'), 'q21': ('q2', '1', '>'), 'q0': ('qAccept', '', '-')}
        test_machine.get_next_values()
        return_value = test_machine.NP()
        self.assertEqual(return_value, ('P', 6))

    def test_machine_output_1_stubbing(self):
        stub_file_handling = FileHandling()
        test_machine = TuringMachine()
        test_machine.set_file_handler(stub_file_handling)
        test_machine.create_dictionary()
        test_NP = NonPolynomialChecker('1001')
        test_NP.set_Turing_machine(test_machine)
        test_NP.get_next_values()
        return_value = test_NP.list()
        self.assertEqual(return_value, 'qAccept')

    def test_machine_output_2_stubbing(self):
        stub_file_handling = FileHandling()
        test_machine = TuringMachine()
        test_machine.set_file_handler(stub_file_handling)
        test_machine.create_dictionary()
        test_NP = NonPolynomialChecker('101001')
        test_NP.set_Turing_machine(test_machine)
        test_NP.get_next_values()
        return_value = test_NP.list()
        self.assertEqual(return_value, 'qReject')

    def test_machine_output_NP_stubbing(self):
        stub_file_handling = FileHandling()
        test_machine = TuringMachine()
        test_machine.set_file_handler(stub_file_handling)
        test_machine.create_dictionary()
        test_NP = NonPolynomialChecker('1001')
        test_NP.set_Turing_machine(test_machine)
        test_NP.get_next_values()
        return_value = test_NP.NP()
        self.assertEqual(return_value, ('P', 5))

    def test_machine_output_1_mocking(self):
        test_machine = TuringMachine()
        test_machine.file_handler.get_rules = MagicMock(return_value=['q0,0,q1,0,>', 'q1,0,q0,0,>', 'q0,1,q0,1,>', 'q1,1,q1,1,>', 'q0,,qAccept,,-'])
        test_machine.create_dictionary()
        test_NP = NonPolynomialChecker('1001')
        test_NP.set_Turing_machine(test_machine)
        test_NP.get_next_values()
        return_value = test_NP.list()
        self.assertEqual(return_value, 'qAccept')
 
    
    def test_machine_output_2_mocking(self):
        test_machine = TuringMachine()
        test_machine.file_handler.get_rules = MagicMock(return_value=['q0,0,q1,0,>', 'q1,0,q0,0,>', 'q0,1,q0,1,>', 'q1,1,q1,1,>', 'q0,,qAccept,,-'])
        test_machine.create_dictionary()
        test_NP = NonPolynomialChecker('101001')
        test_NP.set_Turing_machine(test_machine)
        test_NP.get_next_values()
        return_value = test_NP.list()
        self.assertEqual(return_value, 'qReject')
    
    def test_machine_output_NP_mocking(self):
        test_machine = TuringMachine()
        test_machine.file_handler.get_rules = MagicMock(return_value=['q0,0,q1,0,>', 'q1,0,q0,0,>', 'q0,1,q0,1,>', 'q1,1,q1,1,>', 'q0,,qAccept,,-'])
        test_machine.create_dictionary()
        test_NP = NonPolynomialChecker('1001')
        test_NP.set_Turing_machine(test_machine)
        test_NP.get_next_values()
        return_value = test_NP.NP()
        self.assertEqual(return_value, ('P', 5))