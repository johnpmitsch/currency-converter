
def convert(rates, value, currency1, currency2):
    """converts a value from a currency to another currency taking a list of
    tuples as rates argument. for example:
    convert([("USD", "EUR", .86)], 1, "from", "USD", "to", "EUR") == .86"""

    exchange_rate = rates[0][2]
    return value * exchange_rate

if __name__ == '__main__':

    currency_rates = [("USD", "EUR", 0.86),
                      ("EUR", "JPY", 136.99),
                      ("USD", "JPY", 118.68),
                      ("GBP", "USD", 1.52),
                      ("USD", "CAD", 1.21),
                      ("EUR", "JPY", 137.10),
                      ("AUD", "USD", 0.82),
                      ("USD", "INR", 61.74),
                      ("USD", "XBT", 0.00478)
                      ]
