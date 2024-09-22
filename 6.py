import numpy as np

x = np.array([4,3,2,1])
y = np.array([1,2,3,4])

def mnk(x, y):
    X = np.vstack([x, np.ones(len(x))]).T
    
    beta = np.linalg.inv(X.T @ X) @ X.T @ y
    
    return beta[0], beta[1] 

a, b = mnk(x, y)
print(f"Коэффициент наклона a: {a}")
print(f"Свободный член b: {b}")
