import os
import configparser


class ConfigParser:
    """
    :return : config.ini as dict
    """
    def __init__(self):
        pass

    @staticmethod
    def config_parser(env, filename):
        config = configparser.RawConfigParser(strict=False)

        # needed to keep case sensitive keys
        config.optionxform = str
        try:
            if not os.path.exists(filename):
                raise FileNotFoundError("File not found : {}".format(filename))
            config.read(filename)
        except Exception as exception:
            raise exception

        # configs for env
        config_env = dict(config[env])

        for key, value in config_env.items():
            config_env[key] = value.strip(";").strip('"')

        return config_env
