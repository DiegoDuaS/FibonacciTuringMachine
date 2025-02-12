def run_turing_machine(machine, input_string):
    tape = list(input_string) + ["_"]  
    head = 0
    state = machine["init"]
    accept_state = machine["accept"]
    transitions = machine["transitions"]
    
    while state != accept_state:
        symbol = tape[head]
        key = f"{state},{symbol}"
        
        if key not in transitions:
            print("No transition found. Halting.")
            return "Rejected"
        
        next_state, write_symbol, move = transitions[key]
        tape[head] = write_symbol
        state = next_state
        
        print("".join(tape), f"({state}, head={head})")
        
        if move == ">":
            head += 1
            if head >= len(tape):
                tape.append("_")
        elif move == "<":
            head = max(0, head - 1)
    
    return "".join(tape)