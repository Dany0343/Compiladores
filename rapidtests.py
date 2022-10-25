import tokenize
import io
p = '''\
a
    b
a
x
'''
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