import logging


def setup_logger(cfg: dict) -> logging.Logger:
    log_cfg = cfg.get("logging", {})
    log_level = getattr(logging, log_cfg.get(
        "level", "INFO").upper(), logging.INFO)
    log_file = log_cfg.get("file", "app.log")

    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    formatter = logging.Formatter(
        "{asctime} - {levelname} - {message}", style="{", datefmt="%Y-%m-%d %H:%M"
    )

    file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(logging.StreamHandler())

    return logger
