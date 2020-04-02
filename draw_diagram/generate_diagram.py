from PySimpleAutomata import automata_IO
from draw_diagram import tb_to_diagram

dfa_example = {
    'alphabet': {'5c', '10c', 'gum'},
    'states': {'s1', 's0', 's2', 's3'},
    'initial_state': 's0',
    'accepting_states': {'s0'},
    'transitions': {
        ('s1', '5c'): 's2',
        ('s0', '5c'): 's1',
        ('s2', '10c'): 's3',
        ('s3', 'gum'): 's0',
        ('s2', '5c'): 's3',
        ('s0', '10c'): 's2',
        ('s1', '10c'): 's3'
    }
}

# automata_IO.dfa_to_dot(dfa_example, 'dfa_example', '../')

nfa_example = {
    'alphabet': {'0', '1'},
    'states': {'q0', 'q1', 'q2', 'q3'},
    'initial_states': {'q0'},
    'accepting_states': {'q3'},
    'transitions': {
        ('q0', '0'): {'q0', 'q1'},
        ('q0', '1'): {'q0', 'q2'},
        ('q1', '0'): {'q3'},
        ('q1', '1'): {'q3'},
        ('q2', '0'): {'q3'}
    }
}

automata_IO.nfa_to_dot(nfa_example, 'nfa_example')

tb_to_diagram.nfa_tb_to_diagram("nfa_transition_table.json", "nfa_transition_table")

tb_to_diagram.dfa_tb_to_diagram("dfa_transition_table.json", "dfa_transition_table")







