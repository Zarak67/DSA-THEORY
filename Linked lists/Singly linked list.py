class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def find_middle(self):
        first = self.head
        last = self.head
        while last and last.next:
            first = first.next
            last = last.next.next
        return first.data if first else None

    def reverse(self):
        current = self.head
        prev = None
        while current:
            new_node = Node(current.data)
            new_node.next = prev
            prev = new_node
            current = current.next
        reversed_list = SinglyLinkedList()
        reversed_list.head = prev
        return reversed_list

    def remove_duplicates(self):
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next

    def merge_sorted(self, other):
        single = Node(0)
        tail = single
        p1, p2 = self.head, other.head
        while p1 and p2:
            if p1.data < p2.data:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next
        tail.next = p1 if p1 else p2
        merged_list = SinglyLinkedList()
        merged_list.head = single.next
        return merged_list

    def delete_list(self):
        self.head = None
        
        
        
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
print("Length of SLL:", sll.length())


print("Middle node of SLL:", sll.find_middle())


reversed_sll = sll.reverse()
print("Reversed SLL:", reversed_sll.display())


sorted_sll = SinglyLinkedList()
sorted_sll.append(1)
sorted_sll.append(2)
sorted_sll.append(2)
sorted_sll.append(3)
sorted_sll.remove_duplicates()
print("SLL after removing duplicates:", sorted_sll.display())


sll1 = SinglyLinkedList()
sll2 = SinglyLinkedList()
sll1.append(1)
sll1.append(3)
sll1.append(5)
sll2.append(2)
sll2.append(4)
sll2.append(6)
merged_sll = sll1.merge_sorted(sll2)
print("Merged SLL:", merged_sll.display())


sll.delete_list()
print("SLL after deletion:", sll.display())
