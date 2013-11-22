import web
URLS={}
class requestHandler :
    
    def POSTHandler( self ) :
        pass
    def GETHandler( self ) :
        pass
    def handler( self ) :
        return web.ctx
    def POST( self ) :
        return self.handler( );
    def GET( self ) :
        return self.handler( );
class Server :
    def start( self ) :
        urls = ( '(.*)' , requestHandler )
        app = web.application( urls , globals()  ) 
        app.run();
