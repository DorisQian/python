'''
You are given some string where you need to find its middle characters. The string may contain one word, a few symbols or a whole sentence. If the length of the string is even, then you should return two middle characters, but if the length is odd, return just one. For more details look at the Example.

example

Input: A string.

Output: The middle characters.

Example:

middle('example') == 'm'
middle('test') == 'es'    
middle('very-very long sentence') == 'o'
middle('I') == 'I'
middle('no') == 'no'

How it is used: For work with texts.

Precondition:
1 <= the length of the text <= 100
'''

def middle(text):
    #replace this for solution
    return text

if __name__ == '__main__':
    print("Example:")
    print(middle('example'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert middle('example') == 'm'
    assert middle('test') == 'es'    
    assert middle('very-very long sentence') == 'o'
    assert middle('I') == 'I'
    assert middle('no') == 'no'
    print("Coding complete? Click 'Check' to earn cool rewards!")