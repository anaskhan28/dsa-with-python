import ctypes

class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0

        # create a C type array with size = self.size
        self.A = self.__make_array(self.size)
    
    def __len__(self):
        return self.n
    
    def append(self, item):
        if self.n == self.size:
            self.__resize(2* self.size)
        self.A[self.n] = item
        self.n +=1
    
    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity)
        for i in range(self.n):
            B[i] = self.A[i]
       
        self.size = new_capacity
        self.A = B
    
    def __str__(self):
        result = ""
        for i in range(self.n):
            result = result+str(self.A[i]) + ','
            
        return '[' + result[:-1] + ']'
    
    def __getitem__(self, index):
        if 0<=index < self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of bound!'

    def pop(self):
        if self.n == 0:
            return "Empty list"
        print(self.A[self.n-1])
        self.n = self.n -1
    
    def clear(self):
        self.size = 1
        self.n = 0

    def insert(self, item, pos):
        if self.n == self.size:
            self.__resize(self.size*2)
        
        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i-1]
        
        self.A[pos] = item
        self.n = self.n+1

    def __delitem__(self, pos):
        if 0<=pos<self.n:
        # delete
            for i in range(pos, self.n-1):
                self.A[i] = self.A[i+1]

                self.n = self.n-1
        else:
            'Index Value not found!'
    
   
    
    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'ValueError - not in the list'
    
    def remove(self, item):
        pos = self.find(item)

        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos


    def __make_array(self, capacity):
        # creates a C types array(static, referential) with size capacity
        return (capacity*ctypes.py_object)()
    

L = MeraList()

L.append('hello')
L.append(1)
L.append(5)
L.append(8)
L.append(True)

# print(L[0])
# print(L[4])
# print(L[6])
# L.insert(50, 0)
print(L)
L.remove(True)
print(L)
# L.pop()
# L.clear()
# print(L.find(5))
# print(L.find("nhot"))

# print(L)
# print(len(L))

    