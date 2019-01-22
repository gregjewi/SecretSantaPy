# Title: Secret Santa Pairings Py
# Author: Gregory Ewing
# Date: January 2019
# About: Double-bling matching and send an sms to participants.

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
    
    
nums = dict()
with open('SecretSantaNumbers.csv','r') as f:
    for l in f:
        ids = l.strip().split(',')
#         nums[ids[0]] = '17347094989'
        nums[ids[0]] = ids[1]

    
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'YOUR_TWILIO_ACCOUNT_ID_HERE'
auth_token = 'YOUR_AUTH_TOKEN_HERE'
client = Client(account_sid, auth_token)

for name in final:
    string_to_p = 'Hi {0}! This is the Secret Santa Message Hotline. You are {1}\'s Secret Santa. Merry Merry ho-ho-ho!'.format(name,final[name])
    
    body = string_to_p
    
    message = client.messages \
    .create(
         body=body,
         from_='YOUR TWILIO NUMBER HERE',
         to='+{0}'.format(nums[name])
     )