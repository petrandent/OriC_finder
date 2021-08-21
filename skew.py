import matplotlib.pyplot as plt

genome1=open("pg.txt")
genome_text=""
for i in genome1:
    genome_text+=i
genome1.close

y=0
skew_array=[]

for i in genome_text:
    if i=="G":
        y+=1
    elif i=="C":
        y-=1
    else:
        continue
    skew_array.append(y)

x_axis=list(range(len(skew_array)))

print(len(x_axis))
plt.plot(x_axis,skew_array)
plt.show()



