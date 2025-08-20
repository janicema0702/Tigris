import numpy as np
import matplotlib.pyplot as plt
import datetime

from rocketpy import Environment, Rocket, SolidMotor, Flight

# Machrihanish Airbase Commuity Centre
mach_lat = 55.439056
mach_long = -5.698412

# Launch date is UTC 12:00, 12 July 2023, for reanalysis
launch_date = (2023, 7, 12, 12)
# Atmospheric wind data
EnvECMWF = Environment(date=launch_date, latitude=mach_lat, longitude=mach_long)
EnvECMWF.set_atmospheric_model(type="Windy", file="GFS")
EnvECMWF.set_elevation("Open-Elevation")

# Motor data
I350 = SolidMotor(
  thrust_source = r"Cesaroni_601I350-16A.csv",
  dry_mass = 0.288,
  dry_inertia = (0.00402, 0.00402, 0.0000666),
  nozzle_radius = 0.019,
  grain_number = 5,
  grain_density = 803,
  grain_outer_radius = 0.019,
  grain_initial_inner_radius = 0,
  grain_initial_height = 0.072,
  grain_separation = 0,
  grains_center_of_mass_position = 0.18,
  center_of_dry_mass_position = 0.18,
  nozzle_position = 0,
  burn_time = 1.71,
  throat_radius = 0.019,
  coordinate_system_orientation="nozzle_to_combustion_chamber",
)

# Create rocket
Tigris = Rocket(
    radius = 0.027,
    mass = 1.998,
    inertia=(0.17475, 0.17475, 0.0009345),
    power_off_drag=r"Tigris_Cd.csv",
    power_on_drag=r"Tigris_Cd.csv",
    center_of_mass_without_motor=0.513,
    coordinate_system_orientation="nose_to_tail",
)

motor = Tigris.add_motor(I350, position=1.14)
nosecone = Tigris.add_nose(length=0.108, kind="ogive", position=0, bluffness=0, name="Nose cone")
fins = Tigris.add_trapezoidal_fins(n=3, span=0.036, root_chord=0.08, tip_chord=0.03, position=1.058, cant_angle=0, sweep_length=0.05)
rail_buttons = Tigris.set_rail_buttons(
    upper_button_position=0.553,
    lower_button_position=0.633,
    angular_position=45,
)
main = Tigris.add_parachute(
    name="Main",
    cd_s=0.402,
    trigger=100,
    sampling_rate=105,
    lag=3,
)

drogue = Tigris.add_parachute(
    name="Drogue",
    cd_s=0.077,
    trigger="apogee",
    sampling_rate=105,
)

test_flight = Flight(
    rocket=Tigris, environment=EnvECMWF, rail_length=4.0, inclination=90, heading=0
    )


test_flight.all_info()