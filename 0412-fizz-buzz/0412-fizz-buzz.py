class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        i = 1
        for i in range(1, n + 1):
            fizz = ""
            if i % 3 == 0:
                fizz += "Fizz"
            if i % 5 == 0:
                fizz += "Buzz"
            if (i % 3 != 0 and i % 5 != 0):
                fizz = str(i)
            answer.append(fizz)
        return answer