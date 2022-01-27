import itertools
from collections.abc import Sequence

PathTuple = tuple[int, int]
Vector = list[float]
ResultSequence = tuple[Sequence[PathTuple], Vector, float]


def get_hypotenuse(first: PathTuple, second: PathTuple) -> float:
    """Get distance between two points"""

    return ((second[0] - first[0]) ** 2 + (second[1] - first[1]) ** 2) ** 0.5


def get_distance(path: Sequence[PathTuple]) -> list[float]:
    """Get distance for a sequence of waypoints"""

    return [get_hypotenuse(path[i], path[i + 1]) for i in range(len(path) - 1)]


def pretty_print(path_tuple: ResultSequence) -> None:
    pretty_way = []
    step_sum = 0

    for step in zip(path_tuple[0], (0, *path_tuple[1])):
        point = step[0]
        step_sum += step[1]
        distance_to_next = f"[{step_sum}]" if step[1] != 0 else ''
        pretty_way.append(f"{point}{distance_to_next}")

    print(*pretty_way, sep=" -> ", end=f" = {path_tuple[2]}\n")


if __name__ == '__main__':
    points = {(2, 5): "Ул. Грибоедова, 104/25",
              (5, 2): "Ул. Бейкер стрит, 221б",
              (6, 6): "Ул. Большая Садовая, 302-бис",
              (8, 3): "Вечнозелёная Аллея, 742",
              }
    test_data = ((1, 4), (4, 1), (5, 5), (7, 2))
    post = (0, 1)
    all_paths = itertools.permutations(test_data)
    result_paths = []

    for way in all_paths:
        temp_path = (post, *way, post)
        distance = get_distance(temp_path)
        result_paths.append((temp_path, distance, sum(distance)))
    result = sorted(result_paths, key=lambda path: path[2])

    min_path = result[0][2]
    index = 0
    while result[index][2] <= min_path:
        pretty_print(result[index])
        index += 1
