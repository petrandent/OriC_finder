import matplotlib.pyplot as plt


def opposite_strand(dna_string):
    """returns the opposite strand in a 5 --> 3 direction"""
    opposite=""
    for i in dna_string:
        if i=="A":
            opposite="T"+opposite
        if i=="G":
            opposite="C"+opposite
        if i=="C":
            opposite="G"+opposite
        if i=="T":
            opposite="A"+opposite
    return opposite

def hamming(text1,text2):
    """calculates hamming distance between 2 texts of equal length, if not equal it throws an error"""
    distance=0
    if len(text1)!=len(text2):
        return "Error"
    else:
        for i in range(len(text1)):
            if text1[i]!=text2[i]:
                distance+=1
            else:
                continue
    return distance

def distant_pattern_count(text,pattern,d=1):
    """counts patterns with distance=1 from exact pattern"""
    count=0
    for i in range(len(text)-len(pattern)+1):
        if hamming(pattern,text[i:(i+len(pattern))])<2:
            count+=1
        else:
            continue
    return count

def most_frequent_kmer(text,k=9):
    """returns a dictionary with key the most frequent kmer and value the number of times it appears"""
    kmers={}
    for i in range(len(text)-k+1):
        subpattern=text[i:(i+k)]
        if subpattern in kmers:
            kmers[subpattern]+=1
        else:
            kmers[subpattern]=1
    maximum_value=max(kmers.values())
    frequent_kmers={}
    for key,v in kmers.items():
        if v==maximum_value:
            frequent_kmers[key]=v
        else:continue
    return frequent_kmers


genome1=open("pg.txt")
genome_text=""
for i in genome1:
    genome_text+=i
genome1.close
genome_text=genome_text.upper()

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


#3 positions of 500 bps
position1=minimum_position-500
position2=minimum_position
position3=minimum_position+500

string1=genome_text[position1:position1+500]
string2=genome_text[position2:position2+500]
string3=genome_text[position3:position3+500]

#testing
a=most_frequent_kmer("aaaattattatattttttaaaaa",2)
print(a)

