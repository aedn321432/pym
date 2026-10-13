### 리스트의 기본 사용

리스트를 생성하고 인덱스로 원소를 확인한 뒤, `append()`를 이용해 데이터를 추가.

```python
# 문자열 5개가 들어 있는 리스트 생성
kakao = ["가나", "다라", "마바", "사아", "자차"]

print(kakao)       # 리스트 전체 출력
print(kakao[0])    # 인덱스 0인 첫 번째 항목 출력
print(kakao[4])    # 인덱스 4인 다섯 번째 항목 출력

kakao.append(None)  # 리스트 끝에 None 추가
print(kakao)        # None이 추가된 리스트 출력

kakao.append("카타")  # 리스트 끝에 문자열 "카타" 추가
```

**핵심 내용**

- 리스트의 인덱스는 `0`부터 시작한다.
- `append(값)`은 리스트의 맨 뒤에 새로운 항목을 추가한다.
- `None`은 값이 없음을 나타내는 파이썬 객체이다.

### 리스트 데이터 추가 및 변경

빈 리스트에 데이터를 추가하고, 인덱스를 이용해 각 위치의 값을 변경.

```python
kakao = []  # 빈 리스트 생성

# 리스트 끝에 데이터를 하나씩 추가
kakao.append("다현0")
kakao.append("다현1")
kakao.append("다현2")
kakao.append("다현3")
kakao.append("다현4")
print(kakao)  # 추가한 데이터 확인

kakao.append(kakao[4])  # 인덱스 4의 값을 리스트 끝에 한 번 더 추가
print(kakao)

kakao[4] = kakao[3]  # 인덱스 4의 값을 인덱스 3의 값으로 변경
print(kakao)
kakao[3] = kakao[2]  # 인덱스 3의 값을 인덱스 2의 값으로 변경
print(kakao)
kakao[2] = "삽입"     # 인덱스 2의 값을 문자열 "삽입"으로 변경
print(kakao)
```

**핵심 내용**

- `리스트.append(값)`은 리스트 끝에 값을 추가한다.
- `리스트[인덱스] = 값`은 해당 인덱스에 저장된 값을 변경한다.
- 리스트의 특정 값을 바꾸는 것은 새로운 항목을 중간에 삽입하는 것과는 다르다.

### 노드 생성과 링크 연결

연결 리스트는 각 노드가 데이터와 다음 노드에 대한 참조를 저장하는 구조.

```python
# 노드 클래스 정의
class Node():
    def __init__(self):
        self.data = None  # 노드에 저장할 데이터
        self.link = None  # 다음 노드를 가리키는 참조

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
node3.link = node4       # node3 다음에 node4 연결

node5 = Node()           # 다섯 번째 노드 생성
node5.data = "다현4"
node4.link = node5       # node4 다음에 node5 연결

# link를 따라가며 데이터 출력
print(node1.data, end=" ")
print(node1.link.data, end=" ")
print(node1.link.link.data, end=" ")
print(node1.link.link.link.data, end=" ")
print(node1.link.link.link.link.data, end=" ")
```

**핵심 내용**

- `data`는 노드에 저장되는 값이다.
- `link`는 다음 노드를 가리킨다. 마지막 노드의 `link`는 일반적으로 `None`이다.

### `while`문으로 연결 리스트 순회

첫 번째 노드부터 시작해 다음 노드가 존재하는 동안 링크를 따라 이동하며 모든 데이터를 출력.

```python
# 노드 클래스 정의
class Node():
    def __init__(self):
        self.data = None  # 데이터 저장 공간
        self.link = None  # 다음 노드를 가리키는 참조

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
    print(current.data, end=" ")  # 현재 노드의 데이터 출력
```

**핵심 내용**

