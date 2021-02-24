import os
import json
from subprocess import call

config_file = open(os.path.abspath("./node.config"), 'r')
node_config = json.load(config_file)
render_engine = node_config["engine"]

config_file = open(node_config["path"] + "master.config", 'r')
master_config = json.load(config_file)
blender_path = master_config["exe"]
jobs_path = master_config["jobs"]

command = blender_path + " -b " + "B:/Blender/playground01.blend" + " -a " + "-- --cycles-device " + render_engine
call(command, shell=True)
