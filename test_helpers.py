from sorter import finished, height, last, Flasks, Flask, Color


#
# finished()
#
def test_no_flasks_count_as_finished():
    assert finished([])


def test_empty_flasks_is_finished():
    assert finished([[]])


def test_single_color_is_finished():
    assert finished([[Color("green", 4)]])


def test_multiple_colors_are_finished():
    assert finished([[Color("green", 4)], [Color("blue", 4)], []])


#
# height()
#
def test_mixed_colors_are_not_finished():
    assert not finished([[Color("green", 2), Color("blue", 2)]])


def test_height_of_empty_flask():
    assert height([]) == 0


def test_height_of_flask_single_color():
    assert height([Color("green", 1)]) == 1


def test_height_of_flask_multiple_colors():
    assert height([Color("green", 1), Color("blue", 2), Color("red", 1)]) == 4


#
# last
#
def test_last_color_in_empty_flask():
    assert last([]) is None


def test_last_color_in_flask():
    assert last([Color("green", 1), Color("red", 1)]) == Color("red", 1)
