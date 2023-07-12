# Strings
a_string = 'Hello World'
print(a_string.capitalize())
print(a_string.lower())
print(a_string.upper())
print(a_string.title())
print(a_string.casefold())
print(a_string.swapcase())

print(a_string.split())
print(a_string.rsplit())
a_multi_line_string = 'a string\nsplit across\nmultiple lines'
print(a_multi_line_string.splitlines())
a_string_with_lead_trail_space = '  Leading space with trails   '
print(a_string_with_lead_trail_space.strip())

print(a_string.find('ello'))
print(a_string.replace('World', 'Germany'))
print(a_string.startswith('He'))
print(a_string.endswith('Romania'))
print(a_string.endswith('ld'))
print(a_string.index('l'))
print(a_string.rindex('l'))

print(a_string.isalnum())
print(a_string.isalpha())
print(a_string.isdigit())
print(a_string.isidentifier())

print(a_string.replace(' ', '').isalpha())
print(a_string.replace(' ', '').isalnum())
print(a_string.replace(' ', '').isidentifier())

print(len(a_string))
print(a_string[5:])
print(a_string[:4])
print(a_string * 3)
print(' '.join(['words', 'a', 'line', 'each']))
