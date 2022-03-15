from configparser import ConfigParser


class ReadProperties:

    def readConfiguration(file_path, section, key):
        print(file_path, section, key)
        cfg = ConfigParser()
        cfg.read(file_path)

        return cfg.get(section, key)

