
class StackList:
    def __init__(self):
        self.stackList = []
    
    def __str__(self):
        values = self.stackList.reverse()
        values = [str(x) for x in self.stackList]
        return '\n'.join(values)

    def isEmpty(self):
        return self.stackList.count == 0

    def push(self, value):
        self.stackList.append(value)
        return str(value)+'was added'

    def pop(self):
        if (self.isEmpty):
            return "List is empty"
        else:
            self.stackList.pop()
            return 'Last value removed'

    def peek(self):
        if (self.isEmpty):
            return "List is empty"
        else:
            return self.stackList[len(self.stackList)-1]

stackList = StackList()
stackList.push(5)
stackList.push(8)
stackList.isEmpty()
print(stackList)