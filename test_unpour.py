from sorter import unpour, Flasks, Flask, Color


def test_unpour_empty_flask():
    """
    >pour
    G               G
    G               G
    G               G
    -----       -----
    o   t   ->  o   t
    """
    flasks = [[], [Color("green", 3)]]
    log = [(0, Color("green", 3), 1, None)]
    log_set = set(log)

    unpour(flasks, log, log_set)

    assert flasks == [[Color("green", 3)], []]
    assert log == []
    assert log_set == set()


def test_unpour_two_colors():
    """
    >pour
    G
    B           B
    B           B   G
    -----       -----
    o   t   ->  o   t
    """
    flasks = [[Color("blue", 2)], [Color("green", 1)]]
    log = [(0, Color("green", 1), 1, None)]
    log_set = set(log)

    unpour(flasks, log, log_set)

    assert flasks == [[Color("blue", 2), Color("green", 1)], []]
    assert log == []
    assert log_set == set()


def test_unpour_both_flasks_are_not_empty():
    """
    >pour
    G
    B           B   G
    B   G       B   G
    -----       -----
    o   t   ->  o   t
    """
    flasks = [[Color("blue", 2)], [Color("green", 2)]]
    log = [(0, Color("green", 1), 1, Color("green", 1))]
    log_set = set(log)

    unpour(flasks, log, log_set)

    assert flasks == [[Color("blue", 2), Color("green", 1)], [Color("green", 1)]]
    assert log == []
    assert log_set == set()
