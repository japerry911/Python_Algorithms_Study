# O(n) time | O(space)
def isPalindrome(string) -> bool:
    l_ptr = 0
    r_ptr = len(string) - 1

    while l_ptr < r_ptr:
        if string[l_ptr] != string[r_ptr]:
            return False

        l_ptr += 1
        r_ptr -= 1

    return True
