def round_up(number):
    x = 10

    whole_number = number // x
    remainder = number % x
    
    if remainder >= 5:
        return x*(whole_number+1)
        return x(*whole_number)
     
print(round_up(35))
