class StringCalculator:

    def __init__(self):
        self.call_count = 0
        
    def add(self, numbers: str) -> int:
        self.call_count += 1

        if not numbers:
            return 0
        
        delimiters = [",", "\n"]
        if numbers.startswith("//"):
            last_delimiter_index = numbers.find("\n")
            custom_delimiter = numbers[2:last_delimiter_index]
            delimiters.append(custom_delimiter)
            numbers = numbers[last_delimiter_index+1: ]

        for delimiter in delimiters:
            numbers = numbers.replace(delimiter, ",")

        numbers = [int(num) for num in numbers.split(",")]
        negative_numbers = [num for num in numbers if num < 0]

        if negative_numbers:
            raise NegativeNumberException(negatives=negative_numbers)

        result = sum(num for num in numbers if num <= 1000)
        return result
    
    def get_called_count(self) -> int:
        return self.call_count
    
class NegativeNumberException(Exception):
    def __init__(self, negatives):
        message = f"negative numbers not allowed: {', '.join(map(str, negatives))}"
        super().__init__(message)
