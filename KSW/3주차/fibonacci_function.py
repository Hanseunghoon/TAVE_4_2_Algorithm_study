# fibonacci 함수 문제: N번째 피보나치 수를 구하는 C++로 작성된 코드 참고,
# fibonacci(3)을 호출하면 fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다. fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
# 두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다. fibonacci(0)은 0을 출력하고, 0을 리턴한다. fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
# 첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다. fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
# 1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오
# 입력 - 테스트 케이스가 T가 주어지고, 갹 테스트 케이스는 한줄로 이루어지고 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.
# 출력 - 각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분

# 접근법: 일단 제시된 재귀함수를 수정하여 문제를 풀게되면 반드시, 시간초과가 분명히 날 것이다.
# 메모이제이션: 동일한 계산을 반복해야 할 때, 이전에 계산한 값을 메모리에 저장함으로써 동일한 계산의 반복 수행을 제거하여 실행 속도 증가시킴

'''
# 피보나치 호출 횟수를 클래스에 저장한다.
class fibN():
    def __init__ (self):
        # zero, one 초기값 설정
        self.zero = -1
        self.one = 0

    # 값 출력하는 show함수
    def show (self):
        print(self.zero, self.one)

# 0부터 40까지의 0과 1의 호출 횟수를 리스트에 저장함
fibo = [fibN() for i in range(41)]
fibo[0].zero = 1
fibo[1].one = 1
fibo[1].zero = 0

for i in range(2, 41):
    if fibo[i].zero != -1:
        continue
    else:
        fibo[i].zero = fibo[i-1].zero + fibo[i-2].zero
        fibo[i].one = fibo[i - 1].one + fibo[i - 2].one

T = int(input())
for i in range(T):
    n = int(input())
    fibo[n].show()

'''

fib = int(input())
result = []

for i in range(fib):
    n = int(input())
    zero = 0
    one = 0
    
    # if문으로 조건을
    if n >= 2:
        for i in range(2, n+1):
