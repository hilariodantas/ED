if __name__ == "__main__":
    from profiler import Profiler  
    from algoritmo import selectionSort  

    p = Profiler()
    
    print("Teste para 10 valores\n")
    p.test(selectionSort, size=10, comp=True, exch=True, trace=False)
    
    print("Teste para 100 valores\n")
    p.test(selectionSort, size=100, comp=True, exch=True, trace=False)

    print("Teste para 1000 valores\n")
    p.test(selectionSort, size=1000, comp=True, exch=True, trace=False)

    print("Teste para 10000 valores\n")
    p.test(selectionSort, size=10000, comp=True, exch=True, trace=False)
