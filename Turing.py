import time  

def run_turing_machine(machine, input_string):
    tape = list(input_string) + ["_"]  
    head = 0
    state = machine["init"]
    accept_state = machine["accept"]
    transitions = machine["transitions"]

    start_time = time.time()  
    steps = 0  

    while state != accept_state:
        symbol = tape[head]
        key = f"{state},{symbol}"
        
        if key not in transitions:
            print("No transition found. Halting.")
            return "Rejected"
        
        next_state, write_symbol, move = transitions[key]
        tape[head] = write_symbol
        state = next_state
        steps += 1  
        
        print("".join(tape), f"({state}, head={head})")
        
        if move == ">":
            head += 1
            if head >= len(tape):
                tape.append("_")
        elif move == "<":
            head = max(0, head - 1)

    end_time = time.time()  
    execution_time = end_time - start_time  

    print(f"\nTiempo total de ejecución: {execution_time:.6f} segundos")  
    print(f"Número total de pasos: {steps}")  

    return "".join(tape)
