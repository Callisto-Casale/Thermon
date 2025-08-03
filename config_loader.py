import tomli


def load_config(path="config.toml") -> dict:
    with open(path, "rb") as fp:
        return tomli.load(fp)
