TireShop
========
A python package manager in a similar spirit to [NixOS](https://nixos.org/) as you describe what you want in a giant config file:[tireshop.conf.yaml](/tireshop.conf.yaml)

builds all ".whl" files by tagname and giturl requested in tireshop.conf.yaml file
all inside a virtual environment, finished wheels go in the tirerack directory.

```
git clone https://github.com/GetWheel/tireshop
cd /path/to/TireShop
./getwheel_bootstrap.py
./BootStrap/bin/python3 ./tireshop.py
```

should get you started

currently it works for packages that don't fail to build, 
but I'm having issues figuring out how to build pyside in this virtual envirnoment.
running right now on a debian machine plan on getting it to work on Nixos after I get it working on Debian

