'''def ascending(order_square, top_left_number):
    """If order_square > top_left_number"""
    rows_counter = 0
    for rows in range(1, order_square + 1):
        latin_number = top_left_number + (rows - 1)
        if latin_number > order_square:
            latin_number = 1 + rows_counter
            rows_counter += 1
        row_counter = 0
        for row in range(1, order_square + 1):
            print(latin_number)
            latin_number += 1
            if latin_number > order_square:
                latin_number = 1 + row_counter
                row_counter += 1
        print
 
def descending(order_square, top_left_number):
    """If order_square < top_left_number"""
    rows_counter = 1
    for rows in range(1, order_square + 1):
        latin_number = top_left_number - (rows - 1)
        for row in range(1, order_square + 1):
            print latin_number,
            latin_number -= 1
            if latin_number <= (top_left_number - order_square):
                latin_number = top_left_number
        print
 
def main():
    """Main program"""
    order_square = input('Please input the order of the square: ')
    if order_square > 9:
        order_square = input('Please enter a order between 1 -9: ')
    top_left_number = input('Please input the top left number: ')
    if top_left_number > 9:
        top_left_number = input('Please enter a top left between 1 - 9: ')
    counter = top_left_number
    print "The Latin Square is:"
    if order_square >= top_left_number:
        ascending(order_square, top_left_number)
    else:
        descending(order_square, top_left_number)
         
if __name__ == '__main__':
    main()'''
    
