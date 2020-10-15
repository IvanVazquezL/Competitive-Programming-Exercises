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
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

    def printList(self):
        node = self.head
        print(" ")
        while node:
            print(node.data)
            node = node.next

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

def insertNodeAtPosition(head, data, position):
    node = head
    if position==0:
        pastHead = head
        newHead = SinglyLinkedListNode(data)
        newHead.next = pastHead
    else:
        for i in range(position-1):
            node = node.next
        pastNode = node
        nextNode = node.next
        newNode = SinglyLinkedListNode(data)
        pastNode.next = newNode
        newNode.next = nextNode


    return head



if __name__ == '__main__':


    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    llist_head.printList()
