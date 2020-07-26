import pickle


class Settings:

    def __init__(self):
        self.write_mode = 'wb'
        self.read_mode = 'rb'
        self.file = 'rptool.cfg'
        self.config = {'loop': '0'}

    def saveConfig(self, cfg):
        self.config = cfg
        with open(self.file, self.write_mode) as config_file:
            pickle.dump(self.config, config_file)

    def readConfig(self):
        with open(self.file, self.read_mode) as config_file:
            self.config = pickle.load(config_file)
            return self.config