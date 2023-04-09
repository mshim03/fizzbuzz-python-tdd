class FizzBuzz:
    def convert(self, input: int) -> str:
        if input % 15 == 0:
            return "FizzBuzz"
        if input % 3 == 0:
            return "Fizz"
        elif input % 5 == 0:
            return "Buzz"
        return str(input)

    def print_fizzbuzz(self, input: int):
        print(self.convert(input))

    def print_fizzbuzz_range(self, input: int):
        for i in range(1, input+1):
            self.print_fizzbuzz(i)