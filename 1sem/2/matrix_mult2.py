import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-input_file',
        type=str,
        default='matrix2.txt'
    )
    parser.add_argument(
        '-output_file',
        type=str,
        default='output.txt'
    )

    args = parser.parse_args()

    matrix1 = []
    matrix2 = []


    # load
    with open(args.input_file) as file:
        line = file.readline()

        while line.split():
            matrix1.append(
                [int(i) for i in line.split()]
            )

            line = file.readline()

        line = file.readline()

        while line.split():
            matrix2.append(
                [int(i) for i in line.split()]
            )

            line = file.readline()


    # Свертка
    # output matrix
    matrix_1_sv_2 = [
        [0 for _ in range(len(matrix1[0]) - len(matrix2[0]) + 1)] for _ in range(len(matrix1) - len(matrix2) + 1)
    ]

    for i in range(len(matrix1) - len(matrix2) + 1):
        for j in range(len(matrix1[0]) - len(matrix2[0]) + 1):
            for u in range(len(matrix2)):
                for v in range(len(matrix2[0])):
                    matrix_1_sv_2[i][j] += matrix1[i+u][j+v] * matrix2[u][v]

    # save
    with open(args.output_file, "w") as file:
        file.writelines(
            [" ".join([str(j) for j in i]) + '\n' for i in matrix_1_sv_2]
        )
