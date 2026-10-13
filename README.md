`hello.py` — 리스트의 기본 사용

리스트를 만들어, 인덱스로 값을 읽고, `append()`로 데이터를 추가하는 예제.

```python
# 문자열 5개가 들어 있는 리스트 생성
kakao = ["가나", "다라", "마바", "사아", "자차"]

print(kakao)       # 리스트 전체 출력
print(kakao[0])    # 인덱스 0인 첫 번째 항목 출력
print(kakao[4])    # 인덱스 4인 다섯 번째 항목 출력

kakao.append(None) # 리스트 끝에 None 추가
print(kakao)       # None이 추가된 리스트 출력

kakao.append("카타") # 리스트 끝에 문자열 "카타" 추가
```

리스트의 인덱스는 `0`부터 시작하며, `append()`는 리스트의 맨 뒤에 항목을 추가한다.

`ch03-01.py` — 리스트 데이터 추가 및 변경

리스트에 데이터를 추가한 뒤, 인덱스를 이용해 특정 위치의 값을 다른 값으로 바꾼다.

```python
kakao = []  # 빈 리스트 생성

# 리스트 끝에 데이터를 하나씩 추가
kakao.append("다현0")
kakao.append("다현1")
kakao.append("다현2")
kakao.append("다현3")
kakao.append("다현4")
print(kakao)  # 추가한 데이터 확인

kakao.append(kakao[4])  # 현재 인덱스 4의 값을 리스트 끝에 복사
print(kakao)

kakao[4] = kakao[3]  # 인덱스 4의 값을 인덱스 3의 값으로 변경
print(kakao)
kakao[3] = kakao[2]  # 인덱스 3의 값을 인덱스 2의 값으로 변경
print(kakao)
kakao[2] = "삽입"     # 인덱스 2의 값을 문자열 "삽입"으로 변경
print(kakao)
```

`리스트[인덱스] = 값` 형식으로 리스트의 특정 위치에 있는 데이터를 변경할 수 있다.

`ch04-01.py` — 노드 생성과 링크 연결

`Node` 클래스에는 데이터 저장 공간인 `data`와 다음 노드를 가리키는 `link`가 있다. 각 노드를 만들고 링크를 연결하는 과정을 확인한다.

```python
class Node():
    def __init__(self):
        self.data = None  # 노드에 저장할 데이터
        self.link = None  # 다음 노드를 가리킬 참조

node1 = Node()           # 첫 번째 노드 생성
node1.data = "다현0"     # 첫 번째 노드에 데이터 저장

node2 = Node()           # 두 번째 노드 생성
node2.data = "다현1"
node1.link = node2       # node1 다음에 node2 연결

node3 = Node()           # 세 번째 노드 생성
node3.data = "다현2"
node2.link = node3       # node2 다음에 node3 연결

node4 = Node()           # 네 번째 노드 생성
node4.data = "다현3"
node3.link = node3       # 주의: node3가 자기 자신을 가리키게 됨
                         # node4를 연결하려면 node3.link = node4여야 함

node5 = Node()           # 다섯 번째 노드 생성
node5.data = "다현4"
node4.link = node5       # node4 다음에 node5 연결

# link를 따라가며 각 노드의 데이터 출력
print(node1.data, end=" ")
print(node1.link.data, end=" ")
print(node1.link.link.data, end=" ")
print(node1.link.link.link.data, end=" ")
print(node1.link.link.link.link.data, end=" ")
```

`node3.link = node3`은 `node3`를 자기 자신과 연결하는 코드이다. 따라서 `node4`와 `node5`는 `node1`에서 시작하는 연결 흐름에 포함되지 않는다. 다음 노드로 연결하려면 `node3.link = node4`로 작성해야 한다.

`ch04-02.py` — `while`문으로 연결 리스트 순회

첫 번째 노드에서 시작해 링크가 있는 동안 다음 노드로 이동하며 데이터를 출력한다.

