"""
	config yaml

	wisemonkey
	oranbusiness@gmail.com
	20181222
	github.com/wisehackermonkey
"""
from configparser import ConfigParser
import os

# config_file = "config.yaml"

CONFIG_FILE = "config.yaml"

# create a new config file if it does not currently exist
# if not os.path.exists(config_file):
#     print(f"Creating Config File: '{config_file}'")
#     config.read(config_file)
#     # config.add_section("Defauts")
#     # config.set("Defauts","spyagent1","none")
#     with open(config_file, "w") as f:
#         config.write(f)
# else:
#     print("Reading Config file")
#     config.read(config_file)

# dummy class to test loading config and setting new values
class TopSecreteProgram():
    def __init__(self):
        self.topsecretkey = config["Defauts"]["spyagent1"]
    def setSecret(self, new_secret):
        self.topsecretkey = new_secret
    def recon(self):
        global config
        self.topsecretkey = config.get("Defauts","spyagent1")
        print(self.topsecretkey)
    def saveConfiguration(self):
        config["Defauts"]["spyagent1"] = self.topsecretkey
        with open(config_file, "w") as f:
            config.write(f)

class Configuration():
    def __init__(self, config_file_):
        self.file_name = config_file_
        self.private_key = ""
        self.config = ConfigParser()

        if os.path.exists(self.file_name):
            print("Reading Config file")
            self.config.read(self.file_name)
        else:
            print("config file not found!")
            print("So I created one.")
            self.config.read(self.file_name)
            self.config.add_section("SETTINGS")
            self.set("spyagent1","none")
            self.__save__()
    def set(self, key, value, group="SETTINGS"):
        self.config[group][key] = value
        self.__save__()
    def get(self, key, group="SETTINGS"):
        return self.config.get(group,key)
    def __save__(self):
        with open(self.file_name, "w") as f:
            self.config.write(f)


  

# spyagent = TopSecreteProgram()
# print("Getting password....")
# spyagent.recon()
# spyagent.setSecret(input("Please enter the secrete password to be saved! :"))
# print("Saving configuration file")
# spyagent.saveConfiguration()


print("Setting up Configuration file")
config = Configuration(CONFIG_FILE)
print(config.get("spyagent1"))
config.set("spyagent1","password123")
print(config.get("spyagent1"))

# file_name = "config.yaml"

# config = ConfigParser()

# config.read(file_name)
# config.add_section("SETTINGS")
# config.set("SETTINGS","spyagent1","none")
# with open(file_name, "w") as f:
#     config.write(f)
