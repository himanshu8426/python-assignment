"""
PROGRAM ---45---
A certain childrens game involves starting with a word in a particular category. Each participant in turn says a word, but that word must begin with the final letter of the previous word. Once a word has been given, it cannot be repeated. If an opponent cannot give a word in the category, they fall out of the game. For example, with "animals" as the category,

Child 1: dog 
Child 2: goldfish
Child 1: hippopotamus
Child 2: snake
...
Your task in this exercise is as follows: Take the following selection of 70 English Pokemon names (extracted from Wikipedia's list of Pokemon) and generate the/a sequence with the highest possible number of Pokemon names where the subsequent name starts with the final letter of the preceding name. No Pokemon name is to be repeated.

audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon
cresselia croagunk darmanitan deino emboar emolga exeggcute gabite
girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan
kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine
nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2
porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking
sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko
tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask
"""
with open("45.txt") as file_object:
    list_of_pokemon = []
    list_of_pokemon.extend(file_object.read().split())
def recur(pokemon,list_of_pokemon,count):
    count +=1
    copy_list_of_pokemon = list_of_pokemon[:]
    copy_list_of_pokemon.remove(pokemon)
    list_count = []
    for next_pokemon in copy_list_of_pokemon:
        if pokemon[-1] == next_pokemon[0]:
            list_count.append(recur(next_pokemon,copy_list_of_pokemon,count))
    if len(list_count)==0:
        return count
    ans = max(list_count)
    list_count=[]
    return ans	

def ans(list_of_pokemon):
    count = 0
    maxcount = 0
    for pokemon in list_of_pokemon:
        count = recur(pokemon,list_of_pokemon,count)
        if count > maxcount:
            maxcount = count
        count =0
    print maxcount		

ans(list_of_pokemon)
