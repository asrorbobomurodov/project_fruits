def get_expensive_fruit(data: str) -> str:
    """
    This function returns the name of the most expensive fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the most expensive fruit
    """
    rows = data.split("\n")
    mx = float(rows[1].split(",")[-1])
    name = ""
    for row in rows[1:-1]:
        item = row.split(",")
        price = float(item[-1])
        if mx < price:
            mx = price
            name = item[0]
    return name
    # your code here
    return
data = open('fruits.csv')
print(get_expensive_fruit(data.read()))


