country_capitals = {key: value for (key, value) in zip(input().split(', '), input().split(', '))}
for (key, value) in country_capitals.items():
    print(f'{key} -> {value}')
