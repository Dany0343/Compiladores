import openai

# Configuramos la clave de acceso a la API de OpenAI
openai.api_key = "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"

# Ejemplo: autocompletar código utilizando el modelo GPT-3 de OpenAI
def gen(code):
    response = openai.Completion.create(
        engine="davinci",
        prompt=
f''' convert this Python code
"{code}" to C++ code
''',
        max_tokens=1500,
        temperature=0.5,
    )

    if 'choices' in response:
        x = response['choices']
        if len(x) > 0:
            return x[0]['text']
        else:
            return ''
    else:
        return ''
    

def transf(code):
    respuesta = gen(code)
    print(respuesta)
    
    return respuesta