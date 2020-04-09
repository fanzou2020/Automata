from dfa_minimization import DFA_min
from draw_diagram import tb_to_diagram

# DFA_min.dfa_minimization("dfa_before_2.json", "dfa_after_2.json")
#
# tb_to_diagram.dfa_tb_to_diagram("dfa_before_2.json", "dfa_before_2")
#
# tb_to_diagram.dfa_tb_to_diagram("dfa_after_2.json", "dfa_after_2")

DFA_min.dfa_minimization("example2.json", "example2_after.json")

tb_to_diagram.dfa_tb_to_diagram("example2_after.json", "example2_after")

DFA_min.dfa_minimization("example3.json", "example3_after.json")

tb_to_diagram.dfa_tb_to_diagram("example3_after.json", "example3_after")
