"""
	config yaml

	wisemonkey
	oranbusiness@gmail.com
	20181222
	github.com/wisehackermonkey
"""
from configparser import ConfigParser
import os

CONFIG_FILE = "config.yaml"

# class abastracts settins for a program
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
            self.init()
    def init(self):
        self.config.read(self.file_name)
        self.config.add_section("SETTINGS")
        self.set("spyagent1","none")
        self.__save__()
    def set(self, key, value, section="SETTINGS"):
        self.config[section][key] = value
        self.__save__()
    def get(self, key, section="SETTINGS"):
        return self.config.get(section,key)
    def addSection(self,new_section):
        self.config.add_section(new_section)
        self.__save__()
    def addField(self,new_field, section="SETTINGS"):
        self.config.set(section,new_field,"")
        self.__save__()
    def __save__(self):
        with open(self.file_name, "w") as f:
            self.config.write(f)



print("Setting up Configuration file")
config = Configuration(CONFIG_FILE)
print(config.get("spyagent1"))
config.set("spyagent1","password123")
print(config.get("spyagent1"))
try:
    config.addSection("BACKUPS")
except Exception as e:
    print(f"Error:")
config.addField("url", "BACKUPS")
config.set("url","http://www.google.com",section="BACKUPS")
print(config.get("url","BACKUPS"))


