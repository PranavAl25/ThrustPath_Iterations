import rasp_parser
from scipy import constants
import math
import matplotlib.pyplot as plt

motor = rasp_parser.load_rasp_motor("AeroTech_N1000W.eng")

thrust_info = motor.thrust_curve
burn_time = motor.burn_time

thrust_list = []
thrust_times = []

rocket_mass = float(input("Enter the rocket's mass (kg): "))

for thrusts in thrust_info:
    thrust_times.append(thrusts.time)

for time in thrust_times:
    thrust_list.append(motor.get_interpolated_thrust(time))

plt.plot(thrust_times, thrust_list)
plt.show()
