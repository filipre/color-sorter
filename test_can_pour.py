from sorter import can_pour, Flasks, Flask, Color


def test_can_pour_into_empty_flask():
    flasks = [[Color("blue", 1), Color("green", 1)], []]
    assert can_pour(0, 1, flasks, set())


def test_can_pour_into_same_color():
    flasks = [[Color("green", 1)], [Color("green", 1)]]
    assert can_pour(0, 1, flasks, set())


def test_cannot_pour_into_same_color_higher_index_single_element():
    flasks = [[Color("green", 1)], [Color("green", 1)]]
    assert not can_pour(1, 0, flasks, set())


def test_cannot_pour_from_itself():
    flasks = [[Color("green", 1)]]
    assert not can_pour(0, 0, flasks, set())


def test_cannot_pour_from_empty_flask():
    flasks = [[], []]
    assert not can_pour(0, 0, flasks, set())


def test_cannot_pour_into_wrong_color():
    flasks = [[Color("green", 1)], [Color("blue", 1)]]
    assert not can_pour(0, 1, flasks, set())


def test_cannot_pour_into_full_flasks():
    flasks = [[Color("green", 1)], [Color("green", 4)]]
    assert not can_pour(0, 1, flasks, set())


def test_cannot_pour_whole_flask_into_empty_flask():
    flasks = [[Color("green", 3)], []]
    assert not can_pour(0, 1, flasks, set())


def test_cannot_repeat_same_operation():
    flasks = [[Color("green", 1)], [Color("green", 1)]]
    origin, target = 0, 1
    logs = [(origin, Color("green", 1), target, Color("green", 1))]
    assert not can_pour(origin, target, flasks, set(logs))
