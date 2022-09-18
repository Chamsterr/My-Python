def sum_of_intervals(intervals):
    intervals = sorted(intervals)
    arr = [list(intervals[0])]
    for a in arr:
        for interval in intervals:
            if a[0] < interval[0] and a[1] < interval[0]:
                arr.append(list(interval))
                break
            if a[0] <= interval[0] and a[1] >= interval[1]:
                continue
            elif interval[1] > a[1] and interval[0] <= a[1]:
                a[1] = interval[1]
            elif a[0] <= interval[1]:
                a[0] = interval[0]
            elif a[0] >= interval[0] and a[1] <= interval[1]:
                a[1] = interval[1]
                a[0] = interval[0]
            
            elif a[0] >= interval[0] and a[1] < interval[1]:
                a[0] = interval[0]
                a[1] = interval[1]
    print(arr)
    return sum(([sum([-arr[x][0], arr[x][1]]) for x in range(len(arr))]))

            


print(sum_of_intervals([(41, 73), (-58, 298), (263, 281)]))
