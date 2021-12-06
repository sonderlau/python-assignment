from icecream import ic

st = {}

n = int(input())

for i in range(0, n):
    get = input()
    start = 0
    for x in range(0, len(get)):
        if get[x].isdigit():
            start = x
            break
    
    st[get[0:start]] = {}

    st[get[0:start]]['val'] = float(get[start:])
    # the first is larger
    st[get[0:start]]['pri'] = -i
    


st = sorted(st.items(), key= lambda x: (-x[1]['val'], x[1]['pri']), reverse=True)


class BTree:
    def __init__(self, data, weight, pri):
        self.data = data
        self.weight = weight
        self.pri = pri
        self.left = None
        self.right = None
    

nodes = []
for k in enumerate(st):
    b2Tree = BTree(k[1][0], k[1][1]['val'], k[1][1]['pri'])
    nodes.append(b2Tree)


def get_lr_tree(left: BTree, right: BTree):
    if left.weight > right.weight:
        return [right, left]
    elif left.weight < right.weight:
        return [left, right]
    else:
        if left.pri < right.pri:
            return [right, left]
        else:
            return [left, right]
        


while(True):
    if len(nodes) == 1:
        break
    b2Tree = BTree(None, nodes[0].weight + nodes[1].weight, -n-1)
    n += 1
    b2Tree.left, b2Tree.right = nodes[0], nodes[1]
    del nodes[0]
    del nodes[0]
    
    nodes.append(b2Tree)
    
    ic(b2Tree.left.data, b2Tree.right.data, b2Tree.pri)
    
    nodes = sorted(nodes, key= lambda x: (x.weight, -x.pri))
    
    for x in nodes:
        ic(x.data, x.weight, x.pri)

    


head = nodes[0]


def preOrderTraverse(node:BTree, path:str):
    if node.data != None:
        print("{}:{}".format(node.data, path))
    if node.left != None:
        preOrderTraverse(node.left, path+"0")
    if node.right != None:
        preOrderTraverse(node.right, path+"1")
    
preOrderTraverse(head, "")

# get code
code = input()

print("original:", end="")
while len(code) != 0:
    if code[0] == '0':
        head = head.left
    elif code[0] == '1':
        head = head.right
    
    if head != None and head.data != None:
        print(head.data, end="")
    
    if head.left == None and head.right == None:
        head = nodes[0]
    
    code = code[1:]
    