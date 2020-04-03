import json
from draw_diagram import tb_to_diagram


# tb_to_diagram.dfa_tb_to_diagram("dfa_before.json", "dfa_before")

# input the json file name of dfa transition table before minimization,
# and the json file name of dfa transition table after minimization.
# This function will create a new json file with the name dfa_after_filename
def dfa_minimization(dfa_before_filename, dfa_after_filename):
    with open(dfa_before_filename) as json_file:
        dfa_before = json.load(json_file)

    before_initial = dfa_before["initial_state"]
    before_accepting = dfa_before["accepting_states"]
    before_alphabet = dfa_before["alphabet"]
    before_states = dfa_before["states"]
    before_transition_table = dfa_before["transition_table"]

    # apply Moore's algorithm
    # The initial partition
    pi = []  # size = len(states)
    for x in before_states:
        if x in before_accepting:
            pi.append("1")
        else:
            pi.append("0")

    # repeat until |pi_i| == |pi_i-1|
    while True:
        aux = pi.copy()

        # update pi
        for i in range(len(aux)):
            for j in range(len(before_alphabet)):
                index = before_states.index(before_transition_table[i][j])  # index of destination state
                pi[i] = pi[i] + aux[index]

        # determine the number of partition in pi
        num_partition_old = len(set(aux))
        num_partition_new = len(set(pi))

        # if |pi_i| == |pi_i-1|, break
        if num_partition_old == num_partition_new:
            break

    print(aux)
    print(pi)

    # construct the transition table from aux and pi
    states_dict = dict()  # key is "000111..", value is the index of state in before_states
    for i in range(len(aux)):
        if aux[i] in states_dict:
            states_dict[aux[i]].append(i)
        else:
            states_dict[aux[i]] = [i]

    print(states_dict)

    # use states_dict and pi to construct transition table
    string_len = len(aux[0])  # length of each state in aux
    tb = []
    for x in states_dict:
        state_index = states_dict[x][0]  # the first element in state_dict list
        tb_row = []
        for i in range(0, len(before_alphabet)):
            string_i = pi[state_index][(i+1)*string_len: (i+2)*string_len]
            tb_row.append(states_dict[string_i])
        tb.append(tb_row)

    # output constructed minimum dfa to json file
    dfa_after = dict()
    dfa_after["alphabet"] = dfa_before["alphabet"]

    after_states = [states_dict[x] for x in states_dict]
    for i in range(len(after_states)):
        for j in range(len(after_states[i])):
            after_states[i][j] = before_states[after_states[i][j]]
        after_states[i] = str(set(after_states[i]))
    dfa_after["states"] = after_states

    after_initial = []
    for x in after_states:
        if before_initial in x:
            after_initial = x
            break
    dfa_after["initial_state"] = after_initial

    # if the intersection with accepting states is not empty, it is the new accepting states
    after_accepting = []
    for x in after_states:
        if len(set(before_accepting).intersection(set(x))) != 0:
            after_accepting.append(x)
    dfa_after["accepting_states"] = after_accepting

    for i in range(len(tb)):
        for j in range(len(before_alphabet)):
            tb[i][j] = str(set(tb[i][j]))
    dfa_after["transition_table"] = tb

    # output dfa_after to json file
    with open(dfa_after_filename, 'w') as json_after:
        json.dump(dfa_after, json_after)










