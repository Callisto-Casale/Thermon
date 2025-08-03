import argparse
from config_loader import load_config
from logger_setup import setup_logger
from bridge_controller import setup_bridge, control_temperature


def main():
    config = load_config()
    logger = setup_logger(config)

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--temperature", required=True,
                        help="Temperature in Celsius")
    args = parser.parse_args()

    try:
        temperature = float(args.temperature)
    except ValueError:
        logger.error(
            f"Invalid temperature: '{args.temperature}' must be a number.")
        return

    logger.debug(f"Starting with temperature: {temperature}")
    bridge = setup_bridge(config, logger)
    control_temperature(bridge, temperature, config, logger)


if __name__ == "__main__":
    main()
