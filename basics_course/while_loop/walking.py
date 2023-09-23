day_target = 10000
current_steps = 0
total_day_steps_counter = 0
while current_steps != 'Going home':
    steps = int(current_steps)
    total_day_steps_counter += steps
    if total_day_steps_counter >= day_target:
        diff = total_day_steps_counter - day_target
        print('Goal reached! Good job!')
        print(f'{diff} steps over the goal!')
        break
    current_steps = input()
if total_day_steps_counter < day_target:
    current_steps = input()
    steps = int(current_steps)
    total_day_steps_counter += steps
    if total_day_steps_counter >= day_target:
        diff = total_day_steps_counter - day_target
        print('Goal reached! Good job!')
        print(f'{diff} steps over the goal!')
    else:
        diff_less = day_target - total_day_steps_counter
        print(f'{diff_less} more steps to reach goal.')
