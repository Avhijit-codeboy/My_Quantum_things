# the write_and_run function writes the content in this cell into the file "feature_map.py"

### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector
from qiskit.circuit.library import ZZFeatureMap, ZFeatureMap, PauliFeatureMap
import numpy as np
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def feature_map(): 
    # BUILD FEATURE MAP HERE - START
    
    # import required qiskit libraries if additional libraries are required
    
    # build the feature map
    x = ParameterVector('x', length=3)
    feature_map = QuantumCircuit(3)
    for _ in range(2):
        for i in range(3):
            feature_map.h(i)
            feature_map.rz(x[i]*np.pi/6,i)
            feature_map.h(i)
            feature_map.rx(x[i]*np.pi/2,i)
            feature_map.h(i)
            feature_map.ry(x[i]*np.pi/6,i)
            feature_map.h(i)
        for i in range(3):
            for j in range(i + 1, 3):
                feature_map.cx(i, j)
                feature_map.u1(2*((np.pi/2-x[i]) * (np.pi/2-x[j])), j)
                feature_map.cx(i, j)
    
    # BUILD FEATURE MAP HERE - END
    
    #return the feature map which is either a FeatureMap or QuantumCircuit object
    return feature_map
