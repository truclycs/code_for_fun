if __name__ == "__main__":
    point_set = []
    for i in range(8):
        x, y = map(int, input().split())
        point_set.append((x, y))

    point_set.sort()

    if point_set[0][0] == point_set[1][0] == point_set[2][0]\
        and point_set[3][0] == point_set[4][0]\
        and point_set[5][0] == point_set[6][0] == point_set[7][0]\
        and point_set[2][0] != point_set[3][0]\
        and point_set[4][0] != point_set[5][0]\
        and point_set[0][1] == point_set[3][1] == point_set[5][1]\
        and point_set[1][1] == point_set[6][1]\
        and point_set[2][1] == point_set[4][1] == point_set[7][1]\
        and point_set[0][1] != point_set[1][1]\
        and point_set[1][1] != point_set[2][1]:
            print("respectable")
    else:
        print("ugly")