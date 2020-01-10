# 최소 힙과 관련된 문제
# Heap이라는 것은 최솟값, 최댓값을 찾아내는 연산을 빠르게 하기 위해 이진트리 구조이다.
# 두 가지 종류가 있는데, 첫 번째는 부모 노드의 키값이 자식 노드의 키값보다 항상 큰 경우를 최대 힙
# 두 번째는 부모 노드의 키값이 자식 노드의 키값보다 항상 작은 경우를 최소 힙이라고 한다.
# 부모 자식간의 관계에서 이루어지며 힙에서는 항상 우선순위를 가지는 노드가 항상 뿌리 노드에 오는 경우가 대부분이다.
# 우선순위 쿠와 같은 응용을 할 수 있다.
# 최소 힙을 이용하여 다음과 같은 연산을 처리하는 프로그램을 작성하여라
# 1. 배열에 자연수 X를 넣는다. 2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
# 입력 / 첫째 줄에 연산 갯수 N(1 N 100,000)이 주어진다. 다음 N줄에는 연산의 정보를 나타내는 정수 X가 주어짐
# 출력 / 입력에서 0이 주어진 회수 만큼 출력, 배열이 비어있는 경우에는 가장 작은 값을 출력하라고 하면 0을 출력하면 된다.

# 삭제연산: 힙은 최소값, 최대값을 쉽게 찾아내기 위해 고안된 자료형이다. 루트에서만 이루어진다.
# 루트에서 삭제가 이루어지면 다음에 루트가 될 노드를 정해야 함
# 루트에서 노드 삭제, 이진트리를 유지하기 위해 레벨 순서 중 마지막 노드를 루트로 옮김, 루트로 옮겨진 노드와 자식노드 중 더 큰 값을 가지는 노드와 비교
# 만족하지 않는다면, 루트노드와 자식노드를 변경한다.


# sys.stdin.readline()이라는 메소드를 사용한다. 안그러면 input시 시간이 오래걸린다.
import sys

class Heap:
    heap = []
    count = 0
    size = 0

    def __init__(self, size):
        self.heap = [-1 for i in range(0, size)]
        self.count = 0
        self.size  = size

    # 20씩 증가 시킴
    def resizing(self):
        n_heap = [-1 for i in range(0, self.size + 20)]
        for i in range(0, self.size):
            n_heap[i] = self.heap[i]
        self.heap = n_heap
        self.size = self.size + 20


    def is_empty(self):
        if self.count is 0:
            return True
        return False

    def is_full(self):
        if self.count is self.size - 1:
            return True
        return False

    def insert_node(self, key):
        if self.is_full():
            self.resizing()

            self.count += 1
            current_index = self.count

        while int(current_index/2) >= 1:
            if key <= self.heap[int(current_index/2)]:
                break
            self.heap[current_index] = self.heap[int(current_index/2)]
            current_index = int(current_index/2)
        self.heap[current_index] = key

    def delete_node(self):
        # 힙이 비었다면 0으로 리턴
        if self.is_empty():
            return 0

        # delete 원소의 값을 기억
        delete_node = self.heap[1]
        # 마지막 원소를 루트로 정하기
        temp_node = self.heap[self.count]
        self.heap[1] = temp_node
        # 마지막 원소 삭제
        self.heap[self.count] = -1
        # 노드 개수를 줄임
        self.count -= 1

        if self.count is 0:
            return delete_node

        current_node = 1
        child_node = current_node * 2 # 왼쪽 자식 노드(오른쪽 자식 노드: 왼쪽 자식 노드 + 1)

        while child_node + 1 <= self.count:
            if self.heap[child_node] <= self.heap[child_node + 1]:
                child_node = child_node + 1

            if temp_node >= self.heap[child_node]: # 루트
                break

            self.heap[current_node] = self.heap[child_node]
            current_node = child_node
            child_node = child_node * 2

            self.heap[current_node] = temp_node
            return delete_node

'''
    if __name__ == "__main__":
        com_count = int(sys.stdin.readline())
        heap = Heap(com_count)

        for i in range(0, com_count):
            com = int(sys.stdin.readline())
            if com is 0:
                print(heap.delete_node())
            else:
                heap.insert_node(com)
'''
