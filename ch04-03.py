# Node class
class Node():
    def __init__(self):
        self.data = None
        self.link = None

#첫번째 노드 생성 링크 필요 없음
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

# 데이터 삽입
newNode = Node()
newNode.data = "솔라"
newNode.link = node2.link
node2.link = newNode

# 데이터 삭제
node4.link  = node5.link
del(node5) 

# 데이터 모두 출력
current = node1
print(current.data, end=" ")
while current.link != None:
    current = current.link
    print(current.data, end=" ")
