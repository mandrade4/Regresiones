import random
import matplotlib.pyplot as plt
import os.path
import numpy as np

class RL:
    
    thts = [random.random(),random.random(),random.random(),random.random(),random.random()]
    umbral = 0.01
    alfa = 0.005
    error = 0
    x = np.array([[1, 5, 7, 3, 9],
                [1, 1, 3, 4, 5],
                [1, 2, 1, 6, 4],
                [1, 3, 8, 7, 6],
                [1, 4, 2, 3, 7],
                [1, 5, 8, 2, 8]])
    y = []
    cte = 2*len(y)

    def __init__(self, yy):
        # self.x = xx
        self.y = yy


    def prints(self):
        for i in range(len(self.x)):
            print ('\n')
            for j in range(len(self.x[i])):
                print(self.x[i][j])

    # ECUACION

    def H(self):
        arreglo=[]
        for i in range(len(self.x)):
            arreglo.append(np.dot(self.x[i],self.thts))
        return arreglo
            
        # for e in zip(self.thts,self.x):
        #     t = t + e[0]*e[1]
        # return [sum(e[0]*e[1] for e in zip(self.thts,self.x))]
    
    # ERROR modificada para que sea REGULARIZACION
    def Error(self):

        # H2 = zip(self.y, self.H())
        # error = sum((e[0]-e[1]) for e in H2)**2 / (2*len(self.y))
        # return error

        error = sum ( [ (e[0]-e[1])**2 for e in zip(self.y, self.H())]) / (2*len(self.y))
        reg =  sum([(self.cte*e*e)**2 for e in self.thts]) / (2*len(self.y)) 
        total  = error + reg
        
        return total


    # Cambiar valores de tta
    def changeTheta(self):
        sum =0
        for j in range(len(self.thts)):
            for i in range(len(self.y)):
                sum=sum+((self.y[i]-self.H()[i])*(-1*self.x[j][i]))
            self.thts[j] = self.thts[j]-self.alfa*sum
            
        # temp = self.thts
        # thetai=0
        # computando = sum([(e[0]-e[1])**2 for e in zip(self.y,self.H())]) / (2*len(self.y))
        # for e in range(len(self.thts)):
        #     for i in range(len(self.x)):
        #         thetai=self.alfa*(computando)+((self.cte*x[i])/len(self.y))
        #         print(thetai)
        # # return thetai

    def graficar(self, cont):
       
        plt.scatter(self.x, self.y)
        plt.plot(self.x, self.H(), color="red")
        out_path = os.path.join('D:\imagenes\ia2', str(cont) + '.png')
        plt.savefig(out_path)
        plt.close()

        # plt.savefig(str(cont)+".png")
        # plt.close()

     #    plt.plot(self.x,self.y,'.')
     #    plt.plot(self.x,self.H(),'-')

     #    plt.savefig(str(cont)+".png")
     #    plt.show()

    
    def entrenar(self):
        # plt.scatter(self.x, self.y)
        
        # print("entrenar")
        # print(self.x)
        # print(self.y)
        tmp = 0
        # self.graficar(tmp)
        err = self.Error()
       
        while(err > self.umbral):
            self.changeTheta()
            err = self.Error()
            print(err)
            tmp = tmp+1
            # if(tmp % 20 == 0 or tmp < 40):
            #     self.graficar(tmp)
                

# Creacion de puntos aleatorio
# x =[1]+ [random.randint(0, 10) for _ in range(9)]
y = [random.randint(0, 10) for _ in range(5 )]

a = RL(y)
a.entrenar()
# print(a.changeTheta())
