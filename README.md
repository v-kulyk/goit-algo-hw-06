### DFS шлях:
"Times Square",
"Grand Central",
"Penn Station",
"Central Park West",
"Empire State",
"Rockefeller Center",
"Union Square",
"Columbus Circle",
"Bryant Park",
"Chelsea Market",
"Flatiron District",
"Greenwich Village",
"Brooklyn Bridge",
"Wall Street",
"Battery Park",
"Staten Island Ferry",
"World Trade Center",
"Cortlandt Street",
"Chambers Street",
"Fulton Street",
"Bowling Green",
"Whitehall Street",
"South Ferry",
"Brooklyn Bridge-City Hall",

Алгоритм DFS (глибина) починається з вибраної вершини та продовжує відвідування наступної необхідної вершини, що є
сусідом попередньої, переходячи все глибше у граф, доки не дійде до мертвого кінця, після чого він повертається назад,
щоб знайти необхідні вершини, які ще не були відвідані, і продовжує цей процес, поки не відвідає всі вершини.
Алгоритм DFS можна реалізувати в рекурсивному або ітеративному варіанті.

### BFS шлях:
"Times Square",
"Union Square",
"Grand Central",
"Rockefeller Center",
"Columbus Circle",
"Central Park West",
"Penn Station",
"Flatiron District",
"Empire State",
"Bryant Park",
"Greenwich Village",
"Chelsea Market",
"Brooklyn Bridge",
"Battery Park",
"Wall Street",
"Chambers Street",
"World Trade Center",
"Staten Island Ferry",
"South Ferry",
"Fulton Street",
"Brooklyn Bridge-City Hall",
"Cortlandt Street",
"Whitehall Street",
"Bowling Green",


Алгоритм BFS (ширина) починається з вибраної вершини та відвідує всі її сусідні вершини, перш ніж перейти до сусідів
цих сусідів. BFS продовжує відвідувати вершини в ширину графа, перш ніж переходить глибше.


### Висновок:
Отже, як бачимо, в залежності від вибору алгоритму обходу графа ми отримуємо різний результат. Це пов'язано з тим, що
що різні алгоритм при проході кожної вершини обирають наступну вершину по-різному (в ширину або глибину).