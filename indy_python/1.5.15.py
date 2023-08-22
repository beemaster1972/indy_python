a, b, c = [input() for _ in range(3)]
solutions = [f'{a}*{b}*{c}', f'{a}+{b}*{c}', f'{a}+{b}+{c}', f'{a}*{b}+{c}', f'({a}+{b})*{c}', f'{a}*({b}+{c})']
values = [eval(x) for x in solutions]
print(max(values))