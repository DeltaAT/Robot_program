from automata.tm.dtm import DTM

dtm = DTM(
    # Erlaubte Eingabezeichen
    input_symbols={'1', '#', 'F', 'L', 'R'},

    # Bandzeichen
    tape_symbols={'1', '#', 'F', 'L', 'R', 'Y', 'X', '0'},

    blank_symbol='0',

    # Zustände
    states={'z1', 'z2', 'zf'},

    initial_state='z1',

    transitions={
        # z1: nach rechts laufen und das nächste 'F' suchen
        'z1': {
            '1': ('z1', '1', 'R'),
            '#': ('z1', '#', 'R'),
            'X': ('z1', 'X', 'R'),
            'Y': ('z1', 'Y', 'R'),
            'L': ('z1', 'L', 'R'),
            'R': ('z1', 'R', 'R'),
            # unverarbeitetes 'F' gefunden -> als 'Y' markieren, Treibstoff suchen
            'F': ('z2', 'Y', 'L'),
            # Bandende erreicht, kein 'F' mehr -> akzeptieren
            '0': ('zf', '0', 'N'),
        },
        # z2: nach links laufen und eine unverbrauchte '1' suchen
        'z2': {
            '#': ('z2', '#', 'L'),
            'F': ('z2', 'F', 'L'),
            'Y': ('z2', 'Y', 'L'),
            'L': ('z2', 'L', 'L'),
            'R': ('z2', 'R', 'L'),
            'X': ('z2', 'X', 'L'),
            # freie Treibstoffeinheit gefunden -> verbrauchen ('X'), nächstes 'F' suchen
            '1': ('z1', 'X', 'R'),
            # Kein Übergang für '0': kein Treibstoff mehr -> verwerfen
        },
    },

    # positiver Endzustand 'zf' hat keine Übergänge (die Maschine hält an)
    final_states={'zf'},
)

# Exportieren des DTM
"""
import pygraphviz as pgv

graph = pgv.AGraph(directed=True, rankdir="LR")

graph.add_node("__start__", shape="point", label="")
graph.add_edge("__start__", dtm.initial_state)

for state in dtm.states:
    graph.add_node(
        state,
        shape="doublecircle" if state in dtm.final_states else "circle",
    )

edge_labels = {}
for state, moves in dtm.transitions.items():
    for read_sym, (next_state, write_sym, direction) in moves.items():
        label = f"{read_sym} → {write_sym}, {direction}"
        edge_labels.setdefault((state, next_state), []).append(label)

for (src, dst), labels in edge_labels.items():
    graph.add_edge(src, dst, label="\n".join(labels))

graph.draw("machine.png", prog="dot", format="png")
print("machine.png geschrieben")
"""