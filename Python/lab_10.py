import math

class Vector2D:
    # Class variable to track number of vector objects
    object_count = 0

    def __init__(self, x=0, y=0):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Vector components must be numeric (int or float).")
        
        self.__x = x   # Private attribute
        self.__y = y   # Private attribute

        Vector2D.object_count += 1

    # Getter methods
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    # Magnitude method
    def magnitude(self):
        return math.sqrt(self.__x**2 + self.__y**2)

    # -----------------------------
    # Operator Overloading
    # -----------------------------

    # Vector Addition
    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.__x + other.__x,
                            self.__y + other.__y)
        raise TypeError("Addition is only supported between Vector2D objects.")

    # Vector Subtraction
    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.__x - other.__x,
                            self.__y - other.__y)
        raise TypeError("Subtraction is only supported between Vector2D objects.")

    # Multiplication (Scalar OR Dot Product)
    def __mul__(self, other):
        # Scalar multiplication
        if isinstance(other, (int, float)):
            return Vector2D(self.__x * other,
                            self.__y * other)

        # Dot product
        if isinstance(other, Vector2D):
            return self.__x * other.__x + self.__y * other.__y

        raise TypeError("Multiplication supports scalar or Vector2D only.")

    # Reverse multiplication (for scalar * vector)
    def __rmul__(self, other):
        return self.__mul__(other)

    # Equality check (component-wise)
    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.__x == other.__x and self.__y == other.__y
        return False

    # Less-than (based on magnitude)
    def __lt__(self, other):
        if isinstance(other, Vector2D):
            return self.magnitude() < other.magnitude()
        raise TypeError("Comparison only supported between Vector2D objects.")

    # String representation
    def __str__(self):
        return f"({self.__x}, {self.__y})"

    # Representation for debugging
    def __repr__(self):
        return f"Vector2D({self.__x}, {self.__y})"

def main():
    print("Creating vectors...")
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)
    v3 = Vector2D(3, 4)

    print("\nVectors:")
    print("v1 =", v1)
    print("v2 =", v2)
    print("v3 =", v3)

    print("\nMagnitude:")
    print("Magnitude of v1 =", v1.magnitude())

    print("\nAddition:")
    print("v1 + v2 =", v1 + v2)

    print("\nSubtraction:")
    print("v1 - v2 =", v1 - v2)

    print("\nScalar Multiplication:")
    print("v1 * 3 =", v1 * 3)
    print("3 * v1 =", 3 * v1)

    print("\nDot Product:")
    print("v1 * v2 =", v1 * v2)

    print("\nEquality Check:")
    print("v1 == v3 ?", v1 == v3)
    print("v1 == v2 ?", v1 == v2)

    print("\nMagnitude Comparison:")
    print("v1 < v2 ?", v1 < v2)
    print("v2 < v1 ?", v2 < v1)

    print("\nTotal Vector Objects Created:",
          Vector2D.object_count)


if __name__ == "__main__":
    main()