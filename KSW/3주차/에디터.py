# 한줄로 된 에디터를 구현하려고 한다. 영어 소문자만 기록할 수 있는 편집기로 최대 600,000글자까지 입력가능
# 커서는 문장의 맨 앞, 맨 뒤, 중간 / 즉 L인 문자열이 있으면 위치할 수 있는 곳은 L+1가지 경우
# 편집기가 지원하는 명령 : L - 커서를 왼쪽으로 한 칸 옮김(커서 문장의 맨 앞이면 무시) D - 커서를 오른쪽으로 한 칸 옮김(커서가 문장의 맨 뒤면 무시)
# B - 커서가 왼쪽에 있는 문자를 삭제함(), 삭제로 인해 커서는 왼쪽으로 이동한 것처럼 보이지만, P$ - $라는 문자 왼쪽에 추가

# 입력 / 초기에 편집기에 입력되어 있는 문자열이 주어지는데, 영어 소문자로, 길이는 100,000을 넘지 않도록 한다. 둘 째 줄에는 입력할 명령어 개수를 나타낼 정수
# 셋째 줄부터 N개의 줄에 걸쳐 입력할 명령어가 순서대로 주어짐
text = list(input())
dex = len(text)

N = input()

for i in range(N):
    com = input().split(" a`")
    if com[0] == 'L':
        if dex == 0:
            continue
        dex -= 1

    elif com[0] == 'D':
        if dex == len(text):
            continue
        dex += 1

    elif com[0] == 'B':
        if dex == 0:
            continue
        text.pop(dex - 1)
        dex -= 1

    elif com[0] == 'p':
        text.insert(dex, com[-1])
        dex += 1

print(text)
