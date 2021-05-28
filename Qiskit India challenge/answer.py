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
# the write_and_run function writes the content in this cell into the file "variational_circuit.py"

### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector
from qiskit.circuit.library import  RealAmplitudes, EfficientSU2
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def variational_circuit():
    # BUILD VARIATIONAL CIRCUIT HERE - START
    
    # import required qiskit libraries if additional libraries are required
    
    # build the variational circuit
    var_circuit = EfficientSU2(3, reps=3)

    # BUILD VARIATIONAL CIRCUIT HERE - END
    
    # return the variational circuit which is either a VaritionalForm or QuantumCircuit object
    return var_circuit
# # the write_and_run function writes the content in this cell into the file "optimal_params.py"

### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
import numpy as np
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def return_optimal_params():
    # STORE THE OPTIMAL PARAMETERS AS AN ARRAY IN THE VARIABLE optimal_parameters 
    
    optimal_parameters = [ 1.53366614, -1.180565  , -0.83242541,  1.42514794, -0.6539459 ,
        0.75997613, -0.46002519, -1.04103125,  0.17166766, -0.39573853,
        3.62113631, -0.5200239 ,  0.71020846,  1.31452177,  0.57627883,
       -1.70502093,  0.98979859,  2.13270941, -0.75832064, -0.20020705,
       -0.31182005, -1.04739694, -1.03982196,  1.47795992]
    
    # STORE THE OPTIMAL PARAMETERS AS AN ARRAY IN THE VARIABLE optimal_parameters 
    return np.array(optimal_parameters)
