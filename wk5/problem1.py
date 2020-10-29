import re

example = '''
123 Main Street
935 marietta street
606W 57th street
'''
pattern = re.compile(r'\d+\s\w+\s\w+')
matches = pattern.finditer(example)

for match in matches:
    print(match)
