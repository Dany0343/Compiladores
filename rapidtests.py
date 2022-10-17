import tokenize
import io
p = '''a
	e
f'''
text = tokenize.generate_tokens(io.StringIO(p).readline)
[print(tok) for tok in text]
