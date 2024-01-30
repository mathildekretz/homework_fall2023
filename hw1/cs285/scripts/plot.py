import matplotlib.pyplot as plt

X1 = [1000, 10000, 100, 500, 10, 50, 300, 700]
X2 = [500, 80, 50, 10, 1000, 20, 30]
Y1 = [4726, 4724, 665, 4035, 923, 597, 851, 4172]
Y2 = [4650, 4172, 3726, 621, 4679, 743, 3936]

# plt.scatter(X2, Y2, marker='+', label='Evaluation values')
# plt.axhline(y=4681, color='r', label='Initial value')
# #plt.xlabel('Number of Gradient steps for training policy')
# plt.xlabel('Train batch size')
# plt.ylabel('Evaluation Average Return')
# plt.xscale('log')
# plt.legend()
# plt.title('Evolution of the return depending on the training batch size')
# plt.show()

steps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dag_ant = [4727, 4540, 4714, 4737, 4722, 4681, 4675, 4733, 4704, 4658]
std_ant = [104.9, 76.26, 86.04, 93.60, 97.60, 83.61, 102.10, 122.80, 93.96, 117.40]
dag_hop = [1164, 1446, 3168, 3690, 3456, 3699, 3724, 3708, 3721, 3722]
std_hop = [224.60, 200, 825.38, 17.17, 481.90, 5.25, 5.80, 3.75, 3.73, 3.87]

plt.errorbar(steps, dag_hop, yerr=std_hop, color='teal', marker='o', label='Dagger training on Hopper task')
plt.axhline(y = 3717, color ='hotpink', label='Initial value')
plt.axhline(y= 1116, color='slateblue', label='BC result')
plt.xlabel('Steps')
plt.ylabel('Evaluation Average Return')
plt.legend()
plt.title('Analysis of the Dagger training')
plt.savefig('DaggerHop1.png')
plt.clf()

plt.errorbar(steps, dag_ant, yerr=std_ant, color='teal', marker='o', label='Dagger training on Ant task')
plt.axhline(y = 4681, color ='hotpink', label='Initial value')
plt.axhline(y= 4726, color='slateblue', label='BC result')
plt.xlabel('Steps')
plt.ylabel('Evaluation Average Return')
plt.legend()
plt.title('Analysis of the Dagger training')
plt.savefig('DaggerAnt1.png')