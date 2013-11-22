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
                reg = re.compile( key )
                matchs = reg.match( path )
                if matchs is not None :
                    handlerMethod = URLS[ key ] 
                    break 
            CACHES[ path ] = handlerMethod 
        if handlerMethod is None :
            return web.notfound()
        else : 
           handlerMethodMethod = handlerMethod['method'];
           if handlerMethodRethod == request or handlerMethodRethod == method :
               return handlerMethod['handler']()
           else :
               web.header('Status Code', '405')
               return "<h1>Method Not Allowed</h1>"

    def POST( self , var = None , args = None ) :
        return self.handler( );
    def GET( self , var = None , args = None ) :
        return self.handler( );
class Server :
    def define( self , path , method , handler ) :
        URLS[ path ]  = {
            "method" : method ,
            "handler" : handler 
        }
    def start( self ) :
        urls = ( '(.*)' , requestHandler )
        app = web.application( urls , globals()  ) 
        app.run();
        APP = app 

if __name__ == '__main__' :
    class myServer( Server ) :
        def fuck( self ) :
            return "fuck"
    DEBUG = True
    server = myServer()
    server.define("/fuck","GET", server.fuck )
    server.start()
