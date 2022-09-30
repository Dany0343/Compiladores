import tokenize
import io
t = ''''
x +             y
a
  b
  c
    d
      e
      f
  g
    h
  i
'''
text = tokenize.generate_tokens(io.StringIO(t).readline)
[print(tok) for tok in text]