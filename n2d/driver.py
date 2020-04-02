from n2d import nfa_to_dfa
from draw_diagram import tb_to_diagram
from PySimpleAutomata import automata_IO
from PySimpleAutomata import NFA

# draw diagram of nfa
tb_to_diagram.nfa_tb_to_diagram("nfa_transition_table.json", "nfa_transition_table")

# transform nfa to dfa
nfa_to_dfa.nfa_to_dfa("nfa_transition_table.json", "dfa_transition_table.json")

# draw diagram of dfa
tb_to_diagram.dfa_tb_to_diagram("dfa_transition_table.json", "dfa_transition_table")

# use PySimpleAutomata to check correctness
nfa = automata_IO.nfa_dot_importer("nfa_transition_table.dot")
dfa = NFA.nfa_determinization(nfa)
automata_IO.dfa_to_dot(dfa, "dfa_pysimpleautoma")


# draw diagram of nfa
tb_to_diagram.nfa_tb_to_diagram("nfa_test_tb.json", "nfa_test_tb")

# transform nfa to dfa
nfa_to_dfa.nfa_to_dfa("nfa_test_tb.json", "dfa_test_tb.json")

# draw diagram of dfa
tb_to_diagram.dfa_tb_to_diagram("dfa_test_tb.json", "dfa_test_tb")

# use PySimpleAutomata to check correctness
nfa = automata_IO.nfa_dot_importer("nfa_test_tb.dot")
dfa = NFA.nfa_determinization(nfa)
automata_IO.dfa_to_dot(dfa, "dfa_pysimpleautoma_test")
