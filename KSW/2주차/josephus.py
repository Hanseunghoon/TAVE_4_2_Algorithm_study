# josephus perpumtation 요세퍼스 순열이라고하는 문제
# 1번부터 N번까지 사람이 원으로 둘러 앉아있고, 양의 정수 M이 주어진다. 이때, 이제 순서대로 M번째 사람을 제거한다.
# 한사람이 제거되면 나머지 사람들로 이루어진 원을 따라 이 과정을 계속한다. 이 과정은 N명의 사람이 제거될 때까지 한다.
# 원에서 사람이 제거되는 순서를 (N, M) 조세퍼스 순열이라는 프로그램을 작성하여라.

# 입력 / N, M이 빈칸을 사이에 두고 순서대로 (1 N, M 5,000)
# 출력 / <
# 예시 1, 2, 3, 4, 5, 6, 7 <N, M> = <7, 3>
# 2, 3, 4, 5, 6, 7, 1
# 접근방법:
'''
arr = []
new_arr = []

n, k = map(int, input().split())
index = 0
for i in range(1, n+1):
    arr.append({"v" : i, "n" : (i+1) % n})

while len(arr) > 0 :
    index = (index + k - 1) % len(arr)
    arr[index - 1]["n"] = arr[(index + 1) % len(arr)]["v"]
    new_arr.append(str(arr.pop(index)["v"]))

print("<%s>" %(", ".join(new_arr)))
'''

'''
a,b=map(int,input().split())
answer=list(range(1,a+1))
idx=-1
print("<",end="")
while(len(answer)!=0):
    idx+=b
    idx=idx%(len(answer))
    if len(answer)==1:
        print(answer.pop(idx),end=">")
    else:
        print(answer.pop(idx),end=", ")
    idx-=1
'''

import sys

class Queue():

    def __init__(self, size):
        self.maxSize = size
        self.size = 0
        self.arr = ['']*size
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if not self.isFull():
            self.rear = (self.rear+1) % self.maxSize
            self.arr[self.rear] = data
            self.size += 1

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.maxSize
            self.size -= 1
            return self.arr[self.front]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.maxSize

    def __bool__(self):
        return self.isEmpty()

'''

a, b = map(int, sys.stdin.readline().strip().split())

people = Queue(a)

for i in range(1, a+1):
    people.enqueue(str(i))

result = '<'

while not people.isEmpty():
    for i in range(b-1):
            people.enqueue(people.dequeue())
    result += str(people.dequeue())
    if not people.isEmpty():
        result += ', '
    else:
        result += '>'


sys.stdout.write(result)
'''

'''
import sys
import math

class Queue:
    def __init__(self, capacity):
        self.maxsize = capacity
        self.front = 0
        self.rear = 0
        self.arr = [0] * self.maxsize

    def isFull(self):
        if self.front == (self.rear +1) % self.maxsize :
            return 1
        else :
            return 0

    def isEmpty(self):
        if self.front == self.rear :
            return 1
        else :
            return 0

    def enqueue(self, num):
        if self.isFull() == 1:
            return -1
        else :
            self.rear = self.rear+1
            self.rear = self.rear % self.maxsize

            self.arr[self.rear] = num

    def dequeue(self):
        if self.isEmpty() ==1:
            return -1
        else :
            self.front = self.front+1
            self.front = self.front % self.maxsize

            return self.arr[self.front]

    def size(self):
        if self.rear > self.front :
            return self.rear - self.front
        else :
            return self.maxsize - abs(self.rear-self.front)

def main():
    numCases = sys.stdin.readline().rstrip().split(' ')
    numCases = [int(numCases[i]) for i in range(len(numCases))]

    queue = Queue(numCases[0]+1)

    for i in range(1, numCases[0]+1) :
        queue.enqueue(i)

    strarr ="<"
    while True:
        # print("f",queue.front)
        # print("r",queue.rear)
        if queue.size() == 1 :
            strarr+=str(queue.dequeue())
            break
        for i in range(numCases[1]-1):
            pindex = queue.dequeue()
            # print("ppppp",pindex)
            queue.enqueue(pindex)

        pindex = queue.dequeue()
        strarr+=str(pindex)
        strarr+=(", ")

    strarr+=(">")

    print(strarr)

if __name__ == "__main__":
    main()
'''
