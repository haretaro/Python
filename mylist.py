class Node:
    """A Node of Sequential List"""

    def __init__(self):
        self.data = None
        self.nextnode = None
        self.i = 1

    def __str__(self):
        return str(self.data)

    def hasNext(self):
        return self.nextnode!=None

class ListIterator:
    """Iterator of List class"""
    
    def __init__(self,node):
        self.node = node

    def next(self):
        if self.hasNext():
            raise StopIteration()
        temp = self.node.data
        self.node = self.node.nextnode
        return temp

class List:
    """Sequential List defined by me"""
    
    def __init__(self,data=None):
        self.__end = Node()
        self.__head = self.__end
        self.__length = 0
        if data != None :
            self.append(data)

    def __str__(self):
        if self.__end == self.__head:
            return 'List[]'
        s = 'List['
        node = self.__head
        while node.hasNext():
            s += str(node)+', '
            node = node.nextnode
        return s[:-2]+']'

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return ListIterator(self.__head)

    def add(self,data):
        self.__end.data = data
        self.__end.nextnode = Node()
        self.__end = self.__end.nextnode
        self.__length += 1
        return self

    def append(self,datalist):
        for data in datalist:
            self.add(data)
        return self

    def get(self,n):
        node = self.__head
        for i in range(n):
            if node.hasNext():
                node = node.nextnode
            else:
                raise IndexError
        return node.data

    def getLength(self):
        return self.__length

if __name__ == '__main__':
    l = List(['spam','spam'])
    l.append(['spam','ham']).add('egg').add('ham')
    print(l)
    print('list[0] = '+str(l.get(0)))
    print('length = '+str(l.getLength()))
    print('iteration')
    for x in l:
        print(x)
