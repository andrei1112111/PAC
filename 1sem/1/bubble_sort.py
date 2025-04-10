"""LR 1.1"""

def bubble_sort(progress_list: list):
    for i in range(0, len(progress_list), 1):
        for j in range(i+1, len(progress_list), 1):
            if progress_list[i] > progress_list[j]:
                progress_list[i], progress_list[j] = progress_list[j], progress_list[i]

    return progress_list


if __name__ == "__main__":
    import argparse
    import random


    random.seed(1)
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-list_length',
        type=int,
        default=10
    )

    args = parser.parse_args()

    unsorted_list = [
        random.random() for _ in range(args.list_length)
    ]

    print(bubble_sort(unsorted_list))
