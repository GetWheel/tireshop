#!/usr/bin/env python3
# coding=utf-8
#________________________________________________________________________LICENSE
#	Copyright © 2022 Roy Pfund. All rights reserved.
#
#	Licensed under the Apache License, Version 2.0 (the  "License");
#	you may not use this file except in compliance with the License.
#	You may obtain a copy of the License at
#
#		http://www.apache.org/licenses/LICENSE-2.0
#
#	Unless required by applicable  law  or  agreed  to  in  writing,
#	software distributed under the License is distributed on an  "AS
#	IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,  either
#	express or implied. See the License for  the  specific  language
#	governing permissions and limitations under the License.
#__________________________________________________________________DOCUMENTATION
'''stuff.py
"getwheel_bootstrap.PkgInstall" the following packages:

Revision Tags Last updated 2014-6-13
sudo apt-get install python-dev
'''
#________________________________________________________________Library Imports
import subprocess, threading, re, os, sys, inspect, shutil, argparse, random, math
rows, columns = os.popen('stty size', 'r').read().split() #http://goo.gl/cD4CFf
#"pydoc -p 1234" will start a HTTP server on port 1234, allowing you  to  browse
#the documentation at "http://localhost:1234/" in your preferred Web browser.
cwf = os.path.abspath(inspect.getfile(inspect.currentframe())) # Current Working File
cwfd = os.path.dirname(cwf) # Current Working File Path
#from GitTar import GitTar
import getwheel_bootstrap
#______________________________________________________________________Functions
#https://github.com/cython/cython
#getwheel_bootstrap.PkgInstall(PkgName="alive-progress", GitUrl="https://github.com/rsalmei/alive-progress.git", TagName="", cwfd=cwfd)
    #cython
    #packaging
    #wheel

#____________________________________________________________________Main Script
#getwheel_bootstrap.PkgInstall(PkgName="None", GitUrl=None, TagName=None, cwfd=cwfd)
#getwheel_bootstrap.PkgInstall(PkgName="setuptools", GitUrl="https://github.com/pypa/setuptools.git", TagName="v52.0.0", cwfd=cwfd)#v61.2.0

getwheel_bootstrap.PkgInstall(PkgName="cython", GitUrl="https://github.com/cython/cython.git", TagName="0.29.28", cwfd=cwfd)
getwheel_bootstrap.PkgInstall(PkgName="packaging", GitUrl="https://github.com/pypa/packaging.git", TagName="21.3", cwfd=cwfd)
getwheel_bootstrap.PkgInstall(PkgName="wheel", GitUrl="https://github.com/pypa/wheel.git", TagName="0.37.1", cwfd=cwfd)
getwheel_bootstrap.PkgInstall(PkgName="pyyaml", GitUrl="https://github.com/yaml/pyyaml.git", TagName="6.0", cwfd=cwfd)
#installwheel(cwfd + '/tirerack/' + "PyYAML-6.0-cp39-cp39-linux_x86_64.whl")

