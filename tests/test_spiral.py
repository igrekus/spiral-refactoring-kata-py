from approvaltests.approvals import verify

from spiral.spiral import Spiral


def test_3():
    verify(str(Spiral(3)))


def test_5():
    verify(str(Spiral(5)))


def test_6():
    verify(str(Spiral(6)))


def test_7():
    verify(str(Spiral(7)))


def test_8():
    verify(str(Spiral(8)))


def test_9():
    verify(str(Spiral(9)))


def test_10():
    verify(str(Spiral(10)))


def test_11():
    verify(str(Spiral(11)))


def test_15():
    verify(str(Spiral(15)))
