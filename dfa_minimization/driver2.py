from dfa_minimization import DFA_min
from draw_diagram import tb_to_diagram

DFA_min.dfa_minimization("dfa_before_2.json", "dfa_after_2.json")

tb_to_diagram.dfa_tb_to_diagram("dfa_after_2.json", "dfa_after_2")
