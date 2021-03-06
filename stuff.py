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
import getwheel_bootstrap, gittar
#______________________________________________________________________Functions
#https://github.com/cython/cython
#getwheel_bootstrap.PkgInstall(PkgName="alive-progress", GitUrl="https://github.com/rsalmei/alive-progress.git", TagName="", cwfd=cwfd)
    #numpy
    #pandas
    #sphinx
    #six
    #pyinstaller
    #PyOpenGL
def wheelfab(PkgName=None, GitUrl=None, TagName=None, cwfd=None):
	print(cwfd)
	gittar.gittar(PkgName=PkgName, GitUrl=GitUrl, TagName=TagName, cwfd=cwfd)
	PkgDir = cwfd + '/Pkg/' + PkgName
	print( "\ncreating wheel: "+ PkgName +"\n" )
	SPObject_PkgInstall = subprocess.Popen(
#python setup.py bdist_wheel --universal
#Remove the --universal tag if you want to create a Pure-Python Wheel.
		[cwfd + '/BootStrap/bin/python3', PkgDir + '/setup.py', 'bdist_wheel', \
            #'--qtpaths=/usr/lib/qt5/bin', \
            #'--parallel=4'
            ], #'--qtpaths=/usr/lib/qt5/bin' #], #'--qtpaths=/usr/lib/qt5/bin'
		stdin=None, stdout=None, stderr=None, cwd=PkgDir, env=None)
	SPObject_PkgInstall.wait()
	newwheel = os.listdir( PkgDir + '/dist')[0]
	print(newwheel + '\n')
	shutil.move( PkgDir + '/dist/' + newwheel , \
                cwfd + '/tirerack/' + newwheel )#PkgName + TagName + ".whl" )

def installwheel(newwheel):
	print("installing" + newwheel + '\n')
	tirerack = cwfd + '/tirerack/' + newwheel
	SPObject_PkgInstall = subprocess.Popen(
#python setup.py bdist_wheel --universal
#Remove the universal tag if you want to create a Pure-Python Wheel.
        [cwfd + '/BootStrap/bin/python3', '-m', 'pip', 'install', \
            newwheel   \
            ], #'--qtpaths=/usr/lib/qt5/bin' #], #'--qtpaths=/usr/lib/qt5/bin'
		stdin=None, stdout=None, stderr=None, cwd=None, env=None)
	SPObject_PkgInstall.wait()

#____________________________________________________________________Main Script
#wheelfab(PkgName="None", GitUrl=None, TagName=None, cwfd=cwfd)
#installwheel("")

#wheelfab(PkgName="pyyaml", GitUrl="https://github.com/yaml/pyyaml.git", TagName="6.0", cwfd=cwfd)
#installwheel("/home/owner/GitHy/tirerack/PyYAML-6.0-cp39-cp39-linux_x86_64.whl")

#wheelfab(PkgName="numpy", GitUrl="https://github.com/numpy/numpy.git", TagName="v1.19.3", cwfd=cwfd)
#installwheel("/home/owner/GitHy/tirerack/numpyv1.19.3.whl")
#ERROR: numpyv1.19.3.whl is not a valid wheel filename.
#installwheel("/home/owner/GitHy/tirerack/numpy-1.19.3-cp39-cp39-linux_x86_64.whl")

#wheelfab(PkgName="setuptools", GitUrl="https://github.com/pypa/setuptools.git", TagName="v52.0.0", cwfd=cwfd)#v61.2.0


#wheelfab(PkgName="pandas", GitUrl="https://github.com/pydata/pandas.git", TagName="v1.4.1", cwfd=cwfd)
exit()
wheelfab(PkgName="sphinx", GitUrl="https://github.com/sphinx-doc/sphinx.git", TagName="v4.4.0", cwfd=cwfd)
wheelfab(PkgName="six", GitUrl="https://github.com/benjaminp/six.git", TagName="1.16.0", cwfd=cwfd)
wheelfab(PkgName="pyinstaller", GitUrl="https://github.com/pyinstaller/pyinstaller.git", TagName="v4.10", cwfd=cwfd)
wheelfab(PkgName="PyOpenGL", GitUrl="https://github.com/mcfletch/openglcontext.git", TagName="dd03eba62c5636cff309e8def4422af807614288", cwfd=cwfd)#PyOpenGL

#https://github.com/pyside/pyside-setup
#wheelfab(PkgName="pyside2", GitUrl="https://github.com/pyside/pyside2-setup.git", TagName="v5.15.2", cwfd=cwfd)# needs libclang-dev, python3-dev, libpython3-dev, and qtbase5-private-dev #v5.15.2 worked and v6.0.1 didn't
#wheelfab(PkgName="pyside", GitUrl="https://github.com/pyside/pyside-setup.git", TagName="69d43ea814788a18e8d77920d493fd84f6fc699a", cwfd=cwfd)
#wheelfab(PkgName="pyside", GitUrl="https://code.qt.io/cgit/pyside/pyside-setup.git", TagName="69d43ea814788a18e8d77920d493fd84f6fc699a", cwfd=cwfd)

#wheelfab(PkgName="pyside", GitUrl="https://code.qt.io/cgit/pyside/pyside-setup.git", TagName="v5.15.2.1", cwfd=cwfd)
#exit()

 #qtchooser -print-env
#QT_SELECT="default"
#QTTOOLDIR="/usr/lib/qt5/bin"
#QTLIBDIR="/usr/lib/x86_64-linux-gnu"
#/home//Qt/5.6/gcc_64/bin
#/home//Qt/5.6/gcc_64


#https://github.com/hylang/hy
exit()
wheelfab(PkgName="hy", GitUrl="https://github.com/hylang/hy.git", TagName="0.14.0", cwfd=cwfd)
#https://github.com/kennethreitz/clint
wheelfab(PkgName="clint", GitUrl="https://github.com/kennethreitz/clint.git", TagName="v0.5.1", cwfd=cwfd)
#https://github.com/alex/rply.git
wheelfab(PkgName="rply", GitUrl="https://github.com/alex/rply.git", TagName="v0.7.5", cwfd=cwfd)
#https://github.com/sympy/sympy
wheelfab(PkgName="sympy", GitUrl="https://github.com/sympy/sympy.git", TagName="sympy-1.1.1", cwfd=cwfd)
#https://github.com/scipy/scipy
wheelfab(PkgName="scipy", GitUrl="https://github.com/scipy/scipy.git", TagName="v1.0.1", cwfd=cwfd)
#https://github.com/matplotlib/matplotlib
wheelfab(PkgName="matplotlib", GitUrl="https://github.com/matplotlib/matplotlib.git", TagName="v2.2.2", cwfd=cwfd)
#https://github.com/defnull/bottle
wheelfab(PkgName="bottle", GitUrl="https://github.com/defnull/bottle.git", TagName="0.12.13", cwfd=cwfd)
#https://github.com/mitsuhiko/flask
wheelfab(PkgName="flask", GitUrl="https://github.com/mitsuhiko/flask.git", TagName="1.0", cwfd=cwfd)

exit()
		#this kindof worked once #[cwfd + '/BootStrap/bin/python3', '-m', 'pip', 'wheel', '--no-deps', PkgDir   \
        #from https://stackoverflow.com/a/39579922/144020
        #and https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
