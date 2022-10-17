import tokenize
import io
p = '''a
	b
		c
	e
f'''
text = tokenize.generate_tokens(io.StringIO(p).readline)
[print(tok) for tok in text]
