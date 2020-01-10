# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 다음과 같은 조건에 따라 정렬하는 프로그램을 작성하시오
# 길이가 짧은 것부터, 길이가 같으면 사전 순으로
# 입력 / 첫째 줄에 단어의 개수 N이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다.
# 주어지는 문자열의 길이는 50을 넘지 않는다.
# 출력 / 조건에 따라 정렬하여 단어들을 출력한다. 단 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.

# 접근방법:


import sys
from collections import defaultdict

# 한꺼번에 읽어 들이기

strings = sys.stdin.read().splitlines()

# set()으로 중복을 제거해주고 첫줄에는 단어의 개수가 주어지므로 strings[1:]으로 첫줄을 제외한다.
strings = set(strings[1:])


dict_str = {}

# 반복문을 사용하여 단어의 길이를 구분하기 위해 딕셔너리 형태로 만들어준다.
for s in strings :
    dict_str[s] = len(s)

# 각 단어와 단어길이를 맵핑한 것을 sorted()을 정렬해주고, lambda라는 옵션을 준다.
# dict_str.item()은 단어, 단어길이의 쌍으로 묶여 있다. x[0]은 단어, x[1]은 단어길이에 해당하므로
# x[1]을 기준으로 정렬한다는 것이다.
len_words = sorted(dict_str.item(), key = lambda x:x[1])

# 단어길이가 같을 경우, 사전순으로 정렬해줘야 하기 때문에, 같은 길이의 단어끼리 다시 묶어준 다음, 다시 사전순으로 정렬해야함
# defaultdict으로 딕셔너리의 기본값을 -1로 정해주었다. keyerror를 방지
dic_words = defaultdict(lambda : -1)

for w in len_words:
    # key인 w[1]은 단어의 길이이다. w[1]에 해당하는 값이 비어있으면 -1 상태
    if dic_words[w[1]] == -1:
        # 값이 비어있는 상태이므로 리스트 형태로 w[0]을 추가해준다. 같은 단어에 해당하는 단어도 묶기 위해서
        dic_words[w[1]] = [w[0]]
    else:
        # 기본값이 -1이 아니라면 이미 다른 언어가 추가되어 있는 상태라는 것이다. 리스트에서 append()으로 다른 언어를 추가
        dic_words[w[1]].append(w[0])

# 이제 같은 길이의 단어들을 사전 정렬하기 위해 길이, 단어리스트를 쌍으로 꺼낸다.
# 리스트가 하나라면 정렬할 필요가 없어서 조건문을 활용함, 단어리스트를 sorted()으로 정렬하고 다시 원래의 리스트에 다시 저장한다.
for l, w in dic_words.item():
    if len(w) > 1:
        dic_words[l] = sorted(w)

# output
for words in dic_words.values():
    for w in words:
        print(w)
