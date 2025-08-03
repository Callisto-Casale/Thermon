from phue import Bridge
import phue
import logging
from typing import Union


def setup_bridge(cfg: dict, logger: logging.Logger) -> Bridge:
    try:
        bridge = Bridge(cfg["fixed"]["hue_bridge_ip"])
        bridge.connect()
        bridge.get_api()
        logger.debug("Connected to Hue Bridge")
        return bridge
    except phue.PhueRegistrationException as e:
        logger.error(f"Error connecting to bridge: {e}")
        raise


def control_temperature(
    bridge: Bridge, temperature: Union[int, float], cfg: dict, logger: logging.Logger
):
    lights = bridge.get_light_objects("name")
    plug_name = cfg["variable"]["smart_plug_name"]
    fan_currently_on = lights[plug_name].on

    high_threshold = float(cfg["system"]["high_temp"])
    low_threshold = float(cfg["system"]["low_temp"])
    current_temp = float(temperature)

    if current_temp >= high_threshold and not fan_currently_on:
        lights[plug_name].on = True
        logger.info(f"Turned ventilator ON at {current_temp}°C")
    elif current_temp <= low_threshold and fan_currently_on:
        lights[plug_name].on = False
        logger.info(f"Turned ventilator OFF at {current_temp}°C")
    else:
        logger.info(
            f"No change - Temp: {current_temp}°C, Fan already {'ON' if fan_currently_on else 'OFF'}"
        )
