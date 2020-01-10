# 여러개의 쇠막대기를 레이저 절단하려고 한다. 솨막대기를 위에서 아래로 겹쳐놓고 수직으로 발사하여 절단
# 쇠막대기의 배치는 다음과 같다.
# 1. 자신보다 긴막대를 위에 배치 - 쇠막대기를 다른 막대기 위에 놓은 경우 완전히 포함되도록 하되, 끝점은 겹치지 않는다.
# 2. 각 쇠막대기를 자르는 레이저는 적어도 한 개이상이다.
# 3. 레이저는 어떤 양 끝점과도 겹치지 않는다.

# 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 '()' 모든 '()'는 반드시 레이저를 표현한다.
# 쇠막대기의 왼쪽 끝은 '(' 오른쪽 끝은 ')'로 표현된다.
# 쇠막대기는 레이저에 의해 몇 개의 조각으로 잘려지는데, 예시에서 가장 위에 있는 두 개의 쇠막대는 각각 3개와 2개의 조각으로 잘려지지고,
# 위와 같은 방식으로 잘린 쇠막대기는 총 17개의 조각으로 잘린다.


# 접근방법: '()'처럼 붙어있는 괄호는 쇠막대기를 절단한다, '('는 쇠막대기를 생성, ')'는 쇠막대기가 끝난다.
# 절단된 쇠막대기 갯수를 누적해서 더해줄 변수, 현재 생성된 쇠막대기의 갯수를 뜻하는 변수가 필요하고
# '('가 나오는 경우, ')'가 나왔는데 전자가 ')'인 경우, ')'가 나왔는데 전자가 '('인 경우로 나누어 생각한다.
'''
input_g = input()

sum = 0

current = 0

for i in range(len(input_g)):
    if input_g[i] == '(':
        current = current + 1
    elif input_g[i] == ')':
        current = current - 1
        if input_g[i-1] == '(':
            sum = sum + current
        else:
            sum = sum + 1

print(sum)
'''

# 만약 다른방법으로 풀면 이거는 스택(stack) / 리스트에 길이값을 넣어주는 방법
# 스택 자료구조는 프레젠테이션으로 설명...
def solution (arrangement):
    token_stack = []
    answer = 0

    for token in arrangement:
        if token == "(":
            token_stack.append(token)
            # 리스트라는 변수에 token을 넣어줌
            last = token
        else:
            if last == "(":
                token_stack.pop()
                answer += len(token_stack)
                last = token
            else:
                token_stack.pop()
                answer += 1

    return answer

# 다른 방법으로 푸는 방법
def solution (arragement):
    answer  = 0
    num_stick = 0
    last = 'open'

# 입력 괄호를 루프를 돌면서 만약 괄호가 (라면 쇠막대기 갯수를 하나씩 증가시키고, 마지막 요소는 open으로 표시
    for token in arragement:
        if token == '(':
            num_stick += 1
            last = 'open'
        # 만약 닫힌괄호 )인데, 마지막요소가 open이라면 레이저를 의미함, 즉 괄호가 열렸다가 닫힌 ()을 의미
        else:
            if last == 'open':
                num_stick -= 1
                answer += num_stick
                last = 'close'
            else:
                num_stick -= 1
                answer += 1

    return answer
