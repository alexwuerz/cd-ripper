# cd-ripper
Rip CDs
This was written and tested on macOS Sonoma using Python3.

## Sources
https://github.com/kkroening/ffmpeg-python
https://github.com/jborean93/smbprotocol

## Docs
https://kkroening.github.io/ffmpeg-python/

# environment setup
```
cd ~/project/directory 
python -m venv ./env
source ./env/bin/activate
pip install -r ./requirements.txt
```

# ini file
Create a file called `.ripItGood.ini` and give it the following contents: 
```
[credentials]
NAS_USERNAME = "user"
NAS_PASSWORD = "password"

[config]
NAS_IP = "192.168.0.100"
NAS_SHARE = "Media"
NAS_DESTINATION_DIR = "/Music/"
RIP_OUTPUT_DIR = "/tmp/cd_rip"
```

# Extras
I like to run this automatically when I insert a CD.  In macOS, you can open System Preferences and find `Handle CDs and DVDs`.  Then choose `When you insert a music CD` > `Run Script...`