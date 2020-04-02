from PySimpleAutomata import automata_IO
import json


def nfa_tb_to_diagram(json_filename, output_filename):
    with open(json_filename) as json_file:
        nfa_tb = json.load(json_file)

    # construct nfa parameters
    alphabet = nfa_tb["alphabet"]
    states = nfa_tb["states"]
    nfa = dict()
    nfa["alphabet"] = set(alphabet)
    nfa["states"] = set(states)
    nfa["initial_states"] = set(nfa_tb["initial_states"])
    nfa["accepting_states"] = set(nfa_tb["accepting_states"])

    # construct nfa transitions from transition table
    transition_table = nfa_tb["transition_table"]
    if len(transition_table) != len(states):
        raise Exception("number of rows in transition table not equal to number of states")
    if len(transition_table[0]) != len(alphabet):
        raise Exception("number of columns in transition table not equal to number of elements in alphabet")

    transitions = dict()
    for i in range(len(states)):
        for j in range(len(alphabet)):
            if len(transition_table[i][j]) > 0:
                transitions[(states[i], alphabet[j])] = set(transition_table[i][j])
    nfa["transitions"] = transitions
    print(nfa)
    automata_IO.nfa_to_dot(nfa, output_filename)


def dfa_tb_to_diagram(json_filename, output_filename):
    with open(json_filename) as json_file:
        dfa_tb = json.load(json_file)

    # construct nfa parameters
    alphabet = dfa_tb["alphabet"]
    states = dfa_tb["states"]
    dfa = dict()
    dfa["alphabet"] = set(alphabet)
    dfa["states"] = set(states)
    dfa["initial_state"] = dfa_tb["initial_state"]
    dfa["accepting_states"] = set(dfa_tb["accepting_states"])

    # construct dfa transitions from transition table
    transition_table = dfa_tb["transition_table"]
    if len(transition_table) != len(states):
        raise Exception("number of rows in transition table not equal to number of states")
    if len(transition_table[0]) != len(alphabet):
        raise Exception("number of columns in transition table not equal to number of elements in alphabet")

    transitions = dict()
    for i in range(len(states)):
        for j in range(len(alphabet)):
            if len(transition_table[i][j]) > 0:
                transitions[(states[i], alphabet[j])] = transition_table[i][j]
    dfa["transitions"] = transitions
    print(dfa)
    automata_IO.dfa_to_dot(dfa, output_filename)

