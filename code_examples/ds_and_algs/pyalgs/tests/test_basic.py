import pytest
import basic as bc

def test_peek():
    stack = bc.StackArr([3])
    assert stack.peek() == 3
    
def test_pop():
    stack = bc.StackArr([3])
    assert stack.pop() == 3

def test_is_empty():
    stack = bc.StackArr([3])
    assert stack.is_empty() == False
    
def test_size():
    stack = bc.StackArr([3])
    assert stack.size() == 1
 

    
    

