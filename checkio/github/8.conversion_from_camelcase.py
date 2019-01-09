'''
Your mission is to convert the name of a function (a string) from CamelCase ("MyFunctionName") into the 
Python format ("my_function_name") where all chars are in lowercase and all words are concatenated with 
an intervening underscore symbol "_".
您的任务是将函数（字符串）的名称从CamelCase（“MyFunctionName”）转换为Python格式（“my_function_name”），
其中所有字符都是小写的，并且所有单词都与插入的下划线符号“_”连接在一起。

Input: A function name as a CamelCase string.

Output: The same string, but in under_score.

Example:

from_camel_case("MyFunctionName") == "my_function_name"
from_camel_case("IPhone") == "i_phone"
from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
from_camel_case("Name") == "name"

How it is used: To apply function names in the style in which they are adopted in a specific language 
(Python, JavaScript, etc.).

Precondition:
0 < len(string) <= 100
Input data won't contain any numbers.

'''

def from_camel_case(name):
	function = []
	word = ''
	for s in name:
		if s.isupper():
			if word != '':
				function.append(word)
				word = s.lower()
			else:
				word = s.lower()
		else:
			word += s
	function.append(word)
	return '_'.join(function)

if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
