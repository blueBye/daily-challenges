import numbers


class Chain:
    def __init__(self, value):
        valid = False
        if isinstance(value, str):
            valid = True
        elif isinstance(value, numbers.Number) and not isinstance(value, bool):
            valid = True
        
        if valid == False:
            raise Exception("invalid operation")
        self.value = value

    def __call__(self, other_value):
        valid = False
        if type(self.value) == type(other_value):
            valid = True
        if isinstance(self.value, numbers.Number) and isinstance(other_value, numbers.Number):
            valid = True
        if valid == False:
            raise Exception("invalid operation")
        
        if isinstance(other_value, str):
            self.value += f" {other_value}"
        else:
            self.value += other_value
        return self
    
    def __eq__(self, other):
        if isinstance(other, Chain):
            return self.value == other.value
        return self.value == other

    def __str__(self):
        return f"{self.value}"

