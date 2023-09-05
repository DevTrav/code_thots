class BoolType:
    def __init__(self, value=False):
        if not isinstance(value, bool):
            raise ValueError("BoolType can only be initialized with a boolean value.")
        self.__value = value

    def __str__(self):
        return str(self.__value)

    def __bool__(self):
        return self.__value
    
    @classmethod
    def true(cls):
        """Constructor of a true value"""
        return BoolType(True)
    @classmethod 
    def false(cls):
        """Constructor of a false value"""
        return BoolType(False)

# Example usage
if __name__ == "__main__":
    # Initializing with True
    true_value = BoolType(True)
    print(true_value)  # Output: True
    print(bool(true_value))  # Output: True

    # Initializing with False (default value)
    false_value = BoolType()
    print(false_value)  # Output: False
    print(bool(false_value))  # Output: False

    # Trying to initialize with a non-boolean value will raise a ValueError
    try:
        invalid_value = BoolType("hello")
    except ValueError as e:
        print(f"Pass: {e}")  # Output: Error: BoolType can only be initialized with a boolean value.

        # Review type coersion 
        # Review static methods
        # Review class methods
        # Review private methods
        # Currently has two contructors
        # Hoemwork: make combinators.
        # Combinators: AND, OR and  NOT
        # Deligate combinators to the boolean class and reconstruct it
        # Convert tests to asserts (could involve helper functions)
    

    print(BoolType.true())

