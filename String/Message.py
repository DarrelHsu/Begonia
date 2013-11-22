#!/usr/bin/env python
class Message:
 def __init__( self , txt = None ) :
   if txt is not None :
     self.init( txt )
   self.dictMap = {} 
 def init( self , txt ) :
   for line in txt.split( "\n") :



if __name__ == '__main__' :
  import os
  txt = os.popen("ifconfig").read()
  msg = Message( txt )


#
#aaa:1 bbb:2 ccc:3
#
#aaa  bbb:1 ddd:2
#     sdd:2  as:2
#
#
#
#
#
#
#
#
#

