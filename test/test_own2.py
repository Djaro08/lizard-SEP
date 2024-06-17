import unittest
from lizard_languages.erlang import ErlangReader, ErlangStates
from lizard_languages.code_reader import CodeReader, CodeStateMachine

class TestErlangReader(unittest.TestCase):

    def setUp(self):
        self.context = type('Context', (object,), {
            'stacked_functions': [],
            'current_function': type('Function', (object,), {'name': '', 'cyclomatic_complexity': 1})(),
            'global_pseudo_function': type('Function', (object,), {'cyclomatic_complexity': 1})(),
            'push_new_function': lambda self, name: self.context.stacked_functions.append(type('Function', (object,), {'name': name, 'cyclomatic_complexity': 1})()),
            'end_of_function': lambda self: None,
            'add_to_long_function_name': lambda self, name: None,
            'parameter': lambda self, token: None,
            'add_condition': lambda self, cond: None,
        })()
        self.reader = ErlangReader(self.context)

    def test_state_nested_end_with_dot(self):
        state_machine = ErlangStates(self.context)
        self.context.stacked_functions.append(type('Function', (object,), {'name': 'fun', 'cyclomatic_complexity': 1})())
        state_machine._state = state_machine._state_nested_end
        state_machine._state('.')
        self.assertEqual(state_machine._state, state_machine._state_global)

if __name__ == "__main__":
    unittest.main()
