import unittest
from unittest.mock import MagicMock
from NPChecker import NPChecker
from FileHandling import FileHandling
from Turing_machine import Turing_Machine
from List_Values import List_Values
from Turing_machine_tkinter import tkinterclass

class test_NPChecker(unittest.TestCase):

    def test_machine_output_1(self):
        test_machine = NPChecker('1001')
        test_machine.machine.rules = [['q0', '0', 'q1', '0', '>\n'], ['q1', '0', 'q0', '0', '>\n'], ['q0', '1', 'q0', '1', '>\n'], ['q1', '1', 'q1', '1', '>\n'], ['q0', '', 'qAccept', '', '-']]
        test_machine.get_next_values()
        return_value = test_machine.list()
        self.assertEqual(return_value, 'qAccept')


    def test_machine_output_1(self):
        test_machine = NPChecker('1001')
        test_machine.machine.rules = [['q0', '0', 'q1', '0', '>\n'], ['q1', '0', 'q0', '0', '>\n'], ['q0', '1', 'q0', '1', '>\n'], ['q1', '1', 'q1', '1', '>\n'], ['q0', '', 'qAccept', '', '-']]
        test_machine.get_next_values()
        return_value = test_machine.NP()
        self.assertEqual(return_value, ('P', 5))

