from ctypes import *
import os
import sys
import threading
import time
import ctypes

pr = None

root = os.path.dirname(__file__)

if "win" in sys.platform:
    develpath = os.path.join(root, "windows", "pyrift", "Release", "pyrift.dll")
    distpath = os.path.join(root, "pyrift.dll")
elif "linux" in sys.platform:
    develpath = os.path.join(root, 'linux', '_pyrift.so')
    distpath = os.path.join(root, '_pyrift.so')
else:
    raise Exception("pyrift not supported on this platform")
if os.path.isfile(develpath):
    pr = CDLL(develpath)
elif os.path.isfile(distpath):
    pr = CDLL(distpath)
else:
    raise Exception("pyrift binary library not found")

pr.initialize.argtypes = []
pr.initialize.restypes = None
pr.get_orientation.argtypes = [c_void_p, c_void_p, c_void_p]
pr.get_orientation.restype = None

def initialize():
    pr.initialize()

def get_orientation():
    yaw = ctypes.c_float()
    pitch = ctypes.c_float()
    roll = ctypes.c_float()
    pr.get_orientation(ctypes.byref(yaw), ctypes.byref(pitch), ctypes.byref(roll))
    return yaw.value, pitch.value, roll.value


