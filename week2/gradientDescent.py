import numpy as np

def compute_cost(X,y,theta):
    num = y.size
    cost = np.sum((np.dot(X,theta)-y)**2) / (2 * num)
    return cost

    # for i in range(num):
    #     cost += (np.sum(X[i] * theta) - y[i])**2
    # return cost

# def gradient_comput(X,y,theta,num):
#     N = y.size()
#     gradient = 0.0
#     for i in range(N):
#         gradient += (y - X[i] * theta)*

def gradient_descent(X,y,theta,alpha,num_iters):
    J_history = np.zeros(num_iters)
    num = y.size
    num_w = theta.size

    for i in range(num_iters):
        for j in range(num_w):
            theta[j] = theta[j] - alpha * np.sum((np.dot(X,theta) - y) * X[:,j]) / num

        J_history[i] = compute_cost(X,y,theta)

    return theta,J_history