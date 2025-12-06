'''
Complex Number Calculator: Rectangular to Polar and vice-versa
Description:
    - Rectangular->Polar: Takes a complex vector and converts into phase difference (theta) and magnitude.
    - Polar->Rectangular: Takes magnitute & phase difference (theta) and converts into complex number.
'''

import cmath
import math
class ComplexNumberConverter:
    def extract_parts(self, complex_num):
        c_num = complex(complex_num.replace('i', 'j'))
        return c_num.real, c_num.imag
    
    def rectangular_to_polar(self, complex_num):
        # c_num = complex(complex_num.replace('i', 'j'))
        # magnitude = abs(c_num)
        # angle = math.degrees(cmath.phase(c_num))
        # return magnitude, angle
        
        a, b = self.extract_parts(complex_num)
        # magnitude calculation
        # ∣z1​∣=a12​+b12​
        magnitude = math.sqrt(a**2 + b**2)
    
        # angle calculation
        # θ=tan−1(b/a)
        # Angle preserves quadrant in radians
        angle_rad_safe = math.atan2(b, a)
        # Convert to degrees
        angle = math.degrees(angle_rad_safe)
        
        return magnitude, angle

    def polar_to_rectangular(self, magnitude, angle):
        # real (a) and imaginary (b) part calculation
        # a = r cosθ, where r = magnitude and θ = angle in degrees
        # b = r sinθ
        angle_rad = math.radians(angle)
        a = magnitude * math.cos(angle_rad)
        b = magnitude * math.sin(angle_rad)
        return complex(a, b)
    
def main():
    converter = ComplexNumberConverter()
    choice = input("Choose conversion:\n1. Rectangular to Polar\n2. Polar to Rectangular\nEnter choice (1/2): ")
    
    if choice == '1':
        complex_num = input("Enter complex number in rectangular form (e.g., a+bi): ")
        magnitude, angle = converter.rectangular_to_polar(complex_num)
        print(f"Magnitude: {magnitude}, Angle (degrees): {angle}")
        
    elif choice == '2':
        magnitude = float(input("Enter magnitude: "))
        angle = float(input("Enter angle in degrees: "))
        rect_num = converter.polar_to_rectangular(magnitude, angle)
        print(f"Rectangular form: {rect_num.real:2f}+{rect_num.imag:2f}i")
        
    else:
        print("Invalid choice. Please select 1 or 2.")
        
if __name__ == "__main__":
    main()