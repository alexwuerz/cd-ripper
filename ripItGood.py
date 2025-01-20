#!env/bin/python

import os, json
import subprocess, configparser
# from smbprotocol.connection import Connection
# from smbprotocol.session import Session
# from smbprotocol.tree import TreeConnect
# from smbprotocol.file import Open, CreateDisposition, FilePipePrinterAccessMask

# Configuration
# TODO: put this in an ini file in .gitignore
CONFIG = configparser.ConfigParser()
CONFIG.read('.ripItGood.ini')

# Credentials
NAS_USERNAME = CONFIG['credentials']['NAS_USERNAME']
NAS_PASSWORD = CONFIG['credentials']['NAS_PASSWORD']

# Config
NAS_IP = CONFIG['config']['NAS_IP']
NAS_SHARE = CONFIG['config']['NAS_SHARE']
NAS_DESTINATION_DIR = CONFIG['config']['NAS_DESTINATION_DIR']
RIP_OUTPUT_DIR = CONFIG['config']['RIP_OUTPUT_DIR']
#SKIP_VOLUMES = CONFIG['config']['SKIP_VOLUMES']
SKIP_VOLUMES = json.loads(CONFIG.get("config","SKIP_VOLUMES"))


def isCDinserted():
    # TODO: do this with only python dependencies.  
    # Maybe skip for now and assume it's always inserted.
    return True

def getVolumePaths():
    volumes_dir = "/Volumes"
    volume_paths = []

    for volume in os.listdir(volumes_dir):
        if volume not in SKIP_VOLUMES:
            volume_path = os.path.join(volumes_dir, volume)
            if os.path.isdir(volume_path):
                # Check for audio CD characteristics, TODO: make this more robust
                tracks = [f for f in os.listdir(volume_path)]
                if tracks:
                    print(f"Audio CD detected: {volume_path}")
                    volume_paths.append(volume_path)
        else:
            print(f"Skipping dir: {volume}")
        
    if len(volume_paths) > 0:
        return volume_paths
    else:
        return None


def ripCD(output_dir):
    """Rip the CD using ffmpeg."""
    os.makedirs(output_dir, exist_ok=True)
    try:
        # Replace with a tool that suits your need. This assumes ffmpeg is installed.
        # subprocess.run(["ffmpeg", "-i", "/dev/disk1", f"{output_dir}/track%02d.wav"], check=True)
        # TODO: read cd stream, save it with ffmpeg-python package

        # get the cd info and location
        cd_volume_paths = getVolumePaths()

        for cd in cd_volume_paths:
            print(f"rip it good {cd}")

        return True
    except subprocess.CalledProcessError:
        print("Error ripping the CD.")
        return False

def transferToNAS(local_dir, remote_dir):
    # TODO: this
    return True

if __name__ == "__main__":
    if isCDinserted():
        print("CD detected. Starting to rip...")
        if ripCD(RIP_OUTPUT_DIR):
            # print("Rip succeeded!  Transferring to NAS...")
            transferToNAS(RIP_OUTPUT_DIR, NAS_DESTINATION_DIR)
            # print("Transfer to NAS complete!")
        else:
            print("Rip failed.")

