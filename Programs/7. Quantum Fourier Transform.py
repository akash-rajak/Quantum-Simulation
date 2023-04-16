import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, Aer, execute
from qiskit.circuit.library import QFT

# Define the quantum circuit
num_qubits = 4
qr = QuantumRegister(num_qubits, 'q')
cr = ClassicalRegister(num_qubits, 'c')
circuit = QuantumCircuit(qr, cr)
circuit.x(qr[0])
circuit.append(QFT(num_qubits), qr)

# Run the circuit
backend = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend).result()

# Print the result
print(result.get_statevector())
