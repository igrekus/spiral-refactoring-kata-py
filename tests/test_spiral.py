from approvaltests.approvals import verify

from spiral.spiral import Spiral


def test_3():
    verify(Spiral(3).print())


def test_5():
    verify(Spiral(5).print())


def test_6():
    verify(Spiral(6).print())


def test_7():
    verify(Spiral(7).print())


def test_8():
    verify(Spiral(8).print())


def test_9():
    verify(Spiral(9).print())
