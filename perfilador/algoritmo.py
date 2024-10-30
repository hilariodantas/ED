def selectionSort(lyst, profiler):
    for i in range(len(lyst) - 1):
        minIndex = i
        for j in range(i + 1, len(lyst)):
            profiler.comparison()
            if lyst[j] < lyst[minIndex]:
                minIndex = j
        if minIndex != i:
            lyst[i], lyst[minIndex] = lyst[minIndex], lyst[i]
            profiler.exchange()
