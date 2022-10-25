import tokenize
import io
<<<<<<< HEAD
p = '''\
for i in range(1,10):
	print(i)

def ola():
	pass
ola
'''
=======
p = '''a
	e
f

e'''
>>>>>>> cba4b6634d14142f000dad60a0b4c03496e52a07
text = tokenize.generate_tokens(io.StringIO(p).readline)
[print(tok) for tok in text]

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