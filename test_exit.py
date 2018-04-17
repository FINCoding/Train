def outahere():
    import os
    print('Bye bye')
    os._exit(99)
    print('never reached')
if __name__ == '__main__': outahere()
