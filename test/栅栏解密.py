def decrypt(self, dst):
        if not isinstance(dst, (types.StringType, types.UnicodeType)):
            raise TypeError(u'Decryption dst text is not string')
        self.Length = len(dst)
        self.Column = int(math.ceil(self.Length / self.Row))
        try:
            self.__check()
        except Exception, msg:
            print msg
        #get mask order
        self.__getOrder()
        
        grid  = [[] for i in range(self.Row)]
        space = self.Row * self.Column - self.Length
        ns    = self.Row - space
        prevE = 0
        for i in range(self.Row):
            if self.Mask != None:
                s = prevE
                O = 0
                for x,y in enumerate(self.Order):
                    if i == y:
                        O = x
                        break
                if O < ns: e = s + self.Column
                else: e = s + (self.Column - 1)
                r = dst[s : e]
                prevE = e
                grid[O] = list(r)
            else:
                startIndex = 0
                endIndex   = 0
                if i < self.Row - space:
                    startIndex = i * self.Column
                    endIndex   = startIndex + self.Column
                else:                
                    startIndex = ns * self.Column + (i - ns) * (self.Column - 1)
                    endIndex   = startIndex + (self.Column - 1)
                r = dst[startIndex:endIndex]
                grid[i] = list(r)
        res = ''
        for c in range(self.Column):
            for i in range(self.Row):
                line = grid[i]
                if len(line) == c:
                    res += ' '
                else:
                    res += line[c]
        return res

