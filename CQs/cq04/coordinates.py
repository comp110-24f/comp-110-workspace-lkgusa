__author__ = "730663471"

# general structure
# print(xs[0], ",", ys[0])
# print(xs[0], ",", ys[1])
# print(xs[1], ",", ys[0])
# print(xs[1], ",", ys[0])


def get_coords(xs: str, ys: str) -> None:
    x_index: int = 0
    while x_index < len(xs):
        y_index: int = 0
        while y_index < len(ys):
            print("(" + xs[x_index] + "," + ys[y_index] + ")")
            y_index += 1
        x_index += 1
