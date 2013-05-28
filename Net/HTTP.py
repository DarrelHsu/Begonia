#!/usr/bin/python
import httplib
import re
import urllib
class HTTP :
   def __init__( self , headers = None ) :
     if headers is None :
       self.headers = {'Accept': 'text/html;;q=0.9,*/*;q=0.8', 'User-Agent': 'UIDown StupidSpider http://www.uidown.com/aboutspider.html'}
     else :
       self.headers = headers 
   def request( self , url ,  method = 'GET' , params = None ) :
     global conn 
     print "request" , method , url
     urlmatch = re.match(  r"^(http(?:s)?)://((?:[^(?:\?|/)])+)(/[^\?]*)?(?:\?(.*))?$" , url )
     self.protocol = urlmatch.group(1)
     self.server = urlmatch.group(2)
     self.path = urlmatch.group(3)
     self.query = urlmatch.group(4)
     if self.protocol == "http" :
       conn = httplib.HTTPConnection( self.server )
     elif self.protocol == "https" :
       conn = httplib.HTTPSConnection( self.server )
     if params is not None :
       if self.query is None :
         self.query = urllib.urlencode( params ) 
       else :
         self.query = self.query + "&" + urllib.urlencode( params ) 
     if method == 'GET' :
       if self.path is None :
         self.path = "/" 
       if self.query is not None :
         self.path = self.path + "?" + self.query
     conn.request( method , self.path , self.query , self.headers )
     req = conn.getresponse()
     if req.status == 301 or req.status == 302 :
       redirecturl = req.getheader("location") 
       print "%s found , redirect to %s " %( req.status , redirecturl )
       return self.request( redirecturl , method , params )
     else :
     #if req.status == '301' || req.status == '302' :
     #  print req.
       ret = req.read()
       conn.close()
       return ret
   def get( self , url ) :
     return self.request( url , "GET" ) 
   def post( self , url , params = None ) :
     self.headers["Content-type"] = "application/x-www-form-urlencoded; charset=utf-8"
     return self.request( url , "POST" , params ) 

if __name__ == '__main__' :
  http = HTTP( ) ;
  print http.get("http://127.0.0.1?fuckyou=yes")
