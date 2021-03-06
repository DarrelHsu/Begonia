import web
import re
DEBUG = False 
__urls__={
    "GET" : {} ,
    "POST" : {}  
}
__caches__={
    "GET" : {} ,
    "POST" : {}  
}
APP = None
class requestHandler :
    def POSTHandler( self ) :
        pass
    def GETHandler( self ) :
        pass
    def handler( self ) :
        req = web.ctx.env
        path = req['PATH_INFO']
        method = req['REQUEST_METHOD']
        handlerMethod = None 
        if DEBUG is True :
            if path == '/shutdown' :
                exit()
        if path in __caches__[ method ] :
            handlerMethod = __caches__[ method ] [ path ]
        elif path in __urls__[ method ]  :
            handlerMethod = __urls__[ method ] [ path ]
        else :
            for key in __urls__ :
                reg = re.compile( "^%s$" % key )
                matchs = reg.match( path )
                if matchs is not None :
                    handlerMethod = __urls__[ method ][ key ] 
                    break 
            __caches__[ method ][ path ] = handlerMethod 
        if handlerMethod is None :
            return web.notfound()
        else : 
            return handlerMethod( req )

    def POST( self , var = None , args = None ) :
        return self.handler( );
    def GET( self , var = None , args = None ) :
        return self.handler( );
def __add_request_handler( path , fn , method = None ) :
    if method is None :
        method = "REQUEST"
    else :
        method = method.upper(  ) 
        if method != 'GET' and method != 'POST' :
            method = 'GET'
        __urls__[ method ] [ path ]= fn
def __request_method( path , method = "REQUEST" ):
    def _( *args , **kws ): 
        fn = args[0]
        __add_request_handler( path , fn , method )
    return _

def GET( path ) :
    def _( *args , **kws ): 
        fn = args[0]
        __add_request_handler( path , fn , "GET" )
    return _

def POST( path ) :
    def _( *args , **kws ): 
        fn = args[0]
        __add_request_handler( path , fn , "POST" )
    return _

class Server :
    def start( self ) :
        urls = ( '(.*)' , requestHandler )
        app = web.application( urls , globals()  ) 
        app.run();
        self.app = APP = app 

if __name__ == '__main__' :
    class myServer( Server ) :
        @GET("/fuck")
        def fuck( ) :
            return web.input()
        @POST("/fuck")
        def fuckpost() :
            return web.data()
    DEBUG = True
    server = myServer()
    server.start()
