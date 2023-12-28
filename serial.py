"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Initializes the start attribute and initializes the current value attribute to start value - 1. 
        This is because the first call to the generate method must return the start value, and every subsequent call
        to generate must increment the current value and return it. Thus, upon first call to generate, the current_value will be 
        incremented to match the start value which will be returned."""
        self.start_value = start
        self.current_value = start - 1
    
    def generate(self):
        """Increments the current value and returns it. The first time this method is called after a SerialGenerator object is first
        initialized OR after the reset method is called, it returns the start value."""
        self.current_value += 1
        return self.current_value
    
    def reset(self):
        """Resets the current value to its initial value when the SerialGenerator object was first initialized: Its start value
        minus one."""
        self.current_value = self.start_value - 1

