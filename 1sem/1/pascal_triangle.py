"""LR 1.2"""


def make_paskal_triangle(height: int) -> list:
    triangle = [[1]]

    for layer in range(1, height):
        triangle.append([1] + triangle[-1])

        for i in range(1, len(triangle[layer]) - 1, 1):
            triangle[layer][i] += triangle[layer][i+1]


    return triangle


def print_paskal_triangle(triangle: list):
    for i in range(0, len(triangle), 1):

        print(" " * (len(triangle) - i) +  " ".join([str(i) for i in triangle[i]]))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-triangle_height',
        type=int,
        default=5
    )

    args = parser.parse_args()

    if args.triangle_height <= 0:
        exit()

    print_paskal_triangle(
        make_paskal_triangle(
            args.triangle_height
        )
    )
