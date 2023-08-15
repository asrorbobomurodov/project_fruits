def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    rows = data.split("\n")
    fruits = []
    for row in rows[1:-1]:
        item = row.split(',')
        fruits.append(item[0])  
    return fruits
data = open('fruits.csv').read()
print(get_frutis_name(data))

    