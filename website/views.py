from flask import Blueprint, render_template, send_file, send_from_directory
import socket, os, shutil, sys
import psutil

views = Blueprint("views", __name__)

device_name = socket.gethostname()
ip_address = socket.gethostbyname(device_name)


platform_info = {
    "system": sys.platform,
    "architecture": os.uname().machine,
    "release": os.uname().release,
    "version": os.uname().version
}



@views.route("/")
def home():
  return render_template("index.html", device_name=device_name, ip_address=ip_address, system=platform_info["system"], 
architecture=platform_info["architecture"], release=platform_info["release"], version=platform_info["version"]
)

@views.route("/credits")
def credits():
  return render_template("credits.html")

@views.route("/download")
def download():
  filename = 'device_info.txt'  
  directory = 'website/datafiles/' 
  file_path = directory + filename 

  with open(file_path, 'w') as f:
    f.write(f"""Device Data from ToSphere
DEVICE NAME: {device_name}
IP ADDRESS: {ip_address}
SYSTEM: {platform_info["system"]}
ARCHITECTURE: {platform_info["architecture"]}
RELEASE: {platform_info["release"]}
VERSION:{platform_info["version"]}

from https://tosphere.onrender.com/
""")
  return render_template("index.html")