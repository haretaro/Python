class Node:
    """A Node of Sequential List"""

    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        self.i = 1

    def __str__(self):
        return str(self.data)

    def hasNext(self):
        return self.next!=None

class ListIterator:
    """Iterator of List class"""
    
    def __init__(self,node):
        self.node = node

    def __next__(self):
        if self.node.hasNext()==False:
            raise StopIteration()
        temp = self.node.data
        self.node = self.node.next
        return temp

class List:
    """Sequential List defined by me"""
    
    def __init__(self,data=None):
        self.__end = Node()
        self.__head = self.__end
        self.__length = 0
        if data != None :
            self.extend(data)

    def __repr__(self):
        if self.__end == self.__head:
            return 'List[]'
        s = 'List['
        node = self.__head
        while node.hasNext():
            s += str(node)+', '
            node = node.next
        return s[:-2]+']'

    def __iter__(self):
        return ListIterator(self.__head)

    def append(self,data):
        self.__end.data = data
        self.__end.next = Node()
        self.__end = self.__end.next
        self.__length += 1
        return self

    def extend(self,datalist):
        for data in datalist:
            self.append(data)
        return self

    def __getitem__(self,n):
        node = self.__head
        for i in range(n):
            if node.hasNext():
                node = node.next
            else:
                raise IndexError
        return node.data

    def __len__(self):
        return self.__length

    def reverse(self):
        prev = Node()
        self.__end = prev
        node = self.__head
        while node.hasNext():
            node.next, node, prev  = prev, node.next, node
        self.__head = prev
        return self
            

if __name__ == '__main__':
    list1 = List(['spam','spam'])
    list1.extend(['spam','ham']).append('egg').append('ham')
    print(list1)
    print('list[0] = '+str(list1[0]))
    print('length = '+str(len(list1)))
    print('iteration')
    for x in list1:
        print(x)
    list2 = List([1,2,3])
    list1.extend(list2)
    print(list1)
    list1.reverse()
    print(list1)
