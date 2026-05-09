class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    

    #traversing thorugh a linked list
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")       


    #insert at beginning
    def insert_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    #insert at the end
    def insert_end(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node    


    #  Insert at Position
    def insert_at_position(self, data, pos):
        if pos == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        temp = self.head

        for _ in range(pos - 1):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node        


    # Delete from Beginning
    def delete_from_beginning(self):
        if self.head:
            self.head = self.head.next    