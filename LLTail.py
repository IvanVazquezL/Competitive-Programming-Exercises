#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None


def insertNodeAtTail(head, data):
    #To prevent maximum recursion depth exceeded error
    sys.setrecursionlimit(1000000)
    #If the node is None
    if head == None:
        #return the created node for that data
        return SinglyLinkedListNode(data)
    else:
        #If the next value of the node is None
        if head.next == None:
            #create a node for data in the next node
            head.next = SinglyLinkedListNode(data)
        else:
            #Recursion sending the next node of the current node
            # and the data
            insertNodeAtTail(head.next,data)
        return head



if __name__ == '__main__':

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    node = llist.head
    print(node.data)
    while node:
        print(node.data)
        node = node.next
