'''
2. Feladat
A program generáljon 5 egész számot [0;10] intervallumon, tárolja egy halmazban. 
A felhasználónak meg kell próbálni kitalálni ezeket, olyan módon, hogy megad 5 számot, melyeket szintén halmazban tárol a gép. 
A program tájékoztassa a felhasználót, a következőkről: hány darab számot talált el, és melyek ezek; hány számot nem talált el, és melyek ezek; mely számok kerültek rögzítésre a generálás vagy a felhasználó miatt; mely számok nem szerepeltek egyik halmazban sem!
'''
from random import randint
#szamgeneralas
osszes = set([i for i in range(11)])
egeszek = set()
while len(egeszek)<5:
   egeszek.add(randint(0,10)) 
    
#felhasznaloszamok
    
felhszam = set([int(input('adj egy szamot 0 és 10 között (ne ismétlődjön): ')) for i in range(5)])

#lógika
eltalalt = set(egeszek & felhszam)
nemtalalt = set(egeszek - felhszam)



print(f'\n ezeket a a szamokat talaltad el: {eltalalt}\n eltalalt szamok szama: {len(eltalalt)}')

print(f'ezeket a szamokat nem talaltad el: {nemtalalt} \n nem talalt szamok szama: {len(nemtalalt)}')

rogzitett = set(eltalalt | nemtalalt )
print(f'Rögzítésre került számok: {rogzitett}')

egyikbensem = ( osszes - rogzitett )
print(f'nem szerepel egyikben sem: {egyikbensem}')