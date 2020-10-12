class Node:
    #Node constructor
    def __init__(self, dataval=None):
        #Give the new instance the passed value
        self.dataval = dataval
        #The next node of the node is none
        self.nextval = None

class SingleLinkedList:
    #Single Linked List constructor
    def __init__(self):
        #The node head value is none
        self.headval = None

    #Print LinkedList
    def listprint(self):
        #Get the the node head
        printval = self.headval
        while printval is not None:
            #Print the value of the node
            print (printval.dataval)
            #Printval is now the next node
            printval = printval.nextval

    #Insert a new node at the beginning
    def AtBeginning(self,newdata):
        #Create a new node with the passed data as its value
        NewNode = Node(newdata)
        # The next node is going to be the current node head
        NewNode.nextval = self.headval
        #The new node is going to be the new node head
        self.headval = NewNode

    # Insert a newnode at the end
    def AtEnd(self, newdata):
        #Create a new node with the passed data as its value
        NewNode = Node(newdata)
        #If the linked list is empty
        if self.headval is None:
            #Then the new node is the new head
            self.headval = NewNode
            return
        #Get the node head
        laste = self.headval
        #While the next node is not empty
        while(laste.nextval):
            #Get next node
            laste = laste.nextval
        #The next value of the last node is the new node
        laste.nextval=NewNode

    # Function to add a node between two nodes
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        #Create a new node with the passed data as its value
        NewNode = Node(newdata)
        #The next value of the new node is the next value of the sent node
        NewNode.nextval = middle_node.nextval
        #the next value of the sent node is the new node
        middle_node.nextval = NewNode

    # Function to remove node
    def RemoveNode(self, Removekey):
        #Get the node head
        HeadVal = self.headval

        if (HeadVal is not None):
            #If the node head has the same value as the one to remove
            if (HeadVal.dataval == Removekey):
                #The new head is the next node of the node head
                self.headval = HeadVal.nextval
                #The past node head is now none
                HeadVal = None
                return

        #Loop through the linked list
        #While the node is not none
        while (HeadVal is not None):
            #If the node has the same value as the one to remove
            if HeadVal.dataval == Removekey:
                #End the while
                break
            #prev is the current node in the loop
            prev = HeadVal
            #HeadVal is now the next node
            HeadVal = HeadVal.nextval

        #If the value was not found
        if (HeadVal == None):
            return

        #the next node of the previous node that is going to be Removed
        #Is going to be now the next node of the node that is going to be removed
        prev.nextval = HeadVal.nextval

        #the removed node is now none
        HeadVal = None


list = SingleLinkedList()
