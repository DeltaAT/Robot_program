from automata.fa.dfa import DFA

dfa = DFA(
    # 4 mögliche Zustände
    states={'q0', 'q1', 'q2', 'q3'},

    # alle Möglichen / Erlaubten Zustände
    input_symbols={'1', '#', 'F', 'L', 'R'},

    # start bei q0
    initial_state='q0',

    # nur bei q3 enden
    final_states={'q3'},

    # alle Übergänge
    transitions={
        'q0': {'1': 'q1', '#': 'q2', 'F': 'q2', 'L': 'q2', 'R': 'q2'},
        'q1': {'1': 'q1', '#': 'q3', 'F': 'q2', 'L': 'q2', 'R': 'q2'},
        'q2': {'1': 'q2', '#': 'q2', 'F': 'q2', 'L': 'q2', 'R': 'q2'},
        'q3': {'1': 'q2', '#': 'q2', 'F': 'q3', 'L': 'q3', 'R': 'q3'},
    }
)

def check_robot(robot:str):
    return dfa.accepts_input(robot)

# print(dfa.accepts_input("11##FF"))

def export_image(path="../img/dfa.png"):
    dfa.show_diagram(path=path)

# export_image()