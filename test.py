import ast
from utils.code_extraction import process_file, extract_code_from_ipynb
from utils.description_generation import generate_description
from utils.html_generation import generate_html

# Use the functions from the imported modules to perform the overall task
file_path = 'examples/notebooks/deepdream.ipynb'  # replace with your actual file path
with open(file_path, 'r') as uploaded_file:
    file_content = uploaded_file.read()
if file_path.endswith('.ipynb'):
    code = extract_code_from_ipynb(file_content)
print(code)
