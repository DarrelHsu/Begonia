def test( args ) :
    print "args is ",args
    def _( *args , **kws ) :
        print "check is",args , kws 
    return _

@test("fuck")
def testFn( ) :
   print "testFn"

#testFn()
