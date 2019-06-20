import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_sibtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 8 == calculator.multiply(2, 4)

    def test_division(self):
        assert 2 == calculator.divide(10, 2)
