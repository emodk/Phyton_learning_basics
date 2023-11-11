cars_list = input().split('>>')
total_taxes = 0
valid_car_list = ['family', 'heavyDuty', 'sports']

for i in range(0, len(cars_list)):
    final_car_tax = 0
    car_details_list = cars_list[i].split()
    if car_details_list[0] not in valid_car_list:
        print('Invalid car type.')

    elif car_details_list[0] == 'family':
        family_tax = [50, -5, 12]
        family_tax[1] *= int(car_details_list[1])
        family_tax[2] *= int(car_details_list[2]) // 3000
        final_car_tax = sum(family_tax)
        total_taxes += final_car_tax
        print(f'A {car_details_list[0]} car will pay {final_car_tax:.2f} euros in taxes.')

    elif car_details_list[0] == 'heavyDuty':
        heavy_duty_tax = [80, -8, 14]
        heavy_duty_tax[1] *= int(car_details_list[1])
        heavy_duty_tax[2] *= int(car_details_list[2]) // 9000
        final_car_tax = sum(heavy_duty_tax)
        total_taxes += final_car_tax
        print(f'A {car_details_list[0]} car will pay {final_car_tax:.2f} euros in taxes.')

    elif car_details_list[0] == 'sports':
        sport_tax = [100, -9, 18]
        sport_tax[1] *= int(car_details_list[1])
        sport_tax[2] *= int(car_details_list[2]) // 2000
        final_car_tax = sum(sport_tax)
        total_taxes += final_car_tax
        print(f'A {car_details_list[0]} car will pay {final_car_tax:.2f} euros in taxes.')

print(f'The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.')
