from main import fizzBuzz
import pytest

def test_fizzbuzz():
    assert fizzBuzz(3) == "Fizz"
    assert fizzBuzz(5) == "Buzz"
    assert fizzBuzz(15) == "FizzBuzz"
    assert fizzBuzz(4) == 4

   
    



 
# Path: test_main.py
# Compare this snippet from main.py:
# def fizzBuzz(numb):
