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
'''GitHy_BootStrap.py
Provides a Virtualenv BootStrap with the latest stable version of the following
packages:
    cython
    packaging
    wheel
'''
#________________________________________________________________Library Imports
import subprocess, threading, re, os, sys, inspect, shutil, argparse, random, math, gittar
rows, columns = os.popen('stty size', 'r').read().split() #http://goo.gl/cD4CFf
#"pydoc -p 1234" will start a HTTP server on port 1234, allowing you  to  browse
#the documentation at "http://localhost:1234/" in your preferred Web browser.
cwf = os.path.abspath(inspect.getfile(inspect.currentframe())) # Current Working File
cwfd = os.path.dirname(cwf) # Current Working File Path

#______________________________________________________________________Functions

def PkgInstall(PkgName=None, GitUrl=None, TagName=None, cwfd=None):
	print(cwfd)
	gittar.gittar(PkgName=PkgName, GitUrl=GitUrl, TagName=TagName, cwfd=cwfd)
	PkgDir = cwfd + '/Pkg/' + PkgName
	SPObject_PkgInstall = subprocess.Popen(
#		[cwfd + '/BootStrap/bin/python', PkgDir + '/setup.py', 'install', '--qtpaths=/usr/lib/x86_64-linux-gnu/qt5/bin/qtpaths', '--parallel=4'], #'--qtpaths=/usr/lib/qt5/bin'
		[cwfd + '/BootStrap/bin/python3', PkgDir + '/setup.py', 'install', \
            #'--qtpaths=/usr/lib/qt5/bin', \
            #'--parallel=4'
            ], #'--qtpaths=/usr/lib/qt5/bin' #], #'--qtpaths=/usr/lib/qt5/bin'
		stdin=None, stdout=None, stderr=None, cwd=PkgDir, env=None)
	SPObject_PkgInstall.wait()

#____________________________________________________________________Main Script
if __name__ == "__main__":
	#gittar(GitUrl="https://github.com/pypa/virtualenv.git", PkgName="virtualenv", TagName="20.4.4", cwfd=cwfd)
	SPObject_BootStrap = subprocess.Popen(
		['python3', '-m', 'venv', cwfd + '/BootStrap'],
		stdin=None, stdout=None, stderr=None, cwd=cwfd, env=None)
	SPObject_BootStrap.wait()
	SPObject_init = subprocess.Popen(
		[cwfd + '/BootStrap/bin/python3', cwfd + '/init.py'],
		stdin=None, stdout=None, stderr=None, cwd=cwfd, env=None)
	SPObject_init.wait()

	#https://github.com/pypa/virtualenv
	#PkgInstall(PkgName="virtualenv", GitUrl="https://github.com/pypa/virtualenv.git", TagName="20.4.4", cwfd=cwfd)
	pass#print "This program wasn't called by another python"
else:
	pass#print "This program was called by another python"

##from http://goo.gl/9XO7sa
#SPObject_Unzip = subprocess.Popen( ['gzip', '-dc', './virtualenv-tmp.tar.gz'],
#	stdin=None, stdout=subprocess.PIPE, stderr=None, cwd=cwfd, env=None)
#SPObject_Untar = subprocess.Popen( ['tar', '-xpvf', '-'],
#	stdin=SPObject_Unzip.stdout, stdout=None, stderr=None, cwd=cwfd, env=None)
#SPObject_Unzip.stdout.close()  # Allow SPObject_Unzip to receive a SIGPIPE if p2 exits.
#SPObject_Untar.wait()
#if (SPObject_Untar.returncode == 0):
#	print "\n\'virtualenv-tmp.tar.gz\' has been unzipped.\n"
#else:
#	print "unzip failed\n"

