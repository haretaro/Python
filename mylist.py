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
    
    def __init__(self):
        self.__end = Node()
        self.__head = self.__end
        self.__length = 0

    def __str__(self):
        s = '['
        node = self.__head
        while node.hasNext():
            s += str(node)+', '
            node = node.next
        return s[:-2]+']'

    def append(self,data):
        self.__end.data = data
        self.__end.next = Node()
        self.__end = self.__end.next
        self.__length += 1

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
    l = List()
    l.append(3.14)
    l.append(42)
    l.append('spam')
    print(l)
    print('list[0] = '+str(l.get(0)))
    print('length = '+str(l.getLength()))
