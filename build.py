import os
import subprocess
import sys
import shlex
import shutil
import argparse

def repo_update():
    subprocess.call(shlex.split('./scripts/feeds update -a'))
    subprocess.call(shlex.split('./scripts/feeds install -a'))

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--rebuild', action="store_true", help='(Re)build project with updating repos')
args = parser.parse_args()

if args.rebuild:
    repo_update()

shutil.copy('./defconfig', './.config')

subprocess.call(shlex.split('make defconfig'))
subprocess.call(shlex.split('make -j8 download'))
subprocess.call(shlex.split('make -j56'))
