from collections import deque

if __name__ == '__main__':
    def can_be_poly(word: str) -> bool:
        new_word = deque(word)
        new_word.reverse()
        if ''.join(new_word) == word:
            return True
        return False


    print(can_be_poly('abcba'))
    print(can_be_poly('abbbc'))