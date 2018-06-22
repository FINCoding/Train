class key0(object):
    def __init__(self, id):
        self.id = id

class key1(object):
    def __init__( self, id ):
        key0.__init__( self, id )
    def __hash__(self):
        return None

dic = {}
