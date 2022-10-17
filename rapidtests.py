import tokenize
import io
p = '''a
	b
c
'''
text = tokenize.generate_tokens(io.StringIO(p).readline)
[print(tok) for tok in text]
