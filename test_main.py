import main
import pytest


@pytest.mark.skip()
@pytest.mark.xfail()
@pytest.mark.parametrize("num,output", [(153, True), (370, True), (341, True), (543, False)])
def test_CheckArmstrong(num, output):
    result = main.CheckArmstrong(num)
    assert result == output


@pytest.mark.xfail()
@pytest.mark.parametrize("num,output", [(16, True), (32, True), (341, True), (543, False)])
def test_CheckDivisibleby8(num, output):
    result = main.CheckDivisibleby8(num)
    assert result == output


# @pytest.mark.xfail()
@pytest.mark.parametrize("a,b,c,d", [(2, 3, 4, 2), (54, 76, 32, 32), (4, 8, 1, 4), (3, 1, 5, 1)])
def test_SmallestAmong3(a, b, c, d):
    result = main.SmallestAmong3(a, b, c)
    assert result == d


# @pytest.mark.xfail()
@pytest.mark.parametrize("num,output", [(2, "Even"), (3, "Odd"), (35, "Even"), (53, "Odd")])
def test_CheckEvenOdd(num, output):
    result = main.EvenOdd(num)
    assert result == output


# @pytest.mark.xfail()
@pytest.mark.parametrize("string,output", [("nayan", True), ("eye", True), ("tapan", True), ("sandy", False)])
def test_isPalindrome(string, output):
    result = main.isPalindrome(string)
    assert result == output
