import base64

def encode(string):
	return str(base64.b64encode(bytes(string, 'utf-8')), 'utf-8')

def decode(string):
	print('-------------------------------')
	print(str(base64.b64decode(bytes(str.encode(string))), 'utf-8'))
	print('-------------------------------')
	return str(base64.b64decode(bytes(str.encode(string))), 'utf-8')


if __name__ == '__main__':
	string = 'привет'
	print(encode(string))

	a = input()
	print(decode(a))