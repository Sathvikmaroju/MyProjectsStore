def get_binary_function(number):
    return bin(number).replace("0b", "")

my_list, cards, lst, enter = [i for i in range(1, 64)], [[], [], [], [], [], []], [], ['start']
my_list.reverse()

for x in my_list:
    lst.insert(my_list.index(x), get_binary_function(x))
for num1 in lst:
    a = list(num1)
    n=len(a)-1
    for i in range(len(a)):
        a[i] = int(a[i])*(2**(n-i))
    for q in a:
        y = lst.index(num1)
        if q == 32:
            cards[5].append(my_list[y])
        elif q == 16:
            cards[4].append(my_list[y])
        elif q == 8:
            cards[3].append(my_list[y])
        elif q == 4:
            cards[2].append(my_list[y])
        elif q == 2:
            cards[1].append(my_list[y])
        elif q == 1:
            cards[0].append(my_list[y])
for i in range(len(cards)):
    cards[i].sort()

print("""Think of a number between 1 and 63.
Type 'start' when you are ready and hit the 'Enter' key.""")
while input().lower() not in enter:
    print("Type 'start' when you are ready and hit the 'Enter' key.")
    a=input()
    print()
valid_entries, num = ['yes', 'no'], 0
for card in cards:
    print(card)
    print("\ntype 'yes' if your number is present in card, if not type 'no' ")
    response=input()
    while response not in valid_entries:
        print("Invalid!")
        print("type 'yes' if your number is present in card, if not type 'no' ")
        response = input()
    print()
    if response == 'yes':
        num+=card[0]

print("The number is", num)