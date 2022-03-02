#基于双栈实现队列以及双队列实现栈

class Queue(object):
    def __init__(self):
        self.A = []
        self.B = []
    def in_queue(self,item):
        self.A.append(item)
    def pop_queue(self):
        if self.B:
            return self.B.pop(0)
        else:
            nums = len(self.A)
            if nums>0:
                for item in self.A:
                    self.B.append(item)
                    return self.B.pop(0)
            else:
                return -1


