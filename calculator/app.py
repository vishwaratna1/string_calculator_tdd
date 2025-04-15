class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        result = sum(int(num) for num in numbers.split(","))
        return result