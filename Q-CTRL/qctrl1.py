import attr
import numpy as np

from qctrl import Qctrl

# Starting a session with the API
qctrl = Qctrl(email='avhijtnair@gmail.com', password='Avhijit13$')

# Create drive segment object, and use it to create a drive object
drive_segment = qctrl.types.ComplexSegmentInput(duration=1, value=1 + 1j)
drive = qctrl.types.filter_function.Drive(
    control=[drive_segment],
    operator=np.array([[0, 1], [0, 0]]),
)

# Create shift segment dictionary, and use it to create a shift object
shift_segment = {"duration": 1, "value": 2}
shift = qctrl.types.filter_function.Shift(
    control=[shift_segment],
    operator=np.array([[1, 0], [0, -1]]),
    noise=True,
)

filter_function_result = qctrl.functions.calculate_filter_function(
    duration=1,
    frequencies=np.linspace(0, 1e6, 100),
    drives=[drive],
    shifts=[shift],
)
print("Sample object:")
print(filter_function_result.samples[0])
print("")
print("Sample dictionary:")
print(attr.asdict(filter_function_result.samples[0]))

print(filter_function_result.action.status)
