from collections import namedtuple

Color = namedtuple("Color", "name height")
Flask = list[Color]
Flasks = list[Flask]
Entry = tuple[int, Color, int, Color]

MAX_HEIGHT = 4


def main(flasks: Flasks):
    n = len(flasks)

    log0 = []
    mem = set()

    def solve(state: Flasks, log, memory) -> bool:
        snapshot = render(state)
        if snapshot in memory:
            return False
        memory.add(snapshot)

        if finished(state):
            for l in log:
                print("Pour", l[0], "into", l[2])
            return True

        for i in range(n):
            for j in range(n):
                if not can_pour(i, j, state):
                    continue

                pour(i, j, state, log)
                print("pour: ", render(state))

                if solve(state, log, memory):
                    return True

                # not finished but also nothing possible, undo
                unpour(state, log)
                print("undo: ", render(state))

        return False

    # call solve
    return solve(flasks, log0, mem)


def can_pour(origin: int, target: int, flasks: Flasks) -> bool:
    # Case 0: origin and target are the same
    if origin == target:
        return False

    # Case 1: target flask is full, there is nothing to pour in (false)
    if height(flasks[target]) >= 4:
        return False

    origin_color = last(flasks[origin])
    target_color = last(flasks[target])

    # Case: Nothing to pour from
    if not origin_color:
        return False

    # Case: target is empty, then only pour when there is some other color left
    if not target_color:
        return len(flasks[origin]) > 1

    # Case 2: colors don't match (false)
    if origin_color.name != target_color.name:
        return False

    # Case: when both flasks contain one element, only allow lower into higher index
    if len(flasks[origin]) == 1 and len(flasks[target]) == 1:
        return origin < target

    # Case 3
    return True


def pour(origin: int, target: int, flasks: Flasks, log: list):
    origin_color = flasks[origin].pop()
    if flasks[target]:
        target_color = flasks[target].pop()
    else:
        target_color = None

    name = origin_color.name
    if target_color:
        liquid = origin_color.height + target_color.height
    else:
        liquid = origin_color.height

    if target_color:
        possible = min(MAX_HEIGHT - height(flasks[target]), liquid)
        remaining = liquid - possible
    else:
        possible = liquid
        remaining = 0

    # modify flasks
    if possible > 0:
        flasks[target].append(Color(name, possible))
    if remaining > 0:
        flasks[origin].append(Color(name, remaining))

    # modify logs
    entry = (
        origin,
        origin_color,
        target,
        target_color,
    )
    log.append(entry)


def unpour(flasks: Flasks, log: list[Entry]):
    entry = log.pop()
    origin, origin_color, target, target_color = entry

    # restore origin, this handels residuals
    if last(flasks[origin]) and last(flasks[origin]).name == origin_color.name:
        flasks[origin].pop()
    flasks[origin].append(Color(origin_color.name, origin_color.height))

    # restore target
    # may be None
    flasks[target].pop()
    if target_color:
        flasks[target].append(Color(target_color.name, target_color.height))


def finished(flasks: Flasks) -> bool:
    for flask in flasks:
        if len(flask) > 1:
            return False
    return True


def height(flask: Flask) -> int:
    return sum([color.height for color in flask])


def last(flask: Flask):
    n = len(flask)
    if n == 0:
        return None
    return flask[n - 1]


def render(flasks: Flasks):
    color_mapping = {
        "yellow": "🟨",
        "blue": "🟦",
        "purple": "🟪",
        "green": "🌲",
        "brown": "🟫",
        "red": "🟥",
        "pink": "👚",
        "gray": "⬜️",
        "lime": "🟩",
        "sky": "🦋",
        "orange": "🟧",
    }

    res = ""
    for i, flask in enumerate(flasks):
        residual = MAX_HEIGHT
        for color in flask:
            res += color_mapping[color.name] * color.height
            residual -= color.height
        res += "⬛️" * residual
        res += "  "
    return res


if __name__ == "__main__":
    problem = [
        [Color("yellow", 1), Color("blue", 1), Color("purple", 1), Color("yellow", 1)],
        [Color("green", 1), Color("brown", 2), Color("red", 1)],
        [Color("pink", 1), Color("blue", 1), Color("purple", 1), Color("gray", 1)],
        [Color("pink", 1), Color("brown", 2), Color("purple", 1)],
        [Color("blue", 1), Color("orange", 2), Color("pink", 1)],
        [Color("green", 1), Color("lime", 1), Color("orange", 1), Color("sky", 1)],
        [Color("lime", 1), Color("purple", 1), Color("yellow", 1), Color("orange", 1)],
        [Color("green", 1), Color("red", 1), Color("lime", 1), Color("red", 1)],
        [Color("sky", 1), Color("blue", 1), Color("red", 1), Color("gray", 1)],
        [Color("gray", 1), Color("yellow", 1), Color("gray", 1), Color("green", 1)],
        [Color("sky", 1), Color("lime", 1), Color("pink", 1), Color("sky", 1)],
        [],
        [],
        # [],
    ]
    main(problem)
