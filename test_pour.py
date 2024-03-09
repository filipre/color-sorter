from sorter import pour, Flasks, Flask, Color

# origin: int, target: int, flasks: Flasks, log: list, log_set: set


def test_pour_liquid_into_empty():
    flasks = [[Color("green", 1)], []]
    log = []

    pour(0, 1, flasks, log)

    assert flasks == [[], [Color("green", 1)]]
    entry = (0, Color("green", 1), 1, None)
    assert log == [entry]


def test_pour_liquid_into_color():
    flasks = [[Color("green", 1)], [Color("green", 1)]]
    log = []

    pour(0, 1, flasks, log)

    assert flasks == [[], [Color("green", 2)]]
    entry = (0, Color("green", 1), 1, Color("green", 1))
    assert log == [entry]


def test_pour_liquid_with_residual():
    flasks = [[Color("green", 3)], [Color("blue", 2), Color("green", 1)]]
    log = []

    pour(0, 1, flasks, log)

    assert flasks == [[Color("green", 2)], [Color("blue", 2), Color("green", 2)]]
    entry = (0, Color("green", 3), 1, Color("green", 1))
    assert log == [entry]
