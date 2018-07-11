'''
Your friends and you have decided to feel like a true hackers and create a special "hackers language" for correspondence in the net. The original messages will be in English and than will be encrypted with these rules:
- all letters and white spaces will be converted into their ASCII codes and than into the binary numbers. Except white spaces - their binary form should be '1000000' not '100000'.
- numbers, dates (in the 'dd.mm.yyyy' format), time (in the 'hh:mm' format) and special signs ('.', ':', '!', '?', '@', '$', '%') won't be converted. 
For the realisation of this system you should create the HackerLanguage class with some methods:

write(text) - add new (text) to the current text message.
delete(N) - delete from the current text message the last N symbols.
send() - returns the encrypted message which will be send.
read(text) - get the encrypted (text) as the argument and returns the normal readable English text.

In this mission you could use the Interpreter design pattern.

Examples:

message_1 = HackerLanguage()
message_1.write('Remember: 21.07.2018 at 11:11AM')
message_1.delete(2)
message_1.write('PM')
message_1.send() == '10100101100101110110111001011101101110001011001011110010:100000021.07.2018100000011000011110100100000011:1110100001001101'

message_2 = HackerLanguage()
message_2.read('10011011111001100000011001011101101110000111010011101100100000011010011110011100000011011011110010.11100101101111110001011011111110100@11001111101101110000111010011101100.110001111011111101101') ==
'My email is mr.robot@gmail.com'

Input: plain or encrypted text.

Output: encrypted or decrypted text of the message.

How it is used: For the encryption and decryption of the important information.

Precondition: Only [a-z], [A-Z], [0-9], ".", ":", "!", "?", "$", "%", "@" in the text.
'''

class HackerLanguage:
	secret = str()
	def write(self, text):
		self.current = text
		self.secret += ''.join([bin(ord(s))[2:] if s.isalpha() else s for s in text])

	def delete(self, number):
		word = self.current[-number:]
		length = len(''.join([bin(ord(s))[2:] if s.isalpha() else s for s in word]))
		self.secret = self.secret[:len(self.secret)-length]

	def send(self):
		#print(self.secret)
		return self.secret

	def read(self, message):
		word = str()
		while message:
			if len(message) < 7:
				return message
			else:
				current = message[:7]
				if current.isdigit(): 
					word += chr(int(current, 2))
					message = message[7:]
				#else: 
		print(word)
		return word




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    message_1 = HackerLanguage()
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")
    message_2 = HackerLanguage()
    message = HackerLanguage()

    assert message_1.send() == "111001111001011100011111001011001011110100"
    assert message_2.read("11001011101101110000111010011101100") == "email"
    assert message.read('1001101111100110000001100101110110111000011101001110110010000001101\
    	0011110011100000011011011110010.11100101101111110001011011111110100@1100111110110111000011101\
    	0011101100.110001111011111101101') == "My email is mr.robot@gmail.com"
    print("Coding complete? Let's try tests!")