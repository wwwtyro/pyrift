from ctypes import *
import os
import sys
import threading
import time
import ctypes

pr = None

root = os.path.dirname(__file__)

try:
    pr = CDLL(os.path.join(root, "_pyrift.so"))
except OSError:
    pr = CDLL("_pyrift.so")
    

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

def get_orientation_quaternion():
    x = ctypes.c_float()
    y = ctypes.c_float()
    z = ctypes.c_float()
    w = ctypes.c_float()
    pr.get_orientation_quaternion(ctypes.byref(x), ctypes.byref(y), ctypes.byref(z), ctypes.byref(w))
    return x.value, y.value, z.value, w.value


