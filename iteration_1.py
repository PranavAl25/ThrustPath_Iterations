from scipy import constants
import math
import matplotlib.pyplot as plt
import numpy as np

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
print("Powered Flight Altitude: ", dist_powered, "m")
print("Altitude Gained from Coasting: ", dist_coast, "m")
print("Impact Speed: ", impact_v, "m/s")
print("Total Flight Time: ", t_total, "s")



# PLOTTING SETUP
dt = 0.05

full_time_values = []
full_altitude_values = []

# POWERED FLIGHT
powered_time = []
powered_altitude = []
pow_time = 0

while pow_time < time_thrust:
    powered_time.append(pow_time)

    pow_alt = 0.5 * accel_thrust * pow_time**2
    powered_altitude.append(pow_alt)

    full_time_values.append(pow_time)
    full_altitude_values.append(pow_alt)

    pow_time += dt

powered_time.append(time_thrust)
powered_altitude.append(dist_powered)
full_time_values.append(time_thrust)
full_altitude_values.append(dist_powered)

# COASTING PHASE
coast_time = []
coast_altitude = []
t = 0

while t < time_coast:
    current_time = time_thrust + t

    coast_time.append(current_time)

    coast_alt = (
        dist_powered
        + burnout_v * t
        - 0.5 * constants.g * t**2
    )
    coast_altitude.append(coast_alt)

    full_time_values.append(current_time)
    full_altitude_values.append(coast_alt)

    t += dt

coast_time.append(time_apogee)
coast_altitude.append(apogee)
full_time_values.append(time_apogee)
full_altitude_values.append(apogee)

# DESCENT PHASE
descent_time = []
descent_altitude = []
t = 0

while t < descent_t:
    current_time = time_apogee + t

    descent_time.append(current_time)

    descent_alt = apogee - 0.5 * constants.g * t**2
    descent_altitude.append(descent_alt)

    full_time_values.append(current_time)
    full_altitude_values.append(descent_alt)

    t += dt

descent_time.append(t_total)
descent_altitude.append(0)
full_time_values.append(t_total)
full_altitude_values.append(0)

# FIGURE 1: ENTIRE FLIGHT
fig1, ax1 = plt.subplots(figsize=(11, 6))

ax1.plot(
    powered_time, powered_altitude,
    color="red", linewidth=2.5, label="Powered flight"
)

ax1.plot(
    coast_time, coast_altitude,
    color="green", linewidth=2.5, label="Coasting"
)

ax1.plot(
    descent_time, descent_altitude,
    color="blue", linewidth=2.5, label="Descent"
)

ax1.scatter(
    [time_thrust, time_apogee, t_total],
    [dist_powered, apogee, 0],
    color=["red", "green", "blue"],
    zorder=3
)

ax1.set_title("ThrustPath: Complete Flight Profile", fontsize=15)
ax1.set_xlabel("Time Since Launch (s)", fontsize=12)
ax1.set_ylabel("Altitude (m)", fontsize=12)

ax1.set_xlim(left=0, right=t_total)
ax1.set_ylim(bottom=0)

ax1.grid(True, linestyle="--", alpha=0.5)
ax1.legend(fontsize=10)
fig1.tight_layout()

# FIGURE 2: THREE INDIVIDUAL FLIGHT PHASES
fig2, axes = plt.subplots(
    1, 3,
    figsize=(15, 5),
    num="ThrustPath: Individual Flight Phases"
)

# Powered flight
axes[0].plot(
    powered_time, powered_altitude,
    color="red", linewidth=2
)
axes[0].set_title("Powered Flight")
axes[0].set_xlim(0, time_thrust)

# Coasting
axes[1].plot(
    coast_time, coast_altitude,
    color="green", linewidth=2
)
axes[1].set_title("Coasting")
axes[1].set_xlim(time_thrust, time_apogee)

# Descent
axes[2].plot(
    descent_time, descent_altitude,
    color="blue", linewidth=2
)
axes[2].set_title("Free-Fall Descent")
axes[2].set_xlim(time_apogee, t_total)

# Format all three subplots
for ax in axes:
    ax.set_xlabel("Time Since Launch (s)")
    ax.set_ylabel("Altitude (m)")
    ax.set_ylim(bottom=0)
    ax.grid(True, linestyle="--", alpha=0.5)

fig2.suptitle("ThrustPath: Individual Flight Phases", fontsize=15)
fig2.tight_layout()

plt.show()
