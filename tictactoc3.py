#!/usr/bin/python3
# coding=utf8
'''
proud to write a python 2/3 portable code... # no it's an illusion, a Hallucination. input() in 3 is raw_input() in 2.
@author SnowOnion
'''

chars=[' ','x','o']
names=['Noman','Player 1', 'Player A']


def printBoard(mat):
    print(
        '''%s|%s|%s
-+-+-
%s|%s|%s
-+-+-
%s|%s|%s'''%tuple(matrix[1:]))

def printPrompt(pNum):
    while True:
        inp=input(names[pNum]+', your choice(1~9): ')
        try:
            cho=int(inp)
            if cho not in range(1,10):
                raise ValueError()
            if matrix[cho]==chars[0]:
                matrix[cho]=chars[pNum]
                for ind in magicListener[cho]:
                    magicTable[ind][pNum-1]+=1
                break
            else:
                print('Place %d is held. Choose another.'%(cho))
        except (ValueError,NameError): # NAN || not in [1,9]
            print('Invalid value. Please input integer from 1 to 9.')

'''
return: 1 if p1 win, 2 if p2 win, 0 if no one win
'''
def checkWinning(mat):
    # 8 cases. The knowledge should be memorized, thus learning from history become possible.
    for magic in magicTable:
        if magic[0]==3:
            return 1
        if magic[1]==3:
            return 2
    return 0

def checkFull(mat):
     return chars[0] not in mat[1:] # matrix[0] ===' ' >_<


if __name__=='__main__':
    # Directly store the char to display. flattened, indexed from 1 to 9.
    matrix=[chars[0] for i in range(10)]
    

    # [[1,1],[2,0],...,[0,3]] := 1'x' & 1'o' in row 1, 2'x' & 0'o' in row 2,..., 0'x' & 3'o' in backslash(\) diagonal.
    # 1~8 is: row1, row2, row3(up-down), col1, col2, col3(left-right), 'slash'(/) diagonal, 'backslash'(\) diagonal.
    magicTable=[[0,0] for i in range(9)] # indexes start from 1~
    
    # store "the lines that go across this grid". Indexes start from 1~
    magicListener=[[],
                   [1,4,8],[1,5],[1,6,7],
                   [2,4],[2,5,7,8],[2,6],
                   [3,4,7],[3,5],[3,6,8]]

    # each player move, turn++
    turn=1

    while True:
        printBoard(matrix)
        printPrompt(2-(turn%2)) # p1,p2,p1,p2,...

        winner=checkWinning(matrix)
        if winner>0:
            printBoard(matrix)
            print('Result: '+names[winner]+' wins!')
            break
        else:
            if checkFull(matrix):
                printBoard(matrix)
                print('Result: Draw game~')
                break
            else:
                turn+=1
