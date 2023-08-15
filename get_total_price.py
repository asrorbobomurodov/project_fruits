def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    rows = data.split("\n")
    total = 0
    
    for row in rows[1:-1]:
        name, price = row.split(",")
        total += float(price)
        
    return round(total, 2)

data = open('fruits.csv').read()
print(get_total_price(data))

    