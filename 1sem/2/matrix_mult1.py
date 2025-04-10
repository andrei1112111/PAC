import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-input_file',
        type=str,
        default='matrix.txt'
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


        for i in range(len(matrix1[0])):
            matrix2.append(
                [int(i) for i in file.readline().split()]
            )


    # mult
    # output matrix len(matrix1) x len(matrix2[0])
    matrix_1_mult_2 = [
        [0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))
    ]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix1[0])):
                matrix_1_mult_2[i][j] += sum(
                    [matrix1[i][k] * matrix2[k][j]]
                )


    # save
    with open(args.output_file, "w") as file:
        file.writelines(
            [" ".join([str(j) for j in i]) + '\n' for i in matrix_1_mult_2]
        )
