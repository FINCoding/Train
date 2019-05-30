class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [\n' +str(current.value) +'\n'
            while current.next != None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

    def add(self, x):
        self.length += 1
        if self.first == None:
            # self.first и self.last будут указывать на одну область памяти
            self.last = self.first = Node(x, None)
            return
            # здесь, уже на разные, т.к. произошло присваивание
        if self.first.value > x:
            self.first = Node(x, self.first)
        else:
            curr = self.first
            while curr != None:
                if curr.value > x:
                    old.next = Node(x,curr)
                    return
                old = curr
                curr = curr.next
            self.last = old.next = Node(x, None)



                    #self.last.next = self.last = Node(x, None)
                    #print('look')
                    # self.last = Node(x, None)

# def insert_node(L1, L2):
#     for t =


if __name__ == '__main__':
    L = LinkedList()
    L.add(4)
    L.add(3)
    L.add(0)
    L.add(2)
    L.add(1)
    print(L)
    # L2 = LinkedList()
    # L2.add(101)
    # L2.add(515)
    # L2.add(838)
    # print(L2)