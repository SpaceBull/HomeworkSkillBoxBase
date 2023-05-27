from typing import List

if __name__ == "__main__":
    letters: List[str] = ['a', 'b', 'c', 'd', 'e']
    numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    result = list(map(lambda x, y: tuple(x + str(y)), letters, numbers))
    print(result)
