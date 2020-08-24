import json
import math
import string
import re
import random
import sys
import traceback
import functools
from collections import OrderedDict
import numpy
import pandas

# silence pyflakes
assert json
assert math
assert string
assert re
assert random
assert sys
assert traceback
assert functools
assert OrderedDict
assert numpy
assert pandas


class ListNode(object):
    _slots_ = ('value', 'next')

    def __init__(self, x):
        self.value = x
        self.next = None


class Tree(object):
    _slots_ = ('value', 'left', 'right')

    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

# K is the index of the node from the end of what we need to remove
# If k is higher than the length of the list, do nothing


def remove_kth_from_end(head, k):
    # Handle if the k is 0
    count = 0
    curr = head
    
    while (curr.next):
        curr = curr.next
        count += 1
        
    # include None at end of list
    count += 1
    
    if k > count:
        return head
    if k == 0:
        return head

    location = count - k
    
    if location == 0:
        return head.next

    prev = head
    curr = head
    new_count = 1
    # Finding the target value in the linked list (kth value)
    while (curr.next and new_count <= location):
        prev = curr
        curr = curr.next
        new_count += 1
        
    # Over riding what target is
    prev.next = curr.next
    return head

            