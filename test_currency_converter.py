import currency_converter as cc

currency_rates = [("USD", "EUR", 0.86),
                  ("EUR", "JPY", 136.99),
                  ("USD", "JPY", 118.68),
                  ("GBP", "USD", 1.52),
                  ("USD", "CAD", 1.21),
                  ("AUD", "USD", 0.82),
                  ("USD", "INR", 61.74),
                  ("USD", "XBT", 0.00478)
                  ]

def test_convert():
    assert cc.convert([("USD", "EUR", .86)], 1, "USD", "EUR") == .86
    assert cc.convert([("USD", "EUR", .86)], 1.5, "USD", "EUR") == 1.29
    assert cc.convert(currency_rates, 1.5, "USD", "EUR") == 1.5 * 0.86
    assert cc.convert(currency_rates, 1.5, "USD", "JPY") == 1.5 * 118.68
    assert cc.convert(currency_rates, 1.5, "EUR", "JPY") == 1.5 * 136.99
    assert cc.convert(currency_rates, 100, "JPY", "EUR") == 100 / 136.99
    assert cc.convert(currency_rates, 1, "USD", "USD") == 1

def test_find_currency_rate():
    assert cc.find_currency_rate(currency_rates,
                                 "USD", "JPY") == ("USD", "JPY", 118.68)
    assert cc.find_currency_rate(currency_rates,
                                 "JPY", "USD") == ("USD", "JPY", 118.68)
    #add a test for opposite flipped rates
def test_reverse_rate():
    assert cc.reverse_rate(("USD", "CAD", 1.21)) == 1/1.21

def test_is_reversed():
    assert cc.is_reversed(("USD", "CAD", 1.21), "USD", "CAD") == False
    assert cc.is_reversed(("USD", "CAD", 1.21), "CAD", "USD") == True

def test_is_same():
    assert cc.is_same("USD", "USD") == True
    assert cc.is_same("GBP", "CAD") == False
