import sys
from collections import Counter

input=sys.stdin.readline

n=int(input())

cards=list(map(int,input().split()))

card_counter=Counter(cards)

m=int(input())
my_cards=list(map(int,input().split()))

for card in my_cards:
    print(card_counter[card],end=" ")