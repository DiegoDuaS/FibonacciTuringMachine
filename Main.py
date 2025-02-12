import json
from Turing import run_turing_machine

def load_turing_machine(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            machine = json.load(file)
        return machine
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
        return None
    except json.JSONDecodeError:
        print("Error: El archivo no tiene un formato JSON válido.")
        return None

machine = load_turing_machine("fibonacci.json")
print("*** El formato para que funcione es: \nf(0) = \nf(3) = XXX \nf(6) = XXXXXX")
fibonacci = input("Ingrese el numero para llegar a la sucecion de fibonacci:")
run_turing_machine(machine,fibonacci+"#-1-1")