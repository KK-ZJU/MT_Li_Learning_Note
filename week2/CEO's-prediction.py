import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from mpl_toolkits.mplot3d import axes3d,Axes3D
import numpy as np
from gradientDescent import *

def plot_data(x,y):
    plt.plot(x,y,'*r')
    plt.xlabel("people number")
    plt.ylabel("profit")
    plt.show()

print('Plotting Data...')
data = np.loadtxt('street&profits.txt',delimiter=',',usecols=(0,1))
x = data[:,0]
y = data[:,1]
m = y.size
plot_data(x,y)

#input('Program paused.please Enter to continue')



print('Running Gradient Descent...')

x = np.c_[x,np.ones(m)]
theta = np.zeros(2)

iterations = 1500
alpha = 0.01

print('Initial cost : ' + str(compute_cost(x,y,theta)) + 'the value should be about 32.07')

theta,J_Hisory = gradient_descent(x,y,theta,alpha,iterations)

print('Theta found by gradient descent: ' + str(theta.reshape(2)))






plt.figure(0)
line1,= plt.plot(x[:,0],np.dot(x,theta))
plt.legend(handles=[line1])                      ### ???
plot_data(data[:,0],data[:,1])

predict1 = np.dot(np.array([3.5,1]),theta)
print("For population = 35000,we predict a profit of {:0.3f}(this value should be about 4519.77)".format(predict1 * 10000))
predict2 = np.dot(np.array([7,1]),theta)
print("For population = 70000,we predict a profit of {:0.3f}(this value should be about 45342.45)".format(predict1 * 10000))







print('Vasualizing J(theta0,theta1)...')

theta0_vals = np.linspace(-10,10,100)
theta1_vals = np.linspace(-1,4,100)

xs,ys = np.meshgrid(theta0_vals,theta1_vals)
J_vals = np.zeros(xs.shape)

for i in range(theta0_vals.size):
    for j in range(theta1_vals.size):
        t = np.array([theta0_vals[i],theta1_vals[j]])
        J_vals[i][j] = compute_cost(x,y,t)

J_vals = np.transpose(J_vals)

fig1 = plt.figure(1)
ax = fig1.gca(projection='3d')
ax.plot_surface(xs,ys,J_vals)
plt.xlabel(r'$\theta_0$')
plt.ylabel(r'$\theta_1$')
plt.show()

plt.figure(2)
lvls = np.logspace(-2,3,20)
plt.contour(xs,ys,J_vals,levels=lvls,norm=LogNorm())
plt.plot(theta[0],theta[1],c='r',marker='x')
plt.show()

input('ex1 Finished.Press ENTER to exit')
