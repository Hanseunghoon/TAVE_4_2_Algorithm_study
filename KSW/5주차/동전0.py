# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

# 입력: 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
# 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

# 출력: 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

# 탐욕알고리즘은 최적해를 구하는 상황에서 사용, 여러 경우 중 하나를 선택할 때,

# 입력받기 coins이라는 리스트에 받는다.
N, K = map(int, input().split())

conins = [int(input()) for _ in range(N)]

# 동전 개수 구하기
coin_num = 0

for i in range():
    # index 끝부터 순회하기 // 목표 값인 K보다 작으면서도 가장 큰 가치를 지닌 동전을 찾기 위해 인덱스 끝부
    conin = coins[-i]

    # 가치(coin) K보다 작다면, coin으로 K를 나눈 몫을 num 변수에 담는다.
    if K >= coin:
        num = K/coin
        K -= coin*num # coin 값과 num를 곱한 후 K에서 빼서, K를 최대한 작게 만든다
        coin_num += num # 최소 동전의 갯수이므로 num(동전의 갯수)를 coin_num에 담는다.

print(coin_num)



N, K = input().split()
N = int(N)
K = int(K)
lst = []
for i in range(N):
    a = int(input())
    lst.append(a)
    count = []

for i in range(N):
    count.append(0)

def countCoin(N, K, lst, count):
    lst.reverse()
    for i in range(N):
        count[i] += int(K/lst[i])
        K -= count[i]*lst[i]
        print(count[i])
        print(K)
    return count

ans = countCoin(N, K, lst, count)
result = 0

for i in range(len(ans)):
    result += ans[i]

print(result)
