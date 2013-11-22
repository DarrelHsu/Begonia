import web
import re
DEBUG = False 
URLS={}
CACHES={}
APP = None
class requestHandler :
    def POSTHandler( self ) :
        pass
    def GETHandler( self ) :
        pass
    def handler( self ) :
        req = web.ctx.env
        path = req['PATH_INFO']
        query = req['QUERY_STRING']
        method = req['REQUEST_METHOD']
        handlerMethod = None 
        if DEBUG is True :
            if path == '/shutdown' :
                exit()
        if path in CACHES :
            handlerMethod = CACHES[ path ]
        elif path in URLS :
            handlerMethod = URLS[ path ]
        else :
            for key in URLS :
                reg = re.compile( "^%s$" % key )
                matchs = reg.match( path )
                if matchs is not None :
                    handlerMethod = URLS[ key ] 
                    break 
            CACHES[ path ] = handlerMethod 
        if handlerMethod is None :
            return web.notfound()
        else : 
           handlerMethodMethod = handlerMethod['method'];
           if handlerMethodMethod == "REQUEST" or handlerMethodMethod == method :
               return handlerMethod['handler']()
           else :
               web.header('Status Code', '405')
               return "<h1>Method Not Allowed</h1>"

    def POST( self , var = None , args = None ) :
        return self.handler( );
    def GET( self , var = None , args = None ) :
        return self.handler( );
def add_request_handler( path , fn , method = None ) :
    if method is None :
        method = "REQUEST"
    else :
        method = method.upper(  ) 
        if method != 'GET' and method != 'POST' :
            method = 'GET'
        URLS[ path ]  = {
            "method" : method ,
            "handler" : fn
        }
def request_method( path , method = "REQUEST" ):
    def _( *args , **kws ): 
        fn = args[0]
        add_request_handler( path , fn , method )
    return _

def GET( path ) :
    def _( *args , **kws ): 
        fn = args[0]
        add_request_handler( path , fn , "GET" )
    return _

def POST( path ) :
    def _( *args , **kws ): 
        fn = args[0]
        add_request_handler( path , fn , "POST" )
    return _

class Server :
    def start( self ) :
        urls = ( '(.*)' , requestHandler )
        app = web.application( urls , globals()  ) 
        app.run();
        APP = app 

if __name__ == '__main__' :
    class myServer( Server ) :
        @GET("/fuck")
        def fuck( ) :
            return web.input()
            return "fuck"
    DEBUG = True
    server = myServer()
    server.start()
