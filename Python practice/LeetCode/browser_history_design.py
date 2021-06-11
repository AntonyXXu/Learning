class browserHistory:
    def __init__(self, homepage):
        self.current = homepage
        self.back = []
        self.forward = []
    
    def visit(self, url):
        self.back.append(self.current)
        self.current = url
        self.forward = []

    def back(self, steps):
        while steps > 0 and len(self.back) > 1:
            self.current = self.back.pop()
            self.forward.append(self.current)
            steps -= 1
        return self.current
    
    def forward(self, steps):
        while steps > 0 and len(self.forward) > 1:
            self.current = self.forward.pop()
            self.back.append(self.current)
            steps -= 1
        return self.current

