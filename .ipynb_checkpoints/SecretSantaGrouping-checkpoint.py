import random as r

def choose(options):
    rands = [r.random() for i in options]
    rank = {}
    for rand,p in zip(rands,options):
        rank[rand] = p
    
    options = sorted(rank)
    
    return rank[options[0]]

def remove_name(a,possible):
    for p in possible:
        possible[p] = [i for i in possible[p] if i != a[1]]
        
possible = dict()
final = dict()

with open('SecretSanta.csv','r') as f:
    for l in f:
        l = l.strip().split(',')
        possible[l[0]] = [i for i in l[1:] if i != '']
        
# make list of random numbers
rands = [r.random() for i in possible]

# Assign these random numbers to people as keys
rank = {}
for rand,p in zip(rands,possible):
    rank[rand] = p
    
for i in sorted(rank):
    a =( rank[i] , choose(possible[rank[i]]) )
    print(a)
    
    final[a[0]] = a[1]
    remove_name(a,possible)