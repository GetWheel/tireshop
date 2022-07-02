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
'''TireShop.py
check if wheel exists in wheelrack matches version in tireshop.conf do nothing
else for each package listed create wheel of correct version maintianing a 
tarball of a nocheckout that is no files besides git files
'''
#________________________________________________________________Library Imports
import subprocess, threading, re, os, sys, inspect, shutil, argparse, random, math
rows, columns = os.popen('stty size', 'r').read().split() #http://goo.gl/cD4CFf
#"pydoc -p 1234" will start a HTTP server on port 1234, allowing you  to  browse
#the documentation at "http://localhost:1234/" in your preferred Web browser.
cwf = os.path.abspath(inspect.getfile(inspect.currentframe())) # Current Working File
cwfd = os.path.dirname(cwf) # Current Working File Path
#from GitTar import GitTar
import GitHy_BootStrap
#______________________________________________________________________Functions
#https://github.com/cython/cython
#GitHy_BootStrap.PkgInstall(PkgName="alive-progress", GitUrl="https://github.com/rsalmei/alive-progress.git", TagName="", cwfd=cwfd)
    #cython
    #packaging
    #wheel
    #numpy
    #pandas
    #sphinx
    #six
    #pyinstaller
    #PyOpenGL

#____________________________________________________________________Main Script
#GitHy_BootStrap.PkgInstall(PkgName="None", GitUrl=None, TagName=None, cwfd=cwfd)
#GitHy_BootStrap.PkgInstall(PkgName="cython", GitUrl="https://github.com/cython/cython.git", TagName="0.29.28", cwfd=cwfd)
#GitHy_BootStrap.PkgInstall(PkgName="packaging", GitUrl="https://github.com/pypa/packaging.git", TagName="21.3", cwfd=cwfd)
#GitHy_BootStrap.PkgInstall(PkgName="wheel", GitUrl="https://github.com/pypa/wheel.git", TagName="0.37.1", cwfd=cwfd)

GitHy_BootStrap.PkgInstall(PkgName="numpy", GitUrl="https://github.com/numpy/numpy.git", TagName="v1.19.3", cwfd=cwfd)
GitHy_BootStrap.PkgInstall(PkgName="pandas", GitUrl="https://github.com/pydata/pandas.git", TagName="v1.4.1", cwfd=cwfd)
GitHy_BootStrap.PkgInstall(PkgName="sphinx", GitUrl="https://github.com/sphinx-doc/sphinx.git", TagName="v4.4.0", cwfd=cwfd)
GitHy_BootStrap.PkgInstall(PkgName="six", GitUrl="https://github.com/benjaminp/six.git", TagName="1.16.0", cwfd=cwfd)
GitHy_BootStrap.PkgInstall(PkgName="pyinstaller", GitUrl="https://github.com/pyinstaller/pyinstaller.git", TagName="v4.10", cwfd=cwfd)
GitHy_BootStrap.PkgInstall(PkgName="PyOpenGL", GitUrl="https://github.com/mcfletch/openglcontext.git", TagName="dd03eba62c5636cff309e8def4422af807614288", cwfd=cwfd)#PyOpenGL

#GitHy_BootStrap.PkgInstall(PkgName="setuptools", GitUrl="https://github.com/pypa/setuptools.git", TagName="v52.0.0", cwfd=cwfd)#v61.2.0

#https://github.com/pyside/pyside-setup
#GitHy_BootStrap.PkgInstall(PkgName="pyside2", GitUrl="https://github.com/pyside/pyside2-setup.git", TagName="v5.15.2", cwfd=cwfd)# needs libclang-dev, python3-dev, libpython3-dev, and qtbase5-private-dev #v5.15.2 worked and v6.0.1 didn't
#GitHy_BootStrap.PkgInstall(PkgName="pyside", GitUrl="https://github.com/pyside/pyside-setup.git", TagName="69d43ea814788a18e8d77920d493fd84f6fc699a", cwfd=cwfd)
#GitHy_BootStrap.PkgInstall(PkgName="pyside", GitUrl="https://code.qt.io/cgit/pyside/pyside-setup.git", TagName="69d43ea814788a18e8d77920d493fd84f6fc699a", cwfd=cwfd)

#GitHy_BootStrap.PkgInstall(PkgName="pyside", GitUrl="https://code.qt.io/cgit/pyside/pyside-setup.git", TagName="v5.15.2.1", cwfd=cwfd)
#exit()

 #qtchooser -print-env
#QT_SELECT="default"
#QTTOOLDIR="/usr/lib/qt5/bin"
#QTLIBDIR="/usr/lib/x86_64-linux-gnu"
#/home//Qt/5.6/gcc_64/bin
#/home//Qt/5.6/gcc_64


#https://github.com/hylang/hy
exit()
GitHy_BootStrap.PkgInstall(PkgName="hy", GitUrl="https://github.com/hylang/hy.git", TagName="0.14.0", cwfd=cwfd)
#https://github.com/kennethreitz/clint
GitHy_BootStrap.PkgInstall(PkgName="clint", GitUrl="https://github.com/kennethreitz/clint.git", TagName="v0.5.1", cwfd=cwfd)
#https://github.com/alex/rply.git
GitHy_BootStrap.PkgInstall(PkgName="rply", GitUrl="https://github.com/alex/rply.git", TagName="v0.7.5", cwfd=cwfd)
#https://github.com/sympy/sympy
GitHy_BootStrap.PkgInstall(PkgName="sympy", GitUrl="https://github.com/sympy/sympy.git", TagName="sympy-1.1.1", cwfd=cwfd)
#https://github.com/scipy/scipy
GitHy_BootStrap.PkgInstall(PkgName="scipy", GitUrl="https://github.com/scipy/scipy.git", TagName="v1.0.1", cwfd=cwfd)
#https://github.com/matplotlib/matplotlib
GitHy_BootStrap.PkgInstall(PkgName="matplotlib", GitUrl="https://github.com/matplotlib/matplotlib.git", TagName="v2.2.2", cwfd=cwfd)
#https://github.com/defnull/bottle
GitHy_BootStrap.PkgInstall(PkgName="bottle", GitUrl="https://github.com/defnull/bottle.git", TagName="0.12.13", cwfd=cwfd)
#https://github.com/mitsuhiko/flask
GitHy_BootStrap.PkgInstall(PkgName="flask", GitUrl="https://github.com/mitsuhiko/flask.git", TagName="1.0", cwfd=cwfd)

exit()
