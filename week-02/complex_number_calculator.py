class ComplexNumber:
    def validate_and_extract(self, complex_num):
        try:
            complex(complex_num.replace('i', 'j'))
            return self.extract_parts(complex_num)
        except ValueError:
            print(f"{complex_num} is not a valid complex number.")
            return False
        
    # Extract real and imaginary parts
    def extract_parts(self, complex_num):
        c_num = complex(complex_num.replace('i', 'j'))
        return c_num.real, c_num.imag
    
    def add(self, c1, c2):
        return complex(c1[0] + c2[0], c1[1] + c2[1])
    
    def subtract(self, c1, c2):
        return complex(c1[0] - c2[0], c1[1] - c2[1])
    
    def multiply(self, c1, c2):
        return complex(c1[0] * c2[0] - c1[1] * c2[1], c1[0] * c2[1] + c1[1] * c2[0])
    
    def divide(self, c1, c2):
        denom = c2[0]**2 + c2[1]**2
        if denom == 0:
            raise ValueError("Cannot divide by zero.")
        real_part = (c1[0] * c2[0] + c1[1] * c2[1]) / denom
        imag_part = (c1[1] * c2[0] - c1[0] * c2[1]) / denom
        return complex(real_part, imag_part)

def main():
    complex_calculator = ComplexNumber()
    try:
        real1, imag1 = complex_calculator.validate_and_extract(input("Enter first complex number (e.g., a+bi or a+bj): "))
        real2, imag2 = complex_calculator.validate_and_extract(input("Enter second complex number (e.g., a+bi or a+bj): "))
        print("Choose operation: \n")
        operation = input("1. Add\n2. Subtract\n3. Multiply\n4. Divide\nEnter choice (1/2/3/4): ")
        
        if operation == '1':
            result = complex_calculator.add((real1, imag1), (real2, imag2))
            print(f"Sum is: {result.real}+{result.imag}i")
        elif operation == '2':
            result = complex_calculator.subtract((real1, imag1), (real2, imag2))
            print(f"Difference is: {result.real}+{result.imag}i")
        elif operation == '3':
            result = complex_calculator.multiply((real1, imag1), (real2, imag2))
            print(f"Product is: {result.real}+{result.imag}i")
        elif operation == '4':
            result = complex_calculator.divide((real1, imag1), (real2, imag2))
            print(f"Quotient is: {result.real}+{result.imag}i")
        else:   
            print("Invalid operation choice. Defaulting to addition.")
            result = complex_calculator.add((real1, imag1), (real2, imag2))
            print(f"Sum is: {result.real}+{result.imag}i")
        
    except ValueError as e:
        print(f"Error: {e}")
        return

if __name__ == "__main__":
    main()