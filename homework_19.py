from stack import Stack
# Convert a decimal number to binary
def div_by_two(dec_num):
	s = Stack()
	bin_num = ''
	while dec_num > 0:
		remainder = dec_num % 2
		dec_num = dec_num // 2
		s.push(remainder)
	while not s.is_empty():
		bin_num += str(s.pop())
	return bin_num
print(div_by_two(1)) # 1
print(div_by_two(4)) # 100
print(div_by_two(8)) # 1000
print(div_by_two(12)) # 1100
print(div_by_two(256), '\n') # 100000000


# Reverse a string
def rev_string(input_str):
	s = Stack()
	index = 0
	while index in range(len(input_str)):
		s.push(input_str[index])
		index += 1
	rev_str = ''
	while not s.is_empty():
		rev_str += s.pop()
	return rev_str
print(rev_string('retupmoC')) # Computer
print(rev_string('goD')) # Dog
print(rev_string('eman')) # name
print(rev_string('LLABESAB')) # BASEBALL
print(rev_string('esreveR'), '\n') # Reverse


# Checking the balance of parenthesis
def is_match(p1, p2):
        if p1 == '(' and p2 == ')':
                return True
        elif p1 == '[' and p2 == ']':
                return True
        elif p1 == '{' and p2 == '}':
                return True
        else:
                return False
def is_paren_balanced(paren_string):
        index = 0
        is_balanced = True
        s = Stack()
        if paren_string == '':
                is_balanced = False
                return False
        elif paren_string[-1] in '([{':
                is_balanced = False
                return False
        while index < len(paren_string) and is_balanced == True:
                if paren_string[index] in '([{':
                        s.push(paren_string[index])
                else:
                        if s.is_empty():
                                is_balanced = False
                                return False
                        elif is_match(s.pop(), paren_string[index]):
                                is_balanced = True
                        else:
                                is_balanced = False
                                return False
                index += 1
        if s.is_empty() and is_balanced == True:
                return True
print(is_paren_balanced('[]')) # True
print(is_paren_balanced('([{}])')) # True
print(is_paren_balanced('(([)')) # False
print(is_paren_balanced('())')) # False
print(is_paren_balanced('))')) # False
print(is_paren_balanced('((')) # False
print(is_paren_balanced('{{')) # False
print(is_paren_balanced('[[[[')) # False
print(is_paren_balanced('({{{[[[')) # False
print(is_paren_balanced('')) # False

