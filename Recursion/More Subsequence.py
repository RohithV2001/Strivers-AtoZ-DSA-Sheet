'''Very Important :

No of subsequences for a  string of length n is 2^n , so for each time we traverse through a new character we multiply the count by 2.if it is already present then we decrement the existence of the repeated character by its character count.

Three aproaches are used :
1. 
'''
def func(s: str, n: int) -> int:
    # Initializing 'count' with 1.
    count = 1

    # Creating a dictionary 'm1' to store character counts.
    m1 = {}

    # Calculating the number of distinct subsequences.
    for i in range(n):
        if s[i] not in m1:
            m1[s[i]] = count
            count *= 2
        else:
            temp = m1[s[i]]
            m1[s[i]] = count
            count *= 2
            count -= temp

    return count

def moreSubsequence(n: int, m: int, a: str, b: str) -> str:
    if func(a, n) >= func(b, m):
        return a
    else:
        return b


'''2. Same approach but using extra space by using DP'''

def count_distinct_subsequences(s):
    n = len(s)
    mod = 10**9 + 7
    last_occurrence = [-1] * 26
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        dp[i] = (2 * dp[i - 1]) % mod
        if last_occurrence[ord(s[i - 1]) - ord('a')] != -1:
            dp[i] = (dp[i] - dp[last_occurrence[ord(s[i - 1]) - ord('a')]]) % mod
        last_occurrence[ord(s[i - 1]) - ord('a')] = i - 1

    return dp[n]


def find_string_with_more_subsequences(A, B):
    count_A = count_distinct_subsequences(A)
    count_B = count_distinct_subsequences(B)

    if count_A >= count_B:
        return A
    else:
        return B


# Example usage:
N = 2
M = 2
A = 'ab'
B = 'dd'

result = find_string_with_more_subsequences(A, B)
print(result)

'''
3.Recursive Implementation of above approach
'''

def count_distinct_subsequences_recursive(s, n, last_occurrence, mod):
    if n == 0:
        return 1

    count = (2 * count_distinct_subsequences_recursive(s, n - 1, last_occurrence, mod)) % mod

    if last_occurrence[ord(s[n - 1]) - ord('a')] != -1:
        count = (count - count_distinct_subsequences_recursive(s, last_occurrence[ord(s[n - 1]) - ord('a')], last_occurrence, mod)) % mod

    last_occurrence[ord(s[n - 1]) - ord('a')] = n - 1

    return count


def find_string_with_more_subsequences(A, B):
    mod = 10**9 + 7
    last_occurrence = [-1] * 26
    count_A = count_distinct_subsequences_recursive(A, len(A), last_occurrence, mod)
    last_occurrence = [-1] * 26  # Reset last_occurrence array
    count_B = count_distinct_subsequences_recursive(B, len(B), last_occurrence, mod)

    if count_A >= count_B:
        return A
    else:
        return B


# Example usage:
N = 2
M = 2
A = 'ab'
B = 'dd'

result = find_string_with_more_subsequences(A, B)
print(result)

