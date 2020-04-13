import pytest


def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        return True

@pytest.mark.parametrize(
    "num,expect",
    [(1,False),
     (13,True),
     (4,False)
    ],
    ids=["case1","case2","case3"]
)
def test_is_prime(num,expect):
    assert is_prime(num)==expect
# class Test_prime:
#     @pytest.mark.smoke
#     def test_true(self):
#         assert is_prime(13)
#     def test_false(self):
#         assert is_prime(4)is False
#     def test_special_num(self):
#         assert is_prime(1)is False