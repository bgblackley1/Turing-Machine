import unittest
from unittest.mock import MagicMock
from src.FileHandling import FileHandling
from src.Turing_machine import Turing_Machine

class test_NPChecker(unittest.TestCase):

    def test_machine_output_1(self):
        test_machine = Turing_Machine()
        test_machine.rules_dict = {'q00': ('q1', '0', '>')}
        return_value = test_machine.run_machine('0')
        self.assertEqual(return_value, ('q1', '0', '>'))

    def test_machine_output_2(self):
        test_machine = Turing_Machine()
        test_machine.rules_dict = {'q00': ('q0', '1', '<')}
        return_value = test_machine.run_machine('0')
        self.assertEqual(return_value, ('q0', '1', '<'))
    
    def test_machine_output_3(self):
        test_machine = Turing_Machine()
        test_machine.rules_dict = {'q10': ('q1', '0', '>')}
        return_value = test_machine.run_machine('0')
        self.assertEqual(return_value, ('qReject', '0', '-'))

    def test_create_dictionary(self):
        file_handler = FileHandling()
        file_handler.get_rules = MagicMock(return_value=['q0,0,q1,0,>\n'])
        test_machine = Turing_Machine()
        test_machine.set_file_handler(file_handler)
        test_machine.rules = []
        test_machine.create_dictionary()
        rules = [['q0', '0', 'q1', '0', '>\n']]
        self.assertEqual(rules, test_machine.rules)

    def test_machine_output_1_stubbing(self):
        stub_file_handling = FileHandling()
        test_machine = Turing_Machine()
        test_machine.set_file_handler(stub_file_handling)
        test_machine.create_dictionary()
        return_value = test_machine.run_machine('0')
        self.assertEqual(return_value, ('q1', '0', '>'))

    def test_machine_output_2_stubbing(self):
        stub_file_handling = FileHandling()
        test_machine = Turing_Machine()
        test_machine.set_file_handler(stub_file_handling)
        test_machine.create_dictionary()
        return_value = test_machine.run_machine('1')
        self.assertEqual(return_value, ('q0','1','>'))

    def test_machine_output_3_stubbing(self):
        stub_file_handling = FileHandling()
        test_machine = Turing_Machine()
        test_machine.set_file_handler(stub_file_handling)
        test_machine.create_dictionary()
        return_value = test_machine.run_machine('2')
        self.assertEqual(return_value, ('qReject', '2', '-'))

    def test_machine_output_1_mocking(self):
        test_machine = Turing_Machine()
        test_machine.file_handler.get_rules = MagicMock(return_value=['q0,0,q1,0,>', 'q1,0,q0,0,>', 'q0,1,q0,1,>', 'q1,1,q1,1,>', 'q0,,qAccept,,-'])
        test_machine.create_dictionary()
        return_value = test_machine.run_machine('0')
        self.assertEqual(return_value, ('q1', '0', '>'))

    def test_machine_output_2_mocking(self):
        test_machine = Turing_Machine()
        test_machine.file_handler.get_rules = MagicMock(return_value=['q0,0,q1,0,>', 'q1,0,q0,0,>', 'q0,1,q0,1,>', 'q1,1,q1,1,>', 'q0,,qAccept,,-'])
        test_machine.create_dictionary()
        return_value = test_machine.run_machine('1')
        self.assertEqual(return_value, ('q0','1','>'))

    def test_machine_output_3_mocking(self):
        test_machine = Turing_Machine()
        test_machine.file_handler.get_rules = MagicMock(return_value=['q0,0,q1,0,>', 'q1,0,q0,0,>', 'q0,1,q0,1,>', 'q1,1,q1,1,>', 'q0,,qAccept,,-'])
        test_machine.create_dictionary()
        return_value = test_machine.run_machine('2')
        self.assertEqual(return_value, ('qReject', '2', '-'))