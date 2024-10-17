def calculateAndPrint():
    # sum of two floats
    float1 = 3.2
    float2 = 3.4
    sum = float1 + float2
    
    print(f"\n\nThe sum of {float1} and {float2} is {sum}, and the data type is a float.")
    
    # difference between two integers
    int1 = 5
    int2 = 2
    difference = int1 - int2
    
    print(f"The difference between {int1} and {int2} is {difference}, and the data type is an integer.")
    
    # product of a float and integer
    product = float1 * int1
    print(f"The product of {float1} and {int1} is {product}, and the data type is a float.\n\n")

def main():
    calculateAndPrint()
    
if __name__ == "__main__":
    main()