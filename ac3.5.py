import math
def calculate_trig(a):
    b= math.radians(a)
    c = math.sin(b)
    d = math.cos(b)
    e = math.tan(b)
    return c, d, e
if __name__ == "__main__":
    try:
        f = float(input("Enter the angle in degrees: "))

        g, h, i = calculate_trig(f)

        print(f"Sine of {f}°: {g:.4f}")
        print(f"Cosine of {f}°: {h:.4f}")
        print(f"Tangent of {f}°: {i:.4f}")
    except ValueError:
        print("Please enter a valid number for the angle.")
    except Exception as e:
        print(f"An error occurred: {e}")                                                                    