def f(x):
    return x**3 + 8

def main():
    x = 9
    result = f(x)
    print(f"Result:{result}")
    
    #check if larger than 27
    if result > 27:
        print("YAY!")

# Call the main function
if __name__ == "__main__":
    main()
