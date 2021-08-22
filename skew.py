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
        y=y
    skew_array.append(y)

x_axis=list(range(len(skew_array)))

minimum_skew=min(skew_array)
minimum_position=skew_array.index(minimum_skew)
print(minimum_position)



#skey plot
#plt.xlabel("position")
#plt.ylabel("skew")
#plt.title("Skew diagram")
#plt.plot(x_axis,skew_array)
#plt.show()

def most_frequent_kmer(text,k=9):
    kmers={}
    for i in range(len(text)-k+1):
        subpattern=text[i:(i+k)]
        if subpattern in kmers:
            kmers[subpattern]+=1
        else:
            kmers[subpattern]=1
    maximum_value=max(kmers.values())
    frequent_kmers=[]
    for key,v in kmers.items():
        if v==maximum_value:
            frequent_kmers.append(key)
        else:continue
    return frequent_kmers

#testing
a=most_frequent_kmer("aaaattattatattttttaaaaa",2)
print(a)
