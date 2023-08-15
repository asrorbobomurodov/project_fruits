import csv
def get_cheapest_fruit_id(data: str) -> int:
    """
    This function returns the index of the cheapest fruit
    args:
        data (str): CSV file with the fruits data
    returns:
        int: id of the cheapest fruit
    """
    f = open(data).read()
    prices = []
    id = 2
    rows = f.split("\n")
    for row in rows[1:-1]:
        item = row.split(",")
        price = float(item[-1])
        prices.append(price)
        print(prices)
    mn = min(prices)
    for i in rows[1:-1]:
        item = i.split(",")
        price = float(item[-1])
        if mn != price:
            id += 1
        if mn == price:
            break
    return id
            
    # data2 = csv.reader(f)
    # for i in data2:
    #     print(i)
  
#open file 
print(get_cheapest_fruit_id('fruits.csv'))