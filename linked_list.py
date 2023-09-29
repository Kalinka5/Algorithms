class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """

    data = None
    next_node = None

    def __init__(self, data) -> None:
        self.data = data

    def __repr__(self) -> str:
        return f"<Node data: {self.data}>"
    

class LinkedList:
    """
    Singly linked list
    """

    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Returns the number of nodes in the list.
        Takes O(n) time
        """

        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count
    
    def add(self, data):
        """
        Adds new Node containing data at head of the list.
        Takes O(1) time
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key.
        Returns the node or None if not found

        Takes O(n) time 
        """

        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        
        return None
    
    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position.
        Insertion take O(1) time but finding the node at the insertion point takes O(n) time.

        Takes overall O(N) time
        """

        if index == 0:
            self.add(data)
        elif index > 0:
            new_node = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1
            
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node 

    def remove(self, data):
        """
        Removes Node containing data from the linked list.
        Returns the Node or None if data doesn't exist.

        Takes O(n) time
        """

        current = self.head
        previous = None
        found = False

        while current and not found:
            if self.head.data == data:
                self.head = current.next_node
                found = True
            elif current.data == data:
                previous.next_node = current.next_node
                found = True
            else:
                previous = current
                current = current.next_node
        
        return current
    
    def node_at_index(self, index):
        if index == 0: 
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1
                
            return current
        

    def __repr__(self) -> str:
        """
        Returns a string representation of the linked list
        Takes O(n) time
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[HEAD {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[{current.data} TAIL]")
            else:
                nodes.append(f"[{current.data}]")

            current = current.next_node
        
        return " --> ".join(nodes)
    