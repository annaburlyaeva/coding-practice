MAX_VOLUME = 1000000
MAX_WIDTH = 150
MAX_HEIGHT = 150
MAX_LENGTH = 150
MAX_MASS = 20


class Package:
    def __init__(self, width, height, length, mass):
        self.width = width
        self.height = height
        self.length = length
        self.mass = mass

    def is_bulky(self):
        volume = self.width * self.height * self.length
        return volume >= MAX_VOLUME \
               or self.width >= MAX_WIDTH \
               or self.height >= MAX_HEIGHT \
               or self.length >= MAX_LENGTH

    def is_heavy(self):
        return self.mass >= MAX_MASS

    def categorize(self):
        if self.is_bulky() and self.is_heavy():
            return "REJECTED"
        elif self.is_bulky() or self.is_heavy():
            return "SPECIAL"
        return "STANDARD"


def solve(width, height, length, mass):
    package = Package(width, height, length, mass)
    return package.categorize()


# Test cases
def run_tests():
    test_cases = [
        (160, 70, 70, 10, "SPECIAL"),
        (120, 100, 100, 10, "SPECIAL"),
        (90, 90, 118, 10, "STANDARD"),
        (120, 100, 50, 30, "SPECIAL"),
        (80, 110, 80, 70, "SPECIAL"),
        (70, 80, 90, 10, "STANDARD"),
        (100, 120, 60, 19, "STANDARD"),
        (150, 70, 70, 10, "SPECIAL"),
        (120, 100, 100, 10, "SPECIAL"),
        (90, 90, 118, 10, "STANDARD"),
        (120, 100, 110, 20, "REJECTED"),
        (80, 110, 80, 70, "SPECIAL"),
        (70, 80, 90, 10, "STANDARD"),
        (100, 150, 60, 30, "REJECTED")
    ]

    for width, height, length, mass, expected in test_cases:
        result = solve(width, height, length, mass)
        assert result == expected, \
            f"Failed for {width}x{height}x{length} with mass {mass}: " \
            f"expected {expected}, got {result}"

    print("All tests passed!")


# Run tests
run_tests()
