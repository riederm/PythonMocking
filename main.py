from temp_control import TemperatureController, RealFanControl, RealTemperatureSensor


#example usage
if __name__ == "__main__":
    # Create instances of the real dependencies
    temperature_sensor = RealTemperatureSensor()
    fan_control = RealFanControl()

    # Create an instance of the TemperatureController with real dependencies
    temp_controller = TemperatureController(temperature_sensor, fan_control)

    # Regulate the fan speed based on the current temperature
    temp_controller.regulate_fan_speed()