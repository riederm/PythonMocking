import pytest
from temp_control import TemperatureController, RealFanControl, RealTemperatureSensor, FanSpeed


def test_fan_turns_high_at_50_degrees():
    # GIVEN a sensor that reports 50 degrees
    # ...

    # WHEN the temperature controller regulates the fan speed
    # controller = TemperatureController(...)
    # controller.regulate_fan_speed()

    # THEN the fan should be set to HIGH speed
    # ... 

def test_fan_turns_medium_at_35_degrees():
    # GIVEN a sensor that reports 35 degrees
    # ...

    # WHEN the temperature controller regulates the fan speed
    # controller = TemperatureController(...)
    # controller.regulate_fan_speed()

    # THEN the fan should be set to MEDIUM speed
    # ... 

def test_fan_turns_low_at_25_degrees():
    # GIVEN a sensor that reports 25 degrees
    # ...

    # WHEN the temperature controller regulates the fan speed
    # controller = TemperatureController(...)
    # controller.regulate_fan_speed()

    # THEN the fan should be set to LOW speed
    # ... 

def test_fan_turns_off_at_20_degrees():
    # GIVEN a sensor that reports 20 degrees
    # ...

    # WHEN the temperature controller regulates the fan speed
    # controller = TemperatureController(...)
    # controller.regulate_fan_speed()

    # THEN the fan should be truned OFF
    # ... 