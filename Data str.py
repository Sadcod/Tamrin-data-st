#Tamrin 3 Data st
class Node:
    def __init__(self, coefficient=0, exponent=0):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, coefficient, exponent):
        new_node = Node(coefficient, exponent)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(f"{current.coefficient}x^{current.exponent}", end=" ")
            current = current.next
            if current:
                print("+", end=" ")
        print()

class Polynomial:
    def __init__(self):
        self.terms = LinkedList()

    def add_term(self, coefficient, exponent):
        self.terms.append(coefficient, exponent)

    def display(self):
        self.terms.display()

polynomial = Polynomial()
polynomial.add_term(4, 2)
polynomial.add_term(-1, 1)
polynomial.add_term(7, 0)

polynomial.display()
