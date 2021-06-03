import sys

def row_check(arr,ro,val):
    if val in arr[ro]:
        return False
    return True



def col_check(arr,col,val):
    for i in range(9):
        if arr[i][col]==val:
            return False
    return True


def sq_check(arr,row,col,val):
    #print(row,col,row//3,row//3+3,val)
    for i in range((row//3)*3,(row//3)*3+3):
        for j in range((col//3)*3,(col//3)*3+3):
            #print( (row // 3)*3, (row // 3)*3 + 3, (col//3)*3,(col//3)*3+3,i,j,val)
            if arr[i][j]==val:
                #print(row, col, row // 3, row // 3 + 3,col//3,col//3+3,i,j, val)
                #print(1)
                return False
    return True


def printing_game(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j],end = " ")
        print()


def sudoku(arr,i,j,re):

    if i==9 and j ==0:
        printing_game(arr)
        re=1
        sys.exit()
        return

    #printing_game(arr)
    #print()

    if arr[i][j]==0:
        #print(i, j)
        for val in range(1,10):
            #print(val)

            if row_check(arr,i,val) and col_check(arr,j,val) and sq_check(arr,i,j,val):
                #print(i,j)
                arr[i][j]=val
                if j==8:
                    sudoku(arr,i+1,(j+1)%9,re)

                else:
                    sudoku(arr, i , (j + 1) % 9,re)
                if re == 1:
                    return

                arr[i][j] = 0
    else:
        if j == 8:
            sudoku(arr, i + 1, (j + 1) % 9, re)

        else:
            sudoku(arr, i, (j + 1) % 9, re)
    return

def main():
    arr = []
    for i in range(9):
        lst = list(map(int,input().split()))
        arr.append(lst)
    #print(arr)
    sudoku(arr,0,0,0)


main()



'''
1.If value is not present   D
2.if it is last of the row  D
3.if it is end of the arr
'''