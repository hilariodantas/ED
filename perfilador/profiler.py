import time
import random

class Profiler(object):
    def test(self, function, lyst=None, size=10, unique=True, comp=True, exch=True, trace=False):
      
        self.comp = comp
        self.exch = exch
        self.trace = trace
        
        if lyst is not None:
            self.lyst = lyst
        elif unique:
            self.lyst = list(range(1, size + 1))
            random.shuffle(self.lyst)
        else:
            self.lyst = [random.randint(1, size) for _ in range(size)]

        self.exchCount = 0
        self.cmpCount = 0
        self.startClock()
        
        function(self.lyst, self)
        
        self.stopClock()
        print(self)

    def exchange(self):
        if self.exch:
            self.exchCount += 1
        if self.trace:
            print(self.lyst)

    def comparison(self):
        if self.comp:
            self.cmpCount += 1

    def startClock(self):
        self.start = time.time()

    def stopClock(self):
        self.elapsedTime = round(time.time() - self.start, 3)

    def __str__(self):
        result = f"Tamanho do problema: {len(self.lyst)}\n"
        result += f"Tempo gasto: {self.elapsedTime}\n"
        if self.comp:
            result += f"Comparações: {self.cmpCount}\n"
        if self.exch:
            result += f"Trocas: {self.exchCount}\n"
        return result