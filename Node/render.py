import os
import json
from subprocess import call

class Configuration:
    def __init__(self):
        # config_file = open(os.path.abspath("./node.config"), 'r')
        with open(os.path.abspath("./node.config"), 'r') as _file:
            _config = json.load(_file)
            self.master_path = _config["path"]
            self.render_engine = _config["engine"]

        
        # config_file = open(self.master_path + "master.config", 'r')
        with open(self.master_path + "master.config", 'r') as _file:
            _config = json.load(_file)
            self.blender_path = _config["exe"]
            self.jobs_path = _config["jobs"]

config = Configuration()

command = config.blender_path + " -b " + "B:/Blender/playground01.blend" + " -a " + "-- --cycles-device " + config.render_engine
call(command, shell=True)
