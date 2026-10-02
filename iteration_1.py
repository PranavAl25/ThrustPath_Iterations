from scipy import constants
import math

thrust_force = float(input("Enter the rocket's thrust force (N): "))
time_thrust = float(input("How long does does the rocket fire? (seconds): "))
rocket_mass = float(input("Enter the rocket's mass (kg): "))

#Powered Flight
accel_thrust = (thrust_force/rocket_mass) - constants.g
dist_powered = 0.5 * accel_thrust * time_thrust**2
burnout_v = accel_thrust*time_thrust

#Coasting Phase
dist_coast = (burnout_v**2) / (2 * constants.g)
time_coast = burnout_v / constants.g

#Apogee
apogee = dist_powered + dist_coast
time_apogee = time_coast + time_thrust

#Free Fall
impact_v = math.sqrt(2 * constants.g * apogee)
descent_t = math.sqrt((2*apogee)/(constants.g))

#Total
t_total = time_apogee + descent_t

print("\n\n")
print("Apogee: ", apogee, "m")
print("Time to Apogee: ", time_apogee, "s")
print("Powered Acceleration: ", accel_thrust, "m/(s^2)")
print("Burnout Velocity: ", burnout_v, "(m/s)")
print("Powered  Flight Altitude: ", dist_powered, "m")
print("Altitude Gained from Coasting: ", dist_coast, "m")
print("Impact Speed: ", impact_v, "m/s")
print("Total Flight Time: ", t_total, "s")



