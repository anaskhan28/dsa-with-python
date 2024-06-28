class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0
    
    def __len__(self):
        return self.n
    
    def add(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next!= None:
                curr = curr.next
            curr.next = new_node
        self.n += 1
       
    

    
    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n = self.n+1

    def traverse(self):
        curr = self.head
        while curr!= None:
            print(curr.data)
            curr = curr.next
    
    def __str__(self) -> str:
        curr = self.head

        result = ""
        while curr!= None:
            result = result + str(curr.data) + '->'
            curr = curr.next

        return result[:-2]
    

    def delete_head(self):
        if self.head == None:
            return "Empty LL"
        
        self.head = self.head.next
        self.n = self.n-1
    
    def pop(self):

        if self.head == None:
            return print("Empty LL")
         
        curr = self.head

        if curr.next == None:
            return self.delete_head()

        while curr.next.next!=None:
            curr = curr.next
        curr.next = None
        self.n = self.n-1
    
    def remove(self, value):

        if self.head == None:
            return "Empty LL"

        if(self.head.data == value ):
            return self.delete_head()

        curr = self.head

        while curr.next!=None:
            if curr.next.data == value:
                break
            curr = curr.next
        
        if curr.next == None:
            return "ITEM NOT FOUND"
        else:
            curr.next = curr.next.next
    
    def search(self, item):
        
        curr = self.head
        pos = 0

        while curr!=None:
            if curr.data == item:
                return pos 
            curr = curr.next
            pos = pos +1
        
        return "NOT FOUND"
    
    def __getitem__(self, index):

        curr = self.head
        pos = 0

        while curr!= None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos = pos +1

        return "IndexError Found"
    
    def replace_max(self, value):

        temp = self.head
        Max = temp
        while temp!= None:
            if temp.data > Max.data:
                Max = temp
            temp = temp.next
        Max.data = value

    def sum_odd_pos(self):
        temp = self.head
        counter = 0
        result = 0

        while temp!=None:
            if counter%2 != 0:
                result = result + temp.data
            counter = counter + 1
            temp = temp.next
        print(result)

    def reverse(self):
        prev_node = None
        curr_node = self.head

        while curr_node!=None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node
    
    def change_sent(self):
        
        temp = self.head

        while temp!=None:
            if temp.data == "*" or temp.data == "/":
                temp.data = " "

                if temp.next.data == "*" or temp.next.data == "/":
                    temp.next.next.data = temp.next.next.data.upper()
                    temp.next = temp.next.next
            temp = temp.next





L = LinkedList()
a= L.add("T")
a= L.add("h")
a= L.add("e")
a= L.add("/")
a= L.add("*")
a= L.add("s")
a= L.add("k")
a= L.add("y")
a= L.add("*")
a= L.add("i")
a= L.add("s")
a= L.add("/")
a= L.add("/")
a= L.add("b")
a= L.add("l")
a= L.add("u")
a= L.add("e")


# print(len(L))
# L.traverse()

print(L)
# print(L.sum_odd_pos())
L.change_sent()
# L.traverse()
print(L)

