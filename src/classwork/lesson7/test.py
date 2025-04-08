#Игра "Пятнашки"
2.  import random
3.
4.  #Заготовки для отображения поля
5.  up = """+-----+-----+-----+-----+
6.  |     |     |     |     |"""
7.  mid = """|     |     |     |     |
8.  +-----+-----+-----+-----+
9.  |     |     |     |     |"""
10. bot = """|     |     |     |     |
11. +-----+-----+-----+-----+"""
12.
13. def get_new_random():
14.     line = list(range(16))
15.     random.shuffle(line)
16.     return line
17.
18. def print_board(new_game):
19.     print(up)
20.     for i in range (0, 16):
21.         if new_game[i]<10:
22.             if new_game[i] == 0:
23.                 print('| ', end = '')
24.             else:
25.                 print('| '+str(new_game[i])+' ', end = '')
26.         else:
27.             num = str(new_game[i])
28.             print('| '+num[0]+' '+num[1]+' ', end = '')
29.         if i == 3 or i == 7 or i == 11:
30.             print('|')
31.             print(mid)
32.     print('|')
33.     print(bot)
34.
35. def ansver():
36.     while True:
37.         text = input('Введите число от 1 до 15:')
38.         if text.isdigit() == False:
39.             print('Вводите только целые числа!')
40.         elif 15<int(text) or int(text)<0:
41.             print('Нет такого числа на игровом поле!')
42.         else:
43.             return int(text)
44.             False
45.
46. def possible_moves(new_game):
47.     moves = []
48.     ind = new_game.index(0)
49.     if ind == 0:
50.         moves.append(new_game[1])
51.         moves.append(new_game[4])
52.     elif ind == 1:
53.         moves.append(new_game[0])
54.         moves.append(new_game[2])
55.         moves.append(new_game[5])
56.     elif ind == 2:
57.         moves.append(new_game[1])
58.         moves.append(new_game[3])
59.         moves.append(new_game[6])
60.     elif ind == 3:
61.         moves.append(new_game[2])
62.         moves.append(new_game[7])
63.     elif ind == 4:
64.         moves.append(new_game[0])
65.         moves.append(new_game[5])
66.         moves.append(new_game[8])
67.     elif ind == 5:
68.         moves.append(new_game[1])
69.         moves.append(new_game[4])
70.         moves.append(new_game[6])
71.         moves.append(new_game[9])
72.     elif ind == 6:
73.         moves.append(new_game[2])
74.         moves.append(new_game[5])
75.         moves.append(new_game[7])
76.         moves.append(new_game[10])
77.     elif ind == 7:
78.         moves.append(new_game[3])
79.         moves.append(new_game[6])
80.         moves.append(new_game[11])
81.     elif ind == 8:
82.         moves.append(new_game[4])
83.         moves.append(new_game[9])
84.         moves.append(new_game[12])
85.     elif ind == 9:
86.         moves.append(new_game[5])
87.         moves.append(new_game[8])
88.         moves.append(new_game[10])
89.         moves.append(new_game[13])
90.     elif ind == 10:
91.         moves.append(new_game[6])
92.         moves.append(new_game[9])
93.         moves.append(new_game[11])
94.         moves.append(new_game[14])
95.     elif ind == 11:
96.         moves.append(new_game[7])
97.         moves.append(new_game[10])
98.         moves.append(new_game[15])
99.     elif ind == 12:
100.        moves.append(new_game[8])
101.        moves.append(new_game[13])
102.    elif ind == 13:
103.        moves.append(new_game[9])
105.        moves.append(new_game[12])
106.        moves.append(new_game[14])
107.    elif ind == 14:
108.        moves.append(new_game[10])
109.        moves.append(new_game[13])
110.        moves.append(new_game[15])
111.    else:
112.        moves.append(new_game[11])
113.        moves.append(new_game[14])
114.
115.    return moves
116.
117.
118.
119.
120.#основной код игры
121.win = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
122.new_game = get_new_random()
123.print_board(new_game)
124.
125.while True:
126.    moves = possible_moves(new_game)
127.    move_num = ansver()
128.    if move_num in moves:
129.        ind_move = new_game.index(move_num)
130.        ind_0 = new_game.index(0)
131.        new_game[ind_0] = move_num
132.        new_game[ind_move] = 0
133.        print_board(new_game)
134.    else:
135.        print('Это число нельзя переместить!')
136.    if new_game == win:
137.        print('Поздравляю! Вы победили!')
138.        break
139.    else:
140.        None