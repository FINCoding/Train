class ball():
    def __init__(self):
        self.x = 10
        self.y = 20
a = [ball() for x in range(12)]
for b in a:
    print(b.x, end = ' ')
for b in a:
    b.x += 10
for b in a:
    print('\n', b.x, end = ' ') 
