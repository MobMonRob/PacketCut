#!/usr/bin/env python

import sys
import copy
import rospy
import time
import socket


class forceTorque(object):
  def __init__(self):
    super(forceTorque, self).__init__()


    host = "192.168.3.2"    # The remote host
    port = 63351            # The same port as used by the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initialize Socket

    self.threadForce = threadForce
    self.host = host
    self.port = port
    self.sock = sock

  def getForce(self):

    self.sock.connect((self.host, self.port))
    data = self.sock.recv(128)
    self.sock.close()
    
    data = data[1:-1]
    data = data.split()

    fx = abs(float(data[0]))
    fy = abs(float(data[2]))
    fz = abs(float(data[4]))
    mx = abs(float(data[6]))
    my = abs(float(data[8]))
    mz = abs(float(data[10]))

    return fx,fy,fz

  pass
    
