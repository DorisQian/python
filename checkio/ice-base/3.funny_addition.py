'''
We have an array of two positive integers. Add these two numbers together.

Input: A list of two elements. Each element is a positive integer.

Output: The sum of two numbers.

Example:

checkio([5, 5]) == 10
checkio([7, 1]) == 8
checkio([5, 5]) == 10
    
How it is used: Just for fun.

我们有两个正整数的数组。 将这两个数字加在一起。
'''


def checkio(data):
    """The sum of two integer elements"""
    return data[0] + data[1]
    
if __name__ == '__main__':
    assert checkio([5, 5]) == 10, 'First'
    assert checkio([7, 1]) == 8, 'Second'
    print('All ok')