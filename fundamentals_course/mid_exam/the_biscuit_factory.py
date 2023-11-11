daily_production = int(input())
worker_number = int(input())
competitor_production = int(input())
working_days = 30
low_efficient_days = working_days // 3
low_efficient_prod = int(low_efficient_days * daily_production * worker_number * 0.75)
total_production = ((working_days - low_efficient_days) * daily_production * worker_number) + low_efficient_prod
competitor_diff = abs(competitor_production - total_production)
competitor_diff_percentage = (competitor_diff / competitor_production) * 100
print(f'You have produced {total_production} biscuits for the past month.')
if total_production > competitor_production:
    print(f'You produce {competitor_diff_percentage:.2f} percent more biscuits.')
else:
    print(f'You produce {competitor_diff_percentage:.2f} percent less biscuits.')