- `current`는 현재 방문 중인 노드를 가리키는 변수이다.
- `current = current.link`는 다음 노드로 이동한다는 뜻이다.
- 마지막 노드의 `link`가 `None`이면 `while`문의 조건이 거짓이 되어 반복이 종료된다.
- 출력 결과는 `다현0 다현1 다현2 다현3 다현4`이다.

### 연결 리스트의 데이터 삽입과 삭제

기존 연결 리스트에 `솔라` 노드를 삽입하고, `다현4` 노드를 연결 흐름에서 제외.

```python
# Node class
class Node():
    def __init__(self):
        self.data = None  # 노드에 저장할 데이터
        self.link = None  # 다음 노드를 가리키는 링크

# 첫 번째 노드 생성: 앞 노드가 없으므로 링크 연결은 나중에 설정
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
newNode.link = node2.link    # 새 노드가 원래 다음 노드(node3)를 가리키도록 설정
node2.link = newNode         # node2 다음 노드를 newNode로 변경
# 연결 결과: 다현0 -> 다현1 -> 솔라 -> 다현2 -> 다현3 -> 다현4

# 데이터 삭제: 다현4 노드를 연결 흐름에서 제외
node4.link = node5.link      # node4의 링크를 node5의 링크(None)로 변경
del(node5)                   # node5 변수 삭제

# 연결된 모든 노드의 데이터 출력
current = node1              # 첫 번째 노드부터 시작
print(current.data, end=" ")
while current.link != None:   # 다음 노드가 존재하는 동안 반복
    current = current.link    # 다음 노드로 이동
    print(current.data, end=" ")  # 현재 노드의 데이터 출력
```

**핵심 내용**

- 삽입할 때는 새 노드의 `link`를 먼저 설정하고, 이전 노드의 `link`가 새 노드를 가리키도록 변경한다.
- 삭제할 때는 앞 노드의 `link`를 수정해 삭제할 노드를 연결 흐름에서 제외한다.
- `del(node5)`는 변수 `node5`를 삭제한다. 연결 리스트에서 노드를 제거할 때는 링크를 수정하는 과정이 중요하다.
- 출력 결과는 `다현0 다현1 솔라 다현2 다현3`이다.

### 노드 링크 재설정과 연결 리스트 출력

이 예제에서는 처음에 `node1.link = node1`로 자기 자신을 가리키도록 설정하지만, 이어서 `node1.link = node2`를 실행하기 때문에 첫 번째 링크는 두 번째 노드를 가리키도록 다시 설정된다. 따라서 최종 연결 구조는 정상적인 순서의 연결 리스트가 된다.

```python
# 노드 클래스 정의
class Node():
    def __init__(self):
        self.data = None  # 노드의 데이터 저장 공간
        self.link = None  # 다음 노드에 대한 참조

node1 = Node()
node1.data = "다현"
node1.link = node1       # 일단 자기 자신을 가리키도록 설정

node2 = Node()
node2.data = "다현1"
node1.link = node2       # 앞에서 설정한 링크를 node2로 변경

node3 = Node()
node3.data = "다현2"
node2.link = node3       # node2 다음에 node3 연결

node4 = Node()
node4.data = "다현3"
node3.link = node4       # node3 다음에 node4 연결

node5 = Node()
node5.data = "다현4"
node4.link = node5       # node4 다음에 node5 연결

current = node1              # 첫 번째 노드부터 순회 시작
print(current.data, end=" ") # 첫 번째 노드 데이터 출력

while current.link != None:   # 다음 노드가 있는 동안 반복
    current = current.link    # 다음 노드로 이동
    print(current.data, end=" ")  # 현재 노드 데이터 출력
```

**핵심 내용**

- 변수에 링크를 다시 할당하면 이전에 설정한 링크는 새 링크로 바뀐다.
- 이 코드에서는 `node1.link = node1` 다음에 `node1.link = node2`가 실행되므로 최종적으로 자기 자신을 가리키는 연결은 남지 않는다.
- 출력 결과는 `다현 다현1 다현2 다현3 다현4`이다.
