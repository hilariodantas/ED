if __name__ == "__main__":
    from profiler import Profiler  
    from algoritmo import selectionSort  

    # Criando um objeto
    p = Profiler()
    
    # Teste
    p.test(selectionSort, size=15, comp=True, exch=True, trace=True)