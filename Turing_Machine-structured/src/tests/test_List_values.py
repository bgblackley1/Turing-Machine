import unittest
from unittest.mock import MagicMock
from FileHandlingStub import FileHandling
from NPChecker import NPChecker
from List_Values import List_Values
from Turing_machine import Turing_Machine

class test_NPChecker(unittest.TestCase):

    def test_machine_output_1(self):
        test_machine = NPChecker('0')
        test_machine.machine.rules_dict = {'q00': ('q1', '0', '>'), 'q10': ('q0', '0', '>'), 'q01': ('q0', '1', '>'), 'q11': ('q1', '1', '>'), 'q0': ('qAccept', '', '-')}
        test_list = List_Values()
        test_list.set_np_checker(test_machine)
        return_value = test_list.return_list(3)
        exp_value = [[0, '0', 'qReject'], [1, '1', 'qAccept'], [2, '10', 'qReject'], [3, '11', 'qAccept']]
        self.assertEqual(return_value, exp_value)

    def test_machine_output_2(self):
        test_machine = NPChecker('0')
        test_machine.machine.rules_dict = {'q00': ('q0', '0', '>'), 'q01': ('q1', '1', '>'), 'q10': ('q2', '0', '>'), 'q11': ('q0', '1', '>'), 'q20': ('q1', '0', '>'), 'q21': ('q2', '1', '>'), 'q0': ('qAccept', '', '-')}
        test_list = List_Values()
        test_list.set_np_checker(test_machine)
        return_value = test_list.return_list(6)
        exp_value = [[0, '0', 'qAccept'], [1, '1', 'qReject'], [2, '10', 'qReject'], [3, '11', 'qAccept'], [4, '100', 'qReject'], [5, '101', 'qReject'], [6, '110', 'qAccept']]
        self.assertEqual(return_value, exp_value)

    def test_machine_output_1_stubbing(self):
        stub_file_handling = FileHandling()
        test_machine = Turing_Machine()
        test_machine.set_file_handler(stub_file_handling)
        test_machine.create_dictionary()
        test_NP = NPChecker('0')
        test_NP.set_Turing_machine(test_machine)
        test_list = List_Values()
        test_list.set_np_checker(test_NP)
        return_value = test_list.return_list(3)
        exp_value = [[0, '0', 'qReject'], [1, '1', 'qAccept'], [2, '10', 'qReject'], [3, '11', 'qAccept']]
        self.assertEqual(return_value, exp_value)
    
    def test_machine_output_1_mocking(self):
        test_machine = Turing_Machine()
        test_machine.file_handler.get_rules = MagicMock(return_value=['q0,0,q1,0,>', 'q1,0,q0,0,>', 'q0,1,q0,1,>', 'q1,1,q1,1,>', 'q0,,qAccept,,-'])
        test_machine.create_dictionary()
        test_NP = NPChecker('0')
        test_NP.set_Turing_machine(test_machine)
        test_list = List_Values()
        test_list.set_np_checker(test_NP)
        return_value = test_list.return_list(3)
        exp_value = [[0, '0', 'qReject'], [1, '1', 'qAccept'], [2, '10', 'qReject'], [3, '11', 'qAccept']]
        self.assertEqual(return_value, exp_value)