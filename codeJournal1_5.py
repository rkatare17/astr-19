import numpy as np

# function that returns sin(x)
def returnSin(x):
    return np.sin(x)

def main():
    x_values = np.linspace(0,2*np.pi,1000)
    sin_values = returnSin(x_values)
    
    print(f"       x   vs   sin(x)")
    for i in range(1000):
        print(f"{x_values[i]:>10.4f} {sin_values[i]:>10.4f}")
        
if __name__ == "__main__":
    main()
    
