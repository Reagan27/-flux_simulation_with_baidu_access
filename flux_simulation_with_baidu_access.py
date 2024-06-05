import matplotlib.pyplot as plt
import numpy as np


class ImportFlux:
    @staticmethod
    def set_parameter(name, value):
        print(f"Setting parameter {name} to {value}")

    @staticmethod
    def set_initial_condition(name, value):
        print(f"Setting initial condition {name} to {value}")

    @staticmethod
    def set_boundary_condition(name, value):
        print(f"Setting boundary condition {name} to {value}")

    @staticmethod
    def set_motor_parameter(name, value):
        print(f"Setting motor parameter {name} to {value}")

    @staticmethod
    def set_material(name, properties):
        print(f"Setting material {name} with properties {properties}")

    @staticmethod
    def set_mesh(name, size):
        print(f"Setting mesh {name} with size {size}")

    @staticmethod
    def set_solver_parameter(name, value):
        print(f"Setting solver parameter {name} to {value}")

    @staticmethod
    def set_load(name, value):
        print(f"Setting load {name} to {value}")

    @staticmethod
    def run():
        print("Running simulation")

    @staticmethod
    def get_result(name):
        print(f"Getting result for {name}")
        if name == "Speed":
            return np.linspace(0, -20000, 100)  
        elif name == "Losses":
            return np.linspace(0, -20000, 100)  # Placeholder for losses result
        elif name == "Sensors":
            return np.linspace(-200, 200, 100)  # Placeholder for sensor data
        else:
            return None


def setup_simulation():
    # electrical parameters
    voltage = 230  # Supply voltage in volts
    frequency = 50  # Supply frequency in Hz

    # mechanical parameters
    inertia = 0.01  # Inertia in kg.m^2
    damping = 0.001  # Damping coefficient in Nm.s/rad
    friction = 0.01  # Friction coefficient in Nm

    # Set parameters in Flux model
    ImportFlux.set_parameter("Voltage", voltage)
    ImportFlux.set_parameter("Frequency", frequency)
    ImportFlux.set_parameter("Inertia", inertia)
    ImportFlux.set_parameter("Damping", damping)
    ImportFlux.set_parameter("Friction", friction)

    # initial conditions
    initial_speed = 0  # Initial speed in rad/s
    ImportFlux.set_initial_condition("Speed", initial_speed)

    # Set boundary conditions
    ImportFlux.set_boundary_condition("Voltage", voltage)
    ImportFlux.set_boundary_condition("Frequency", frequency)

    #  motor parameters
    motor_resistance = 0.1  # Resistance in ohms
    motor_inductance = 0.01  # Inductance in H

    # Set motor parameters
    ImportFlux.set_motor_parameter("Resistance", motor_resistance)
    ImportFlux.set_motor_parameter("Inductance", motor_inductance)

    # Define core material properties
    core_material = {
        "Name": "Iron",
        "HysteresisLoss": True,
        "EddyCurrentLoss": True
    }

    # Assign material to core
    ImportFlux.set_material("Core", core_material)

    # Set mesh properties
    mesh_size = 0.001  # Mesh size in meters

    # Apply mesh to the model
    ImportFlux.set_mesh("Model", mesh_size)

    #  solver settings
    tolerance = 1e-6
    max_iterations = 1000

    #  solver parameters
    ImportFlux.set_solver_parameter("Tolerance", tolerance)
    ImportFlux.set_solver_parameter("MaxIterations", max_iterations)

    # load conditions
    load_torque = 10  # Load torque in Nm

    # load conditions
    ImportFlux.set_load("Torque", load_torque)

    print("Simulation setup completed successfully.")

def run_simulation():
    # Run the simulation
    try:
        ImportFlux.run()
        print("Simulation ran successfully.")
    except Exception as e:
        print(f"Error running simulation: {e}")

def check_results():
    # Check and print the results
    speed = ImportFlux.get_result("Speed")
    losses = ImportFlux.get_result("Losses")
    sensors = ImportFlux.get_result("Sensors")

    print(f"Speed: {speed[-1]} rad/s")
    print(f"Losses: {losses} W")
    print(f"Sensors: {sensors}")

    if speed[-1] == 0 or np.any(losses == 0):
        print("Warning: Speed is zero or Losses are zero, check the model setup.")

    return speed, losses, sensors

def plot_results(speed, sensors):
    # Plot the rotation speed
    time = np.linspace(0, 2.5, len(speed))
    plt.figure(figsize=(10, 6))
    plt.plot(time, speed, label="Rotation Speed (ROTOR)", color="blue", linewidth=2)
    plt.title("Mechanical Set / Rotation Speed (ROTOR)")
    plt.xlabel("Time")
    plt.ylabel("Speed (rad/s)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot the sensor data
    time = np.linspace(2.85, 3.0, len(sensors))  # Adjusted time range based on the image
    plt.figure(figsize=(10, 6))
    plt.plot(time, sensors, label="P_1", color="blue", linewidth=2)
    plt.title("SENSORS_1")
    plt.xlabel("Time")
    plt.ylabel("Sensor Value")
    plt.legend()
    plt.grid(True)
    plt.show()

def access_baidu_disk():
    # Open the Baidu APP to access the shared file
    link = "https://pan.baidu.com/s/1K42Ek4qq32B4CtG3TOzptA"
    extraction_code = "7gmp"

    print("Copy this content to open 'Baidu APP can be obtained':")
    print(f"#小程序://百度网盘/{link} {extraction_code}")

if __name__ == "__main__":
    setup_simulation()
    run_simulation()
    speed, losses, sensors = check_results()
    plot_results(speed, sensors)
    access_baidu_disk()
