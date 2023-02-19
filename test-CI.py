
import pytest
msg="hello world"
print(msg)
print(msg)
print(msg)
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"


if __name__ == "__main__":
    test_sum()
    print("Everything passed")

def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'