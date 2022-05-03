from logging import FileHandler
import unittest
from unittest.mock import MagicMock
from NPChecker import NPChecker
from FileHandling import FileHandling
from Turing_machine import Turing_Machine
from List_Values import List_Values
from Turing_machine_tkinter import tkinterclass

class test_NPChecker(unittest.TestCase):

    def test_machine_output_1(self):
        test_machine = Turing_Machine()
        test_machine.rules = [['q0', '0', 'q1', '0', '>\n'], ['q1', '0', 'q0', '0', '>\n'], ['q0', '1', 'q0', '1', '>\n'], ['q1', '1', 'q1', '1', '>\n'], ['q0', '', 'qAccept', '', '-']]
        return_value = test_machine.run_machine('0')
        self.assertEqual(return_value, ('q1', '0', '>'))

    def test_create_dictionary(self):
        file_handler = FileHandling()
        file_handler.set_inputs('q0,0,q1,0,>')
        test_machine = Turing_Machine()
        rules = ['q0', '0', 'q1', '0', '>\n']
        self.assertEqual(rules, test_machine.rules)
