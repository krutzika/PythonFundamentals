class Node:
    
    def __init__(self, data):
        self.data = data 
        self.next = None
        
        
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def insertion_at_beginning(self, data):
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
            
    def insertion_at_end(self, data):
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
        
        current_node = self.head 
        
        while(current_node.next):
            current_node = current_node.next
        
        current_node.next = new_node
        
    def insertion_at_index(self, data, index):
        new_node = Node(data)
        
        if(index==0):
            self.insertion_at_beginning(data)
            return
            
        position = 0 
        current_node = self.head
        
        while (current_node!=None and position+1!= index):
            position+=1
            current_node = current_node.next
        
        if current_node!=None:
            new_node.next = current_node.next
            current_node.next = new_node
            
    def update_node(self, data, index):
        position = 0 
        current_node=self.head
        
        if index==0:
            current_node.data = data 
            return
        
        while (current_node!=None and position+1!=index):
            position+=1
            current_node = current_node.next
        
        if current_node!=None:
            current_node.data = data 
        else:
            print("The index is wrong")
            
    def delete_node_at_begining(self):
        if (self.head == None):
            return 
        self.head = self.head.next
    
    def delete_node_at_end(self):
        
        if self.head is None:
            return
        
        current_node = self.head 
        
        while (current_node.next!= None and current_node.next.next!=None):
            current_node = current_node.next
        
        current_node.next = None
            
    def delete_node_index(self, index):
       
        if self.head is None:
            return 
        
        current_node = self.head
        position = 0 
        
        if index == 0 :
            self.delete_node_at_begining()
            return
        
        while(current_node!=None and position< index-1):
            position+=1
            current_node = current_node.next
            
        if current_node!= None and current_node.next!=None:
            current_node.next=current_node.next.next
        else:
            print("Enter the current index")
            
        return
    
    def delete_node_by_value(self, data):
        
        if self.head is None:
            return
        
        current_node = self.head 
        
        if current_node.data==data:
            self.delete_node_at_begining()
            return
            
        while (current_node != None and current_node.next.data!=data):
            current_node=current_node.next
            
        if current_node!=None:
            current_node.next = current_node.next.next
            
        return 
    
    def print_linked_list(self):
        current_node = self.head 
        while(current_node.next):
            print(current_node.data)
            current_node = current_node.next
        
    def print_size_linked_list(self):
        
        if self.head is None:
            return 0
        
        current_node = self.head
        length = 0
        while(current_node.next):
            length+=1
            current_node=current_node.next
        return length
            
            
                                     
def main(): 

    llist = LinkedList()
    llist.insertion_at_end('a')
    llist.insertion_at_end('b')
    llist.insertion_at_beginning('c')
    llist.insertion_at_end('d')
    llist.insertion_at_index('g', 2)

    print("Node Data:")
    llist.print_linked_list()

    print("\nRemove First Node:")
    llist.delete_node_at_begining()
    llist.print_linked_list()

    print("\nRemove Last Node:")
    llist.delete_node_at_end()
    llist.print_linked_list()

    print("\nRemove Node at Index 1:")
    llist.delete_node_index(1)
    llist.print_linked_list()

    
    print("\nLinked list after removing a node:")
    llist.print_linked_list()

    print("\nUpdate node Value at Index 0:")
    llist.update_node('z', 0)
    llist.print_linked_list()

    print("\nSize of linked list:", llist.print_size_linked_list())
        
if __name__ == "__main__":
    main()
        
    
