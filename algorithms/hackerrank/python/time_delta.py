from dateutil import parser


def time_delta(t1, t2):
    t1 = parser.parse(t1)
    t2 = parser.parse(t2)
    return int(abs((t1 - t2).total_seconds()))


T = int(input())

for _ in range(T):
    t1 = input().strip()
    t2 = input().strip()
    print(time_delta(t1, t2))
