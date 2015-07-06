class Node:
    """A Node of Sequential List"""

    def __init__(self):
        self.data = None
        self.next = None

    def __str__(self):
        return str(self.data)

    def hasNext(self):
        return self.next!=None

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
            node = node.next
        return s[:-2]+']'

    def __repr__(self):
        return self.__str__()

    def add(self,data):
        self.__end.data = data
        self.__end.next = Node()
        self.__end = self.__end.next
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
                node = node.next
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
