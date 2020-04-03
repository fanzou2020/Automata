import json


def nfa_to_dfa(nfa_tb_file, output_filename):
    with open(nfa_tb_file) as json_file:
        nfa = json.load(json_file)

    nfa_initial = nfa["initial_states"]
    nfa_accepting = nfa["accepting_states"]
    alphabet = nfa["alphabet"]
    nfa_states = nfa["states"]
    nfa_tb = nfa["transition_table"]

    dfa_states = []  # all the states occurred
    queue = []  # maintain a queue, contain sub-sets

    dfa_initial = set(nfa_initial)  # initial state, a set
    queue.append(dfa_initial)  # add initial state to queue
    dfa_states.append(dfa_initial)  # add initial state to set

    # construct dfa transition table
    dfa_transition_table = []  # dfa transition table
    while len(queue) > 0:
        curr = queue.pop(0)  # dequeue

        # calculate the reachable states form curr
        c = closure(curr, nfa_states, alphabet, nfa_tb)

        # add this row to dfa transition table
        dfa_transition_table.append(c)

        # check if the closure of states is in the dfa_states
        # if not, add the subset to queue and dfa_states
        for x in c:
            if x not in dfa_states:
                dfa_states.append(x)
                queue.append(x)

    # print(dfa_transition_table)

    # dfa accepting states, if the intersection between dfa_states and nfa accepting states
    # is not empty, then add it to dfa accepting states
    dfa_accepting = []
    for x in dfa_states:
        if len(set(nfa_accepting).intersection(x)) != 0:
            dfa_accepting.append(x)

    # print(dfa_accepting)

    dfa = dict()
    dfa["alphabet"] = alphabet
    dfa["states"] = dfa_states
    dfa["initial_state"] = dfa_initial
    dfa["accepting_states"] = dfa_accepting
    dfa["transition_table"] = dfa_transition_table

    dfa_json = dump2json(dfa)

    with open(output_filename, 'w') as output:
        json.dump(dfa_json, output)


def dump2json(dfa):
    dfa_json = {"alphabet": dfa["alphabet"], "initial_state": str(dfa["initial_state"])}

    states = []
    for x in dfa["states"]:
        states.append(str(x))
    dfa_json["states"] = states

    accepting_states = []
    for x in dfa["accepting_states"]:
        accepting_states.append(str(x))
    dfa_json["accepting_states"] = accepting_states

    dfa_transition_table = dfa["transition_table"]
    json_transition_table = []
    for i in range(len(dfa_transition_table)):
        json_transition_table.append([str(dfa_transition_table[i][j]) for j in range(len(dfa_transition_table[0]))])
    dfa_json["transition_table"] = json_transition_table

    return dfa_json


# the reachable states from curr set of states,
# return a list whose items are the reachable set of states
def closure(curr, nfa_states, alphabet, nfa_tb):
    out = []
    for k in range(len(alphabet)):
        s = set()
        for x in curr:
            rowNum = nfa_states.index(x)
            r = set(nfa_tb[rowNum][k])
            s = s.union(r)
        out.append(s)
    return out
