# coding: utf-8



'''class quick_sort:


    def __init__(self,L):
         self.A = L


    def quick(self, left, right):
        self.left = left
        self.right = right # left< right
        if(left < right):
            q = self.partition()
            self.quick(self, left, q)
            self.quick(self, q+1, right)

    def partition(self, left, right):
        x = self.A[left]
        i = left
        j = right

        while(self.i < self.j):
            while(x < self.A[j]):
                j--
            while(x > self.A[i]):
                i++
            if(i < j):
                tmp = self.A[j]
                self.A[j] = self.A[i]
                self.A[i] = tmp
                i++
                j--
            if(i == j and self.A[j]> x)
                j--

        return j

    def p(self):
        print(self.A)
        print("A")
'''
def quick(L, left, right):
    if(left < right):
        q = partition(L, left, right)
        quick(L, left, q)
        quick(L, q+1, right)

def partition(L, left, right):
    x = L[left]
    i = left
    j = right

    while(i < j):
        while(x < L[j]):
            j = j-1
        while(x > L[i]):
            i = i+1
        if(i < j):
            tmp = L[j]
            L[j] =  L[i]
            L[i] = tmp
            i = i+1
            j = j-1
        if(i == j and L[j] > x):
            j = j-1

    return j

f = open("test.txt", "r")

line = f.readlines()
number = int(line[0])
L = []

for i in range(1,number+1):
    L.append(int(line[i]))

quick(L , 0 , number-1)
print(L)
#'''
#quickソートのクラス　→　ソートをして出力する
#関数:
#quick
#partition
#'''