T = int(input())
for i in range(1,T+1):
    n,sum = input().strip().split()
    n = int(n)
    sum = int(sum)
    k = 'POSSIBLE'
    if n==2:
        if sum==2:
            print("Case #{}: {}".format(i,k))
            print('1 2\n2 1')
        elif sum==4:
            print("Case #{}: {}".format(i,k))
            print('2 1\n1 2')
        else:
            k = 'IMPOSSIBLE'
            print("Case #{}: {}".format(i,k))
    elif n==3:
        if sum==3:
            print("Case #{}: {}".format(i,k))
            print('1 2 3\n3 1 2\n2 3 1')
        elif sum==6:
            print("Case #{}: {}".format(i,k))
            print('2 3 1\n1 2 3\n3 1 2')
        elif sum==9:
            print("Case #{}: {}".format(i,k))
            print('3 1 2\n2 3 1\n1 2 3')
        else:
            k = 'IMPOSSIBLE'
            print("Case #{}: {}".format(i,k))
    elif n==4:
        if sum==4:
            print("Case #{}: {}".format(i,k))
            print('1 2 3 4\n4 1 2 3\n3 4 1 2\n2 3 4 1')
        elif sum==6:
            print("Case #{}: {}".format(i,k))
            print('1 2 3 4\n2 1 4 3\n3 4 2 1\n4 3 1 2')
        elif sum==7:
            print("Case #{}: {}".format(i,k))
            print('1 3 4 2\n2 1 3 4\n3 4 2 1\n4 2 1 3')
        elif sum==8:
            print("Case #{}: {}".format(i,k))
            print('2 3 4 1\n1 2 3 4\n4 1 2 3\n3 4 1 2')
        elif sum==9:
            print("Case #{}: {}".format(i,k))
            print('2 4 3 1\n1 2 4 3\n4 3 1 2\n3 1 2 4')
        elif sum==10:
            print("Case #{}: {}".format(i,k))
            print('1 4 3 2\n4 1 2 3\n3 2 4 1\n2 3 1 4')
        elif sum==11:
            print("Case #{}: {}".format(i,k))
            print('3 4 2 1\n1 3 4 2\n4 2 1 3\n2 1 3 4')
        elif sum==12:
            print("Case #{}: {}".format(i,k))
            print('3 4 1 2\n2 3 4 1\n1 2 3 4\n4 1 2 3')
        elif sum==13:
            print("Case #{}: {}".format(i,k))
            print('2 4 1 3\n4 3 2 1\n3 1 4 2\n1 2 3 4')
        elif sum==14:
            print("Case #{}: {}".format(i,k))
            print('3 4 1 2\n4 3 2 1\n1 2 4 3\n2 1 3 4')
        elif sum==16:
            print("Case #{}: {}".format(i,k))
            print('4 1 2 3\n3 4 1 2\n2 3 4 1\n1 2 3 4')
        else:
            k = 'IMPOSSIBLE'
            print("Case #{}: {}".format(i,k))
    elif n==5:
        if sum==5:
            print("Case #{}: {}".format(i,k))
            print('1 2 3 4 5\n5 1 2 3 4\n4 5 1 2 3\n3 4 5 1 2\n2 3 4 5 1')
        elif sum==7:
            print("Case #{}: {}".format(i,k))
            print('1 5 2 3 4\n2 1 4 5 3\n3 2 1 4 5\n4 3 5 2 1\n5 4 3 1 2')
        elif sum==8:
            print("Case #{}: {}".format(i,k))
            print('2 5 1 3 4\n1 2 4 5 3\n3 1 2 4 5\n4 3 5 1 2\n5 4 3 2 1')
        elif sum==9:
            print("Case #{}: {}".format(i,k))
            print('1 5 3 2 4\n3 1 4 5 2\n2 3 1 4 5\n4 2 5 3 1\n5 4 2 1 3')
        elif sum==10:
            print("Case #{}: {}".format(i,k))
            print('2 3 4 5 1\n1 2 3 4 5\n5 1 2 3 4\n4 5 1 2 3\n3 4 5 1 2')
        elif sum==11:
            print("Case #{}: {}".format(i,k))
            print('1 5 4 3 2\n4 1 2 5 3\n3 4 1 2 5\n2 3 5 4 1\n5 2 3 1 4')
        elif sum==12:
            print("Case #{}: {}".format(i,k))
            print('2 5 3 1 4\n3 2 4 5 1\n1 3 2 4 5\n4 1 5 3 2\n5 4 1 2 3')
        elif sum==13:
            print("Case #{}: {}".format(i,k))
            print('3 5 2 1 4\n2 3 4 5 1\n1 2 3 4 5\n4 1 5 2 3\n5 4 1 3 2')
        elif sum==14:
            print("Case #{}: {}".format(i,k))
            print('4 5 1 3 2\n1 4 2 5 3\n3 1 4 2 5\n2 3 5 1 4\n5 2 3 4 1')
        elif sum==15:
            print("Case #{}: {}".format(i,k))
            print('3 4 5 1 2\n2 3 4 5 1\n1 2 3 4 5\n5 1 2 3 4\n4 5 1 2 3')
        elif sum==16:
            print("Case #{}: {}".format(i,k))
            print('4 5 2 3 1\n2 4 1 5 3\n3 2 4 1 5\n1 3 5 2 4\n5 1 3 4 2')
        elif sum==17:
            print("Case #{}: {}".format(i,k))
            print('3 5 4 1 2\n4 3 2 5 1\n1 4 3 2 5\n2 1 5 4 3\n5 2 1 3 4')
        elif sum==18:
            print("Case #{}: {}".format(i,k))
            print('4 5 3 1 2\n3 4 2 5 1\n1 3 4 2 5\n2 1 5 3 4\n5 2 1 4 3')
        elif sum==19:
            print("Case #{}: {}".format(i,k))
            print('3 4 5 1 2\n5 3 2 4 1\n1 5 3 2 4\n2 1 4 5 3\n4 2 1 3 5')
        elif sum==20:
            print("Case #{}: {}".format(i,k))
            print('5 1 2 3 4\n4 5 1 2 3\n3 4 5 1 2\n2 3 4 5 1\n1 2 3 4 5')
        elif sum==21:
            print("Case #{}: {}".format(i,k))
            print('5 4 3 1 2\n3 5 2 4 1\n1 3 5 2 4\n2 1 4 3 5\n4 2 1 5 3')
        elif sum==22:
            print("Case #{}: {}".format(i,k))
            print('4 3 5 1 2\n5 4 2 3 1\n1 5 4 2 3\n2 1 3 5 4\n3 2 1 4 5')
        elif sum==23:
            print("Case #{}: {}".format(i,k))
            print('5 3 4 1 2\n4 5 2 3 1\n1 4 5 2 3\n2 1 3 4 5\n3 2 1 5 4')
        elif sum==25:
            print("Case #{}: {}".format(i,k))
            print('5 1 2 3 4\n4 5 1 2 3\n3 4 5 1 2\n2 3 4 5 1\n1 2 3 4 5')
        else:
            k = 'IMPOSSIBLE'
            print("Case #{}: {}".format(i,k))