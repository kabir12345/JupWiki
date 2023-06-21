import ast
import json

def extract_code_from_ipynb(ipynb_content):
    data = json.loads(ipynb_content)
    code_cells = [cell for cell in data['cells'] if cell['cell_type'] == 'code']
    python_code_cells = []
    for cell in code_cells:
        python_code_cell = [line for line in cell['source'] if not line.strip().startswith('!')]
        python_code_cells.append(python_code_cell)
    code = '\n'.join(['\n'.join(cell) for cell in python_code_cells])
    return code



def extract_code_elements(code):
    tree = ast.parse(code)
    functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    classes = [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    assignments = [node for node in ast.walk(tree) if isinstance(node, ast.Assign)]
    variables = [node.targets[0].id for node in assignments if isinstance(node.targets[0], ast.Name)]
    return functions, classes, variables

def process_file(file_path):
    with open(file_path, 'r') as uploaded_file:
        file_content = uploaded_file.read()
    if file_path.endswith('.ipynb'):
        code = extract_code_from_ipynb(file_content)
    else:
        code = file_content
    functions, classes, variables = extract_code_elements(code)
    function_dict = {function.name: function for function in functions}
    class_dict = {class_.name: class_ for class_ in classes}
    code_elements = {'functions': function_dict, 'classes': class_dict, 'variables': variables}
    return code_elements

