#!/usr/bin/env python
import socket
import os
import re
class Host:
  @staticmethod
  def getHostname( ): 
    return socket.gethostname()
  @staticmethod
  def getHost():
    return socket.gethostbyname( Host.getHostname() )
  @staticmethod
  def getNetPorts():
    cmd = None
    if os.sys.platform == 'darwin' :
      cmd = "ifconfig -L | grep -E \"^\\S\" | awk -F':' '{print $1}'"
    else :
      cmd = "ifconfig  -s | awk -F' ' '{print $1}'"
    txt = os.popen( cmd ).read().strip()
    return txt.split("\n")[1:]
  @staticmethod
  def getIp( port = "eth0"):
    txt = os.popen("ifconfig %s | grep \"inet addr\"" % port ).read()
    g = re.search(r'inet addr:(\S+)',txt)
    return g.group(1)
  @staticmethod
  def getHWaddr( port ) :
    txt = os.popen("ifconfig " + port + "| grep HWaddr | awk '{ print $5 }'").read().strip()
    return txt

if __name__ == '__main__':
  print Host.getHWaddr( "eth0")
  print Host.getIp( "eth0")
