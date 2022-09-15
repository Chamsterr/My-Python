def hanoi(i, j, n):
    if n == 1:
        print(f"Move disk 1 from pin {i} to pin {j}")
    else:
        tmp = 6 - i - j
        hanoi(i, tmp, n - 1)
        print(f"Move disk {n} from pin {i} to pin {j}")
        hanoi(tmp, j, n - 1)

hanoi(1, 2, 5)