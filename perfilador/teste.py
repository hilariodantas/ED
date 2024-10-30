if __name__ == "__main__":
    from profiler import Profiler  
    from algoritmo import selectionSort  

    p = Profiler()
    
    # Teste
    p.test(selectionSort, size=100, comp=True, exch=True, trace=False)