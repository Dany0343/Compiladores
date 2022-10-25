import tokenize
import io
p = '''\
a
	b
x
	y
	owo


'''
text = tokenize.generate_tokens(io.StringIO(p).readline)
[print(tok) for tok in text]

for i in range(1,5):
	print("xd")
	

'''
a
	e
	e
	e	d
		e
			f
				g
					h
					i
						j
					k
				l
			m
		n
		o
	o
sup
'''