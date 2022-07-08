TireShop
========
A python package manager in a similar spirit to [NixOS](https://nixos.org/) as you describe what you want in a giant config file:[tireshop.conf.yaml](/tireshop.conf.yaml). Right now it only works for libraries that can be built with a bdist_wheel target, which should be like 80-90% of all packages;
So if your package is failing to build it more than likely is a OS level dependency is missing like gfortran77 dependency for numpy compilation is simply not a python package.

The rule of thumb, is if the package you're working with has a bdist_wheel target in the setup.py it SHOULD compile.

```
git clone https://github.com/GetWheel/tireshop
cd /path/to/TireShop
./getwheel_bootstrap.py
./BootStrap/bin/python3 ./tireshop.py
```

Code above should clone this repo from github and builds all ".whl" files by tagname and giturl requested in tireshop.conf.yaml file
all inside a virtual environment, finished wheels go in the tirerack directory.

If a wheel fails to build; it will dump the log of the failed build, where the wheel should be located in the tirerack directory.
