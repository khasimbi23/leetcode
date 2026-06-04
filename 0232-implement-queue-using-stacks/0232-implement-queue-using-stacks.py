class MyQueue:

    def __init__(self):
        self.st_in = []
        self.st_out = []

    def push(self, x: int) -> None:
        self.st_in.append(x)

    def pop(self) -> int:
        self.peek()  
        return self.st_out.pop()

    def peek(self) -> int:
        if not self.st_out:   
            while self.st_in:
                self.st_out.append(self.st_in.pop())
        return self.st_out[-1]

    def empty(self) -> bool:
        return not self.st_in and not self.st_out