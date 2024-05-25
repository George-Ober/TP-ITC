
def triangle(n):
	for i in range(n + 1):
		a = ""
		for k in range(i):
			a += "*"	
		print(a)


def triangle_ch(n):
	a = "'"
	for i in range(n + 1):
		for k in range(i):
			a += "*"	
		a += "\\n"
	print(a + "'")
