import os

def generate_html(directory):
    html = '<html>\n<head>\n<title>Index</title>\n</head>\n<body>\n<ul>\n'
    
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            html += f'<li><a href="{item}/index.html">{item}/</a></li>\n'
        else:
            html += f'<li><a href="{item}">{item}</a></li>\n'

    html += '</ul>\n</body>\n</html>'
    return html

def create_subdir_index(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            subdir_index = generate_html(item_path)
            with open(os.path.join(item_path, 'index.html'), 'w') as file:
                file.write(subdir_index)
                print(f'Created index.html in {item_path}')

if __name__ == '__main__':
    root_directory = '.'  # Replace '.' with the path to your root directory
    create_subdir_index(root_directory)

    print('Index files created successfully.')

