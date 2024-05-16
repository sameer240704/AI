# Finding square root of a number

def objective(currObj, target):
    return currObj * currObj - target

def square_number(target=25, epsilon=1e-6, currSol=0.0, max_iter=1000):
    step_size = target / 10  # Initialize step_size to a reasonable value
    
    for _ in range(max_iter):
        currObj = objective(currSol, target)
        
        if abs(currObj) < epsilon:
            return currSol
        
        if currObj > 0:
            currSol -= step_size
        if currObj < 0:
            currSol += step_size
            
        step_size /= 2  # Halve the step_size in each iteration
    
    return currSol
    
def main():
    sq = square_number(target=10)
    print(f"Square Root of the number is : {sq}")
    
if __name__ == "__main__":
    main()