
### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
from qiskit import QuantumCircuit
import numpy as np
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def build_state():
    
    # create a quantum circuit on one qubit
    circuit = QuantumCircuit(1)
    initial_state = [1.0/np.sqrt(2),-1.j/np.sqrt(2)]
    circuit.initialize(initial_state,0)
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - START
    
    # apply necessary gates
    
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - END
    return circuit
