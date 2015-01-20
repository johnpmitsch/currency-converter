
def convert(rates, value, from_currency, to_currency):
    """Converts a value from a currency to another currency taking a list of
    tuples as rates argument. for example:
    convert([("USD", "EUR", .86)], 1, "USD", "EUR") == .86"""

    currency_rate = find_currency_rate(rates, from_currency, to_currency)
    if is_same(from_currency, to_currency):
        return value
    elif is_reversed(currency_rate, from_currency, to_currency):
        return reverse_rate(currency_rate) * value
    else:
        return value * currency_rate[2]


def find_currency_rate(rates, from_currency, to_currency):
    """Finds the currency rate for the from and to currency, returns the tuple
    containing the rate irregardless of order"""
    currency_rate = [rate for rate in rates
                     if set((from_currency, to_currency)) ==
                     set((rate[0], rate[1]))]
    try:
        return currency_rate[0]
    except IndexError:
        print("Can not find exchange rate")


def reverse_rate(rate_tuple):
    """Returns a reversed currency rate, taking a tuple as input"""
    return 1 / rate_tuple[2]


def is_reversed(rate_tuple, from_currency, to_currency):
    """Checks to see if the currency rate is the reverse of the from
    and to currency"""
    if (rate_tuple[1] == from_currency) and (rate_tuple[0] == to_currency):
        return True
    else:
        return False


def is_same(from_currency, to_currency):
    return from_currency == to_currency

if __name__ == '__main__':

    currency_rates = [("USD", "EUR", 0.86),
                      ("EUR", "JPY", 136.99),
                      ("USD", "JPY", 118.68),
                      ("GBP", "USD", 1.52),
                      ("USD", "CAD", 1.21),
                      ("AUD", "USD", 0.82),
                      ("USD", "INR", 61.74),
                      ("USD", "XBT", 0.00478)
                      ]
