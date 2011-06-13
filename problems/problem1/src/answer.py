class Main():
    def isMultiple(self, number):
        if not (number % 3) or not (number % 5):
            return True
        return False
    
    def inRange(self, init=1, end=False):
        if not end:
            end = init
            init = 1
        return [x for x in range(init, end + 1) if self.isMultiple(x)]
    
    def solve(self):
        return sum(self.inRange(999))
        
if __name__ == '__main__':
    print 'The answer is: %s' % Main().solve()