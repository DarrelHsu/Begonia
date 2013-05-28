#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
class Progress :
  tiplen = 0
  def start( self ) :
   self.tiplen = 0 
   self.tip = "" 
  def show( self , text ) :
   text = str( text ) 
   clear = self.tiplen * "\b" 
   sys.stdout.write( clear )
   sys.stdout.write( text )
   sys.stdout.flush()
   self.tiplen = len( text )
  def end( self ) :
   self.tiplen = 0 ;


if __name__ == '__main__' :
  import time
  p = Progress()
  p.start()
  for i in xrange( 50 ) :
    tip = "[%s%s]" % ( "=" * i , " " * ( 50 - i ) )
    p.show( tip )
    time.sleep( 0.2 )
  p.end()
