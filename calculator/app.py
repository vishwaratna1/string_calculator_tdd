class StringCalculator:
    def add(self, numbers: str) -> int:
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

        result = sum(int(num) for num in numbers.split(","))
        return result