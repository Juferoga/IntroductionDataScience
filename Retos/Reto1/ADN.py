import numpy as np
import pandas as pd

dna = np.array([[np.random.randint(0, 3, 5)], [np.random.randint(0, 3, 5)], [np.random.randint(0, 3, 5)]])
#print(dna)

df = pd.DataFrame( data = {'posicionx':  [0, 0, 0], 'posiciony':  [0, 0, 0], 'valoresRepetidos': [0, 0, 0], 'acumulador': [0, 0, 0]})
# print(df)

#print(df.loc[0,'posicionx'])

for x in range(5):
    
    if dna[0, 0, x] == dna[1, 0, -(x+1)] and dna[2, 0, x] == dna[1, 0, -(x+1)]:
        df.loc[0,'acumulador'] = df.loc[0,'acumulador'] + 1
        df.loc[0,'posicionx'] = x
        df.loc[0,'posiciony'] = 0
        print('1  2  3')
        print('1  2  3')
        print(dna[0, 0, x], dna[1, 0, -(x+1)], dna[2, 0, x])
    
    elif dna[0, 0, x] == dna[1, 0, -(x+1)] and dna[2, 0, x] != dna[1, 0, -(x+1)]:
        df.loc[0,'acumulador'] = df.loc[0,'acumulador'] + 1
        df.loc[0,'posicionx'] = x
        df.loc[0,'posiciony'] = 0
        print('1  2  3')
        print(dna[0, 0, x], dna[1, 0, -(x+1)], dna[0, 0, x])
    
    elif dna[0, 0, x] != dna[1, 0, -(x+1)] and dna[2, 0, x] == dna[1, 0, -(x+1)]:
        df.loc[0,'acumulador'] = df.loc[0,'acumulador'] + 1
        df.loc[0,'posicionx'] = x
        df.loc[0,'posiciony'] = 0
        print('1  2  3')
        print(dna[0, 0, x], dna[1, 0, -(x+1)], dna[0, 0, x])
        
    #elif dna[0, 0, x] != dna[1, 0, -(x+1)] and dna[2, 0, x] == dna[1, 0, -(x+1)]:
        
    else:
        print('No matches in', x, -(x+1))

print(df)
print (dna)


    # for x in range(50):
    #     if dna[0, 0, x+2] == dna[1, 0, -(x+1)] and dna[0, 0, x] == dna[1, 0, -(x+1)]:
    #         a = a + 1
    #         print(a)
    #     elif dna[0, 0, x+x] == dna[1, 0, -(x+1)] and dna[0, 0, x] != dna[1, 0, -(x+1)]:
    #         a = a + 1
    #         print(a)
    #
    # for x in range(50):
    #     if dna[0, 0, x] == dna[1, 0, -(x+1)] and dna[0, 0, x] == dna[1, 0, -(x+1)]:
    #         a = a + 1
    #         print(a)
    #     elif dna[0, 0, x] == dna[1, 0, -(x+1)] and dna[0, 0, x] != dna[1, 0, -(x+1)]:
    #         a = a + 1
    #         print(a