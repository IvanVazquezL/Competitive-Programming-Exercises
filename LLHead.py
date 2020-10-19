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

def insertNodeAtHead(llist, data):
    if llist == None:
        return SinglyLinkedListNode(data)
    else:
        temp = SinglyLinkedListNode(data)
        temp.next = llist
        head = temp

        return head

if __name__ == '__main__':

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head

    head = llist.head
    while head:
        print(head.data)
        head = head.next
