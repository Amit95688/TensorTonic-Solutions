def min_max_scaling(data: list) -> list:
    n = len(data)
    m = len(data[0])

    min_val = [float('inf')] * m
    max_val = [float('-inf')] * m

    # Find min and max for each column
    for i in range(n):
        for j in range(m):
            min_val[j] = min(min_val[j], data[i][j])
            max_val[j] = max(max_val[j], data[i][j])

    # Normalize each column
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            if max_val[j] == min_val[j]:
                row.append(0.0)
            else:
                x = (data[i][j] - min_val[j]) / (max_val[j] - min_val[j])
                row.append(x)
        result.append(row)

    return result