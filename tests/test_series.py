from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_fibonacci0():
    assert fibonacci(0) == 0

def test_fibonacci1():
    assert fibonacci(1) == 1

def test_fibonacci2():
    assert fibonacci(2) == 1

def test_fibonacci3():
    assert fibonacci(3) == 2

def test_fibonacci4():
    assert fibonacci(4) == 3

def test_fibonacci5():
    assert fibonacci(5) == 5

def test_fibonacci6():
    assert fibonacci(6) == 8

def test_fibonacci7():
    assert fibonacci(7) == 13

def test_fibonacci8():
    assert fibonacci(8) == 21

def test_fibonacci9():
    assert fibonacci(9) == 34

def test_fibonacci10():
    assert fibonacci(10) == 55

def test_lucas0():
    assert lucas(0) == 2

def test_lucas1():
    assert lucas(1) == 1

def test_lucas2():
    assert lucas(2) == 3

def test_lucas3():
    assert lucas(3) == 4

def test_lucas4():
    assert lucas(4) == 7

def test_lucas5():
    assert lucas(5) == 11

def test_lucas6():
    assert lucas(6) == 18

def test_lucas7():
    assert lucas(7) == 29

def test_lucas8():
    assert lucas(8) == 47

def test_lucas9():
    assert lucas(9) == 76

def test_lucas10():
    assert lucas(10) == 123



def test_sum_series_Fibonacci0():
    assert sum_series(0) == 0

def test_sum_series_Fibonacci1():
    assert sum_series(1) == 1

def test_sum_series_Fibonacci2():
    assert sum_series(2) == 1

def test_sum_series_Fibonacci3():
    assert sum_series(3) == 2

def test_sum_series_Fibonacci4():
    assert sum_series(4) == 3



def test_sum_series_Lucas0():
    assert sum_series(0,2,1) == 2

def test_sum_series_Lucas1():
    assert sum_series(1,2,1) == 1

def test_sum_series_Lucas2():
    assert sum_series(2,2,1) == 3

def test_sum_series_Lucas3():
    assert sum_series(3,2,1) == 4

def test_sum_series_Lucas4():
    assert sum_series(4,2,1) == 7



def test_sum_series_Other0():
    assert sum_series(0,2,3) == 2

def test_sum_series_Other1():
    assert sum_series(1,2,3) == 3

def test_sum_series_Other2():
    assert sum_series(2,2,3) == 5

def test_sum_series_Other3():
    assert sum_series(3,2,3) == 8

def test_sum_series_Other4():
    assert sum_series(4,2,3) == 13


def test_sum_series_Other4():
    assert sum_series(0,5,7) == 5

def test_sum_series_Other5():
    assert sum_series(1,5,7) == 7

def test_sum_series_Other6():
    assert sum_series(2,5,7) == 12

def test_sum_series_Other7():
    assert sum_series(3,5,7) == 19

def test_sum_series_Other8():
    assert sum_series(4,5,7) == 31