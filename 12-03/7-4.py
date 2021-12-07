from typing import Any
from icecream import ic

class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f"{self.data}"


class LinkedList:
    
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def __iter__(self) -> Any:
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self) -> int:
        return self.length
    
    def __repr__(self) -> str:
        return " ".join([str(item) for item in self]) + " "

    def insert_nth(self, index: int, data: Any) -> None:
        if not 0 <= index <= len(self):
            return

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1

    def insert_tail(self, data: Any) -> None:
        self.insert_nth(len(self), data)
        
    def print_list(self) -> None:

        print(self)

    def delete_nth(self, index: int = 0) -> Any:
        if not 0 <= index <= len(self) - 1:
            return

        delete_node = self.head

        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            delete_node = temp.next
            temp.next = temp.next.next
        self.length -= 1
        return delete_node.data


tmp = input()

# init nums
nums = list(input().split(" "))

# linked list
link = LinkedList()

for x in nums:
    link.insert_tail(x)


# rounds
tmp = int(input())

for x in range(0, tmp):
    opt = input()

    # Add
    if opt[:1] == "0":
        sp = opt[2:].split(" ")
        k = int(sp[0])
        d = sp[1]
        link.insert_nth(k, d)
    # Remove
    else:
        k = int(opt[2:])
        link.delete_nth(k - 1)
    

link.print_list()
