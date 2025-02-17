import json
import os
import sys
from graphviz import Digraph


def load_turing_machine(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def draw_turing_machine(turing_machine):
    dot = Digraph()
    dot.attr(rankdir='LR')  
    
    
    for state in set([t.split(',')[0] for t in turing_machine['transitions']]):
        if state == turing_machine['init']:
            dot.node(state, shape='doublecircle', color='green')  
        elif state == turing_machine['accept']:
            dot.node(state, shape='doublecircle', color='red', style='filled', fillcolor='yellow')  
        else:
            dot.node(state, shape='circle')
    
    
    transition_set = set()
    for key, value in turing_machine['transitions'].items():
        current_state, read_symbol = key.split(',')
        next_state, write_symbol, move = value
        transition_key = (current_state, next_state, f"{read_symbol} → {write_symbol}, {move}")
        if transition_key not in transition_set:
            dot.edge(current_state, next_state, label=f"{read_symbol} → {write_symbol}, {move}")
            transition_set.add(transition_key)
    
    return dot

def main(filename):
    
    if not os.path.isfile(filename):
        print(f"Error: Archivo '{filename}' no encontrado.")
        sys.exit(1)
    
    turing_machine = load_turing_machine(filename)
    dot = draw_turing_machine(turing_machine)
    output_file = '/mnt/data/turing_machine_diagram'
    dot.render(output_file, format='png', view=True)
    print(f"Diagrama de transiciones guardado en: {output_file}.png")

if __name__ == "__main__":
    default_filename = "fibonacci.json"
    filename = sys.argv[1] if len(sys.argv) == 2 else default_filename
    main(filename)
