import currency_converter as cc

def test_convert():
    assert cc.convert([("USD", "EUR", .86)], 1,
                        "USD", "EUR") == .86
    assert cc.convert([("USD", "EUR", .86)], 1.5,
                        "USD", "EUR") == 1.29
