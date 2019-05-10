def calculate(distance,no_of_passengers):
    price_per_litre_of_fuel=70
    Mileage = 10
    price_per_ticket=80
    total_inversement=((distance/Mileage)*price_per_litre_of_fuel)
    total_gain=price_per_ticket*no_of_passengers
    if(total_gain>total_inversement):
        profit=total_gain-total_inversement
        return profit
    else:
        return -1
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))
