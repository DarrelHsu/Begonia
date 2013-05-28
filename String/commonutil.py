"""
Common Utils 
author Darrel.Hsu
"""
import time
import hashlib
from curses import ascii
import base64

class TimeUtil :

    @staticmethod
    def getTimestamp( ) :
        now = time.time()
        now = str(now).split(".")
        while len( now[1] ) < 3 :
           now[1] =  str( now[1] ) + "0"
        return now[0] + now[1]

class StringUtil:
    @staticmethod
    def md5( org ):
        md5 = hashlib.md5()
        md5.update( org )
        return md5.hexdigest().upper()

    @staticmethod
    def sig( org ):
        md5 = StringUtil.md5( org )
        return base64.b64encode( md5 )

class UrlUtil:
    @staticmethod
    def decode( url ):
      import urllib
      result = {}
      pms = url.split("&");
      k = 0
      while k < len( pms ) :
        param = pms[ k ]
        k = k + 1
        if param.find("="):
          p = param.split("=")
          if len( p ) == 2 :
            key = p[0]
            val = urllib.unquote_plus( p[1] )
            result[ key ] = val
      return result;

    @staticmethod
    def encode( params ):
        import urllib
        result = []
        for key in params:
           p = {}
           p[key] = params[key]
           result.append( urllib.urlencode( p ) )
        result.sort()
        return "&".join( result )
