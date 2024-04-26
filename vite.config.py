from rjsmin import jsmin
import os

def minify_js(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
        minified_content = jsmin(content)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(minified_content)

# Example usage
input_js_file = 'path/to/your/input.js'
output_js_file = 'path/to/your/output.min.js'
minify_js(input_js_file, output_js_file)
