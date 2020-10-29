import re

example = '''
8+9
483967027
10-15
'''
pattern = re.compile(r'(\d+)([\+|\-|\*|\/])(\d+)')
matches = pattern.finditer(example)

for match in matches:
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))

