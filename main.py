import matplotlib.pyplot as plt         #Importerar bibliotek
import numpy as np

X =  [x for x in range(1,101)]   #Våra listor
Y = [(x*2 + np.random.randint(30)) for x in X]        # Y = 2X + randomness



k = 0
m = 0
error = 0
De_Dk = 0        #Definerar funktioner
De_Dm = 0
learning_rate = float(input("Hur hög learning rate? ")) # Om du har 100 mätvärden så är en learning rate på 0.0001 rekommenderat, och iterationer ungefär 50 000. Men om du bara har 8 mätvärden får du bäst nogrannhet med learning rate 0.01 och iterationer 6000 eller learning rate 0.001 och iterationer 60 000
iterationer = int(input("Hur många gånger vill du anpassa funktionen? ")) # Ju fler mätvärden desto lägre learning rate måste du ha. Om du minskar learning raten mycket måste du även öka iterationerna. Tänk på att för stor learning rate gör att programmet kraschar och den mest optimala learning raten är den högsta du kan ha utan att det kraschar.
def function(x):
    return k*x + m

for i in range(iterationer):
    for x, y in zip(X, Y):
        error += abs(y - function(x))
        De_Dk += -x * (y - function(x))
        De_Dm += -1 * (y - function(x))
    error /= len(X)
    De_Dk *= (2 / len(X))
    De_Dm *= (2 / len(X))
    k -= De_Dk * learning_rate
    m -= De_Dm * learning_rate
    print(error)
    error = 0

plt.scatter(X,Y, color = "red", s = 50)
plt.plot(list(range(0, len(X))), [function(x) for x in range(0, len(X))], color = "b")
plt.show()
print (k,m)