"""
	config yaml

	wisemonkey
	oranbusiness@gmail.com
	20181222
	github.com/wisehackermonkey
"""
from configparser import ConfigParser

config = ConfigParser()
config.read("config.yaml")
# config.add_section("Defauts")
# config.set("Defauts","spyagent1","password123")
# with open("config.yaml", "w") as f:
    # config.write(f)


class TopSecreteProgram():
    def __init__(self):
        self.topsecretkey = config["Defauts"]["spyagent1"]
        pass
    def recon(self):
        print(self.topsecretkey)

spyagent = TopSecreteProgram()

spyagent.recon()