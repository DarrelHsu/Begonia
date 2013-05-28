#!/usr/bin/python
import MySQLdb
class MySql:
  def __init__( self , host='127.0.0.1' , port = 3306 ,user='root',passwd='root', db=None , charset = 'utf8'):
    try:
      self.conn = MySQLdb.connect( host = host , user = user , passwd = passwd , db = db , port = port , charset = charset )   
      self.cur= self.conn.cursor()
    except MySQLdb.Error,e:
      print "Mysql Error %d: %s" % (e.args[0], e.args[1])
  def usedb( self , db ):
    self.conn.select_db( db )
  def close( self ):
    self.cur.close()
    self.conn.close()
  def update( self , sql ):
    self.cur.execute( sql )
    self.conn.commit()
  def query( self , sql ):
    self.cur.execute( sql )
    return self.cur.fetchall();
  def insert( self , table , value ):
    cols = []
    re = []
    vls = []
    for key in value :
      cols.append( '`' + key + '`' )
      vls.append( value[ key ] ) 
      re.append("%s")
    cols = ",".join( cols )
    res = " , ".join( re )
    sql =  "insert into "+ table +" ( "+  cols +" ) values ( "+ res + " ) " 
    self.cur.execute( sql ,  vls );
    self.conn.commit()
    self.cur.execute( "SELECT LAST_INSERT_ID()")
    lid = self.cur.fetchall()
    return lid[0][0]
  def insertmany( self , table , values ):
    self.cur.execute("insert into "+ table +" values ( %s ) " ,  values );
    self.conn.commit()
  def getCur( self ):
    return self.cur 
 

if __name__ == '__main__':
   mysql = MySql( passwd="admin" , db='xiaomi' , host='10.235.3.121') 
   print mysql.query("select * from users")
   mysql.close()
