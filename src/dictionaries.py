def create_dict(cities, temperatures):
    """
    Given a list of cities and a list of temperatures, create a dictionary
    with city as key and temperature as value
    """
    raise NotImplementedError

def stock_value(product_stock, product_values):
    """
    Given are two dictionaries, the first contains the number of items in a warehouse

    product_stock = { "banana": 6, "apple": 0, "orange": 32, "pear": 15 }
    
    The second contains a dictionary with the values of each item:
    
    prices = { "banana": 4, "apple": 2, "orange": 1.5, "pear": 3 }

    return the total value of all items in the warehouse
    """
    raise NotImplementedError

def character_statistics(text):
    """
    returns the character statistics of the given text stored in a list
    of tuples (char, count)

    Characters are normalized to lower case, and non-letter characters are ignored.
    The resulting list is ordered by letter frequency, descending.

    Example:

    character_statistics("abbccc") # -> [('c', 3), ('b', 2), ('a', 1)]
    """
    raise NotImplementedError