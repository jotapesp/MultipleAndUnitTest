import pytest
from multiplo import multiplo, ispositive

class TesteMultiplo:
    def setup(self):
        pass
# test function that checks if any number is positive
    def test_ispositive(self):
        result = ispositive(5)

        assert result

# to test the function that will say if a positive integer is a multiple of some
# other integer.
    def test_multiplo(self):
        result1 = multiplo(5, 10)
        result2 = multiplo(7, 14)

        assert result1
        assert result2
