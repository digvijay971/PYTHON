a = {'7': ' ', '8': ' ', '9': ' ',
     '4': ' ', '5': ' ', '6': ' ',
     '1': ' ', '2': ' ', '3': ' '}
b = []
def display_board(a):
    print(a['7'] + '|' + a['8'] + '|' + a['9'])
    print('-+-+-')
    print(a['4'] + '|' + a['5'] + '|' + a['6'])
    print('-+-+-')
    print(a['1'] + '|' + a['2'] + '|' + a['3'])
def game():
    turn = 'X'
    for i in range(9):
        display_board(a)
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        if a[move] == ' ':
            a[move] = turn
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
        else:
            print('That space is already occupied. Try again.')
            continue
        if (a['7'] == a['8'] == a['9'] != ' ') or (a['4'] == a['5'] == a['6'] != ' ') or (a['1'] == a['2'] == a['3'] != ' ') or (a['7'] == a['4'] == a['1'] != ' ') or (a['8'] == a['5'] == a['2'] != ' ') or (a['9'] == a['6'] == a['3'] != ' ') or (a['7'] == a['5'] == a['3'] != ' ') or (a['9'] == a['5'] == a['1'] != ' '):
            display_board(a)
            print('Congratulations! ' + turn + ' loses!')
            break
        else:
            display_board(a)
            print('It\'s a tie!')
game()
