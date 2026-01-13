def get_fare(age: int, is_peak: bool) -> float:
    if age < 0:
        raise ValueError("Not valid age")
    if not type(is_peak) is bool:
        raise TypeError("is_peak needs to be set as a bool")
    if not type(age) is int:
        raise TypeError("age needs to be set as an int")
    fare = 0.0
    if age > 15 and age < 65:
        fare = 2.5
    elif age < 16:
        fare = 1.25
    elif age >= 65:
        fare = 1.00

    if is_peak == False:
        discount = 0.8
    else:
        discount = 1

    final_fare = fare * discount
    return float(final_fare)


