import pandas as pd
import matplotlib.pyplot as plt
print("YO")
archivo_excel = pd.read_excel('C:/Users/USUARIO/Desktop/Python/roberto.xlsx')
plt.xticks([]), plt.yticks([])
plt.imshow(archivo_excel, cmap='gray', interpolation='bicubic')
plt.show()
print("------------------------------------------------------------------------")
print("Bob Marley")
archivo_excel = pd.read_excel('C:/Users/USUARIO/Desktop/Python/bob.xlsx')
plt.xticks([]), plt.yticks([])
plt.imshow(archivo_excel, cmap='gray', interpolation='bicubic')
plt.show()