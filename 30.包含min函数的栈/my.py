#具有最小值的栈结构

class minStack(object):

    def __init__(self):
        self.data_stack = []
        self.mins_stack = []
    def pop(self):
        #if data is not null
        if self.data_stack > 0:
            if (self.mins_stack):
                return  self.data_stack.pop(-1)
            elif(self.data_stack[-1]==self.mins_stack[-1]):
                self.mins_stack.pop(-1)
                return  self.data_stack.pop(-1)
        else:
            return -1

    def insert(self,value):
        self.data_stack.append(value)
        if self.mins_stack:
            if self.data_stack[-1] < self.mins_stack[-1]:
                self.mins_stack.append(value)
        else:
            self.mins_stack.append(value)

    def min(self):
        return self.mins_stack[-1]






