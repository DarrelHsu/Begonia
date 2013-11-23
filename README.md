Begonia
=======

python 2.7 development utils

### Begonia Server
- Be sure that `web.py` has been installed
- import Begonia

```python
   """
      myServer.py
   """
    import Begonia
    class myServer( Begonia.Server.server )
        @GET("/test")
        def test_get( ) :
            return "test"
    myServer().start()
```
    
```shell
    python myServer.py 8080
```
