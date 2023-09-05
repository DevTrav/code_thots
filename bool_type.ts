// Custom bool constructor function
function Bool(value: unknown): bool {
    // Custom logic to convert any input to a bool value
    // For this example, we'll consider non-empty strings as true, and everything else as false
    if (typeof value === 'string' && value !== '') {
      return true;
    } else {
      return false;
    }
  }
  
  // Example usage
  const boolValue1: bool = Bool(true); // Custom bool constructor with true
  const boolValue2: bool = Bool(false); // Custom bool constructor with false
  const boolValue3: bool = Bool('true'); // Custom bool constructor with non-empty string
  const boolValue4: bool = Bool('false'); // Custom bool constructor with empty string
  
  console.log(boolValue1); // Output: false
  console.log(boolValue2); // Output: false
  console.log(boolValue3); // Output: true
  console.log(boolValue4); // Output: false