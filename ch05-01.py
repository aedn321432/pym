class Node():
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()
node1.data = "다현"
node1.link = node1

node2 = Node()
node2.data = "다현1"
node1.link = node2

node3 = Node()
node3.data = "다현2"
node2.link = node3

node4 = Node()
node4.data = "다현3"
node3.link = node3

node5 = Node()
node5.data = "다현4"
node4.link = node5

current = node1
print(current.data, end=" ")
while current.link != None:
    current = current.link
    print(current.data, end=" ")