```python
class Node():
    def __init__(self):
        self.data = None  # 데이터 저장 공간
        self.link = None  # 다음 노드 참조

node1 = Node()
node1.data = "다현0"

node2 = Node()
node2.data = "다현1"
node1.link = node2  # 다현0 -> 다현1

node3 = Node()
node3.data = "다현2"
node2.link = node3  # 다현1 -> 다현2

node4 = Node()
node4.data = "다현3"
node3.link = node4  # 다현2 -> 다현3

node5 = Node()
node5.data = "다현4"
node4.link = node5  # 다현3 -> 다현4

current = node1                 # 첫 번째 노드부터 순회 시작
print(current.data, end=" ")    # 첫 번째 노드의 데이터 출력

while current.link != None:      # 다음 노드가 존재하는 동안 반복
    current = current.link       # 다음 노드로 이동
    print(current.data, end=" ") # 현재 노드의 데이터 출력
```

`current = current.link`로 다음 노드로 이동한다. 마지막 노드의 `link`가 `None`이면 반복이 종료된다.

`ch04-03.py` — 연결 리스트의 데이터 삽입과 삭제

기존 연결 리스트에 새 노드 `솔라`를 삽입하고, `다현4` 노드를 연결에서 제외한 뒤 모든 데이터를 출력한다.

```python
# Node 클래스 정의
class Node():
    def __init__(self):
        self.data = None  # 노드의 데이터
        self.link = None  # 다음 노드를 가리키는 링크

# 노드를 생성하고 순서대로 연결: 다현0 -> 다현1 -> 다현2 -> 다현3 -> 다현4
node1 = Node()
node1.data = "다현0"

node2 = Node()
node2.data = "다현1"
node1.link = node2

node3 = Node()
node3.data = "다현2"
node2.link = node3

node4 = Node()
node4.data = "다현3"
node3.link = node4

node5 = Node()
node5.data = "다현4"
node4.link = node5

# 데이터 삽입: 다현1 뒤에 솔라 노드 추가
newNode = Node()             # 새 노드 생성
newNode.data = "솔라"        # 새 노드에 데이터 저장
newNode.link = node2.link    # 새 노드가 원래 다현2를 가리키도록 설정
node2.link = newNode         # 다현1이 새 노드(솔라)를 가리키도록 변경
# 연결 결과: 다현0 -> 다현1 -> 솔라 -> 다현2 -> 다현3 -> 다현4

# 데이터 삭제: 다현4 노드를 연결 흐름에서 제외
node4.link = node5.link      # 다현3의 링크를 다현4의 다음 링크(None)로 변경
del(node5)                   # node5 변수 삭제

# 연결된 모든 노드의 데이터 출력
current = node1              # 첫 번째 노드부터 시작
print(current.data, end=" ")
while current.link != None:   # 다음 노드가 있는 동안 반복
    current = current.link    # 다음 노드로 이동
    print(current.data, end=" ")
```

삽입할 때는 새 노드의 `link`를 먼저 지정한 다음, 이전 노드가 새 노드를 가리키도록 변경한다. 삭제할 때는 앞 노드의 링크를 바꿔 해당 노드를 연결 흐름에서 제외한다. `del(node5)`는 변수 `node5`를 삭제하는 것이며, 연결 리스트에서는 링크를 수정하는 과정이 중요하다.

`ch05-01.py`

```python
class Node():
    def __init__(self):
        self.data = None  # 데이터 저장 공간
        self.link = None  # 다음 노드 참조

node1 = Node()
node1.data = "다현"
node1.link = node1       # 자기 자신을 가리키지만, 아래에서 링크가 다시 변경됨

node2 = Node()
node2.data = "다현1"
node1.link = node2       # node1의 링크를 node2로 변경

node3 = Node()
node3.data = "다현2"
node2.link = node3       # node2 다음에 node3 연결

node4 = Node()
node4.data = "다현3"
node3.link = node4       # node3 다음에 node4 연결


node5 = Node()
node5.data = "다현4"
node4.link = node5       # node4 다음에 node5 연결

current = node1
print(current.data, end=" ")
while current.link != None:
    current = current.link
    print(current.data, end=" ")
```

연결 리스트에서는 각 노드의 링크가 의도한 다음 노드를 가리키는지 확인해야 한다.
