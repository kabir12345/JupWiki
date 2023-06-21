import ast
from utils.code_extraction import process_file, extract_code_from_ipynb
from utils.description_generation import generate_description
from utils.html_generation import generate_html

#Use the functions from the imported modules to perform the overall task
file_path = 'examples/notebooks/GAN.ipynb'  
code_elements = process_file(file_path)

# Extract the code from the Jupyter notebook
with open(file_path, 'r') as uploaded_file:
    file_content = uploaded_file.read()
code = extract_code_from_ipynb(file_content)

functions = code_elements['functions']
classes = code_elements['classes']
variables = code_elements['variables']

function_info = [{'name': name, 'args': [arg.arg for arg in function.args.args], 'description': generate_description(function, 'function', code, code_elements, args=[arg.arg for arg in function.args.args])} for name, function in functions.items()]
class_info = [{'name': name, 'bases': [base.id for base in class_.bases if isinstance(base, ast.Name)], 'description': generate_description(class_, 'class', code, code_elements, bases=[base.id for base in class_.bases if isinstance(base, ast.Name)])} for name, class_ in classes.items()]
variable_info = [{'name': variable, 'description': generate_description(variable, 'variable', code, code_elements)} for variable in variables]
code_elements = {'functions': function_info, 'classes': class_info, 'variables': variable_info}

html = generate_html(code_elements)

out_loc='examples/wikis/'
with open(out_loc + 'GAN.html', 'w') as f:
    f.write(html)
x