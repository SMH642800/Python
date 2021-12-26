from decimal import Decimal, ROUND_HALF_UP


def sum_of_trace(start_height float)
    total = start_height
    now_height = start_height2
    while now_height  1.00
        total += now_height2
        now_height = 2
    return Decimal(str(total)).quantize(Decimal('.00'), ROUND_HALF_UP)


def main()
    start_height = float(input())
    print(sum_of_trace(start_height))


if __name__ == __main__
    main()


