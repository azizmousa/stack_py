from Stack import Stack


ss = Stack()

equation = input("Inter postfix equation form: ")
for word in equation.split(" "):
	if word.isdigit():
		ss.push(int(word))
	else:
		if word == "*":
			rhs = ss.get_top()
			ss.pop()
			lhs = ss.get_top()
			ss.pop()
			ss.push(lhs * rhs)
		elif word == "/":
			rus = ss.get_top()
			ss.pop()
			lhs = ss.get_top()
			ss.pop()
			ss.push(lhs / rhs)
		elif word == "+":
			rhs = ss.get_top()
			ss.pop()
			lhs = ss.get_top()
			ss.pop()
			ss.push(lhs + rhs)
		elif word == "-":
			rhs = ss.get_top()
			ss.pop()
			lhs = ss.get_top()
			ss.pop()
			ss.push(lhs - rhs)

print("the result = ", ss.get_top())