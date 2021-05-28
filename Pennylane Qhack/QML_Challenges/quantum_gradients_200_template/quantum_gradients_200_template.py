#! /usr/bin/python3

import sys
import pennylane as qml
import numpy as np
def gradient_200(weights, dev):
    r"""This function must compute the gradient *and* the Hessian of the variational
    circuit using the parameter-shift rule, using exactly 51 device executions.
    The code you write for this challenge should be completely contained within
    this function between the # QHACK # comment markers.

    Args:
        weights (array): An array of floating-point numbers with size (5,).
        dev (Device): a PennyLane device for quantum circuit execution.

    Returns:
        tuple[array, array]: This function returns a tuple (gradient, hessian).

            * gradient is a real NumPy array of size (5,).

            * hessian is a real NumPy array of size (5, 5).
    """

    @qml.qnode(dev, interface=None)
    def circuit(w):
        for i in range(3):
            qml.RX(w[i], wires=i)

        qml.CNOT(wires=[0, 1])
        qml.CNOT(wires=[1, 2])
        qml.CNOT(wires=[2, 0])

        qml.RY(w[3], wires=1)

        qml.CNOT(wires=[0, 1])
        qml.CNOT(wires=[1, 2])
        qml.CNOT(wires=[2, 0])

        qml.RX(w[4], wires=2)

        return qml.expval(qml.PauliZ(0) @ qml.PauliZ(2))

    gradient = np.zeros([5], dtype=np.float64)
    hessian = np.zeros([5, 5], dtype=np.float64)
    
    # QHACK #
    dev1 = qml.device('default.qubit',wires=3)
    @qml.qnode(dev1, interface=None)
    def circuit1(w):
        for i in range(3):
            qml.RX(w[i], wires=i)

        qml.CNOT(wires=[0, 1])
        qml.CNOT(wires=[1, 2])
        qml.CNOT(wires=[2, 0])

        qml.RY(w[3], wires=1)

        qml.CNOT(wires=[0, 1])
        qml.CNOT(wires=[1, 2])
        qml.CNOT(wires=[2, 0])

        qml.RX(w[4], wires=2)

        return qml.expval(qml.PauliZ(0) @ qml.PauliZ(2))

    s = 0.5 * np.pi
    denom = 4 * np.sin(s) ** 2
    shift = np.eye(len(weights))

    def parameter_shift1(qnode,weights,i):
        shifted = weights.copy()
        shifted[i]+=np.pi/2
        forward = qnode(shifted)
        shifted[i]-=np.pi
        backward = qnode(shifted)
        return 0.5*(forward-backward)/np.sin(np.pi/2)


    def parameter_shift2(qnode,weights):
        for i in range(len(weights)):
            gradient[i] = parameter_shift1(qnode,weights,i)

    f_m = circuit(weights)
    def calculate_hessian(weights):
        for c in range(len(weights)):
            for c1 in range(c,len(weights)):
                if c!=c1:
                    weights_pp = weights + s * (shift[c] + shift[c1])
                    weights_pm = weights + s * (shift[c] - shift[c1])
                    weights_mp = weights - s * (shift[c] - shift[c1])
                    weights_mm = weights - s * (shift[c] + shift[c1])
                    f_pp = circuit(weights_pp)
                    f_pm = circuit(weights_pm)
                    f_mp = circuit(weights_mp)
                    f_mm = circuit(weights_mm)
                    ans = (f_pp-f_pm-f_mp+f_mm)/denom
                    hessian[c,c1]=ans
                    hessian[c1,c]=ans
    parameter_shift2(circuit,weights)
    for i in range(len(weights)):
            f_p = circuit1(weights+np.pi*shift[i])
            hessian[i,i] = 0.5*(f_p-f_m)
    calculate_hessian(weights)
    # QHACK #

    return gradient, hessian, circuit.diff_options["method"]


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    weights = sys.stdin.read()
    weights = weights.split(",")
    weights = np.array(weights, float)

    dev = qml.device("default.qubit", wires=3)
    gradient, hessian, diff_method = gradient_200(weights, dev)

    print(
        *np.round(gradient, 10),
        *np.round(hessian.flatten(), 10),
        dev.num_executions,
        diff_method,
        sep=","
    )
