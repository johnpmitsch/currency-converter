import currency_converter as cc

def test_convert():
    assert cc.convert([("USD", "EUR", .86)], 1,
                                "from", "USD", "to", "EUR") == .86
