import os
import openai
import configparser
import sys
import contextlib
import random

USE_STREAM_FEATURE = True
SET_TEMPERATURE_NOISE = False
MAX_TOKENS_DEFAULT = 1000

STREAM = True
API_KEYS_LOCATION = "./config"
PYTHON_FILE_TO_CONVERT = "ProyectoFinal.txt"

  
def create_template_ini_file():
    if not os.path.isfile(API_KEYS_LOCATION):
        with open(API_KEYS_LOCATION, 'w') as f:
            f.write('[openai]\n')
            f.write('organization_id=\n')
            f.write('secret_key=\n')
    
        sys.exit(1)


def initialize_openai_api():
    create_template_ini_file()
    config = configparser.ConfigParser()
    config.read(API_KEYS_LOCATION)

    openai.organization_id = config['openai']['organization_id'].strip('"').strip("'")
    openai.api_key = config['openai']['secret_key'].strip('"').strip("'")


def create_input_prompt(length=3000):
    inputPrompt = ''
    filename = PYTHON_FILE_TO_CONVERT
    with open(filename) as f:
        inputPrompt += f.read() + '\n'

    inputPrompt = inputPrompt[:length]
    inputPrompt += '\n\nConvert this Python Code to' + 'C++' + '\n'
    return inputPrompt


def generate_completion(input_prompt, num_tokens):
    temperature = 0.0
    if SET_TEMPERATURE_NOISE:
        temperature += 0.1 * round(random.uniform(-1, 1), 1)
    response = openai.Completion.create(engine='code-davinci-002', prompt=input_prompt, temperature=temperature,
                                        max_tokens=num_tokens, stream=STREAM, stop='===================\n',
                                        top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0)
    return response


def get_generated_response(response):
    generatedFile = "// -Codigo:-\n"
    while True:
        nextResponse = next(response)
        completion = nextResponse['choices'][0]['text']
        generatedFile = generatedFile + completion
        if nextResponse['choices'][0]['finish_reason'] is not None:
            break
    return generatedFile


def write_cpp_file(textResponse):
    fileName = PYTHON_FILE_TO_CONVERT.split(".")[0] + ".cpp"
    if os.path.exists(fileName):
        os.remove(fileName)
    f = open(fileName, "a")
    f.write(textResponse)
    f.close()


def test_cpp_compilation(cppFile):
    exeFile = cppFile.split(".")[0] + ".exe"
    if os.system("gcc " + cppFile + " -o " + exeFile + " &> /dev/null") == 0:
        return True
    else:
        return False


def iterate_for_compilable_solution(prompt, maxIterations):
    for it in range(maxIterations):
        response = generate_completion(prompt, num_tokens=MAX_TOKENS_DEFAULT)
        textResponse = get_generated_response(response)
        write_cpp_file(textResponse)
        fileName = PYTHON_FILE_TO_CONVERT.split(".")[0]
        with contextlib.redirect_stdout(None):
            isSolutionCompilable = test_cpp_compilation(fileName + ".cpp")
        if isSolutionCompilable:
            #print("Found a compilable solution after {} iterations".format(it+1))
            #print("C++ File: {}".format(fileName + ".cpp"))
            #print("Compiled Executable: {}".format(fileName + ".exe"))
            break
        if it == maxIterations - 1:
            print("")


def run():
    initialize_openai_api()
    prompt = create_input_prompt()
    iterate_for_compilable_solution(prompt=prompt, maxIterations=1)