import itertools
import sys
from collections.abc import Sequence, Iterable

PathTuple = tuple[int, int]
Vector = list[float]
WaypointsDict = dict[PathTuple, str]


def calc_hypotenuse(first: PathTuple, second: PathTuple) -> float:
    """Get distance between two points"""
    x, y = 0, 1
    return ((second[x] - first[x]) ** 2 + (second[y] - first[y]) ** 2) ** 0.5


def get_distance(path: Sequence[PathTuple]) -> Vector:
    """Get distance for a sequence of waypoints"""
    return [calc_hypotenuse(path[i], path[i + 1]) for i in range(len(path) - 1)]


def print_pretty(path_tuple: Sequence[Sequence[PathTuple], Vector, float]) -> None:
    """Print waypoints and distance between them and full path length"""

    pretty_way = []
    step_sum = 0

    for step in zip(path_tuple[0], (0, *path_tuple[1])):
        point = step[0]
        step_sum += step[1]
        distance_to_next = f"[{step_sum}]" if step[1] != 0 else ''
        pretty_way.append(f"{point}{distance_to_next}")

    print(*pretty_way, sep=" -> ", end=f" = {path_tuple[2]}\n")

def test_myoutput(capsys):  # or use "capfd" for fd-level
    print("hello")
    sys.stderr.write("world\n")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == "world\n"
    print("next")
    captured = capsys.readouterr()
    assert captured.out == "next\n"


def main(waypoints: Iterable[PathTuple]):
    post = (0, 1)
    all_paths = itertools.permutations(waypoints)
    result_paths = []

    for way in all_paths:
        temp_path = (post, *way, post)
        distance = get_distance(temp_path)
        result_paths.append((temp_path, distance, sum(distance)))
    return sorted(result_paths, key=lambda path: path[2])


if __name__ == '__main__':
    points = {(2, 5): "Ул. Грибоедова, 104/25",
              (5, 2): "Ул. Бейкер стрит, 221б",
              (6, 6): "Ул. Большая Садовая, 302-бис",
              (8, 3): "Вечнозелёная Аллея, 742",
              }
    test_data = ((1, 4), (4, 1), (5, 5), (7, 2))

    result = main(test_data)
    min_path = result[0][2]
    index = 0

    while result[index][2] == min_path:
        print_pretty(result[index])
        index += 1
