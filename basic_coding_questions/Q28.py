'''
You got a summer job at a bakery where you are incharge of the pastry section. Everyday you get n no. of pastries at the bakery.

There is a huge queue for buying pastries. There can be more people than you can serve so some might have to return empty handed.

You are serving each customer one after the another.

Each customer wants some number of pastries.
If you can serve that customer you need to reply with "Enjoy your dessert!".
If you cannot serve them at all, say "Sorry, we are all out!".

'''
n, q = map(int, input().split())

for _ in range(q):
    need = int(input())
    if need <= n:
        print("Enjoy your dessert")
        n = n - need
    else:
        print("Sorry, we are all out!")    