# Create function, that will take optional argument n,
# and will return chessboard on the side of given argument.
# Default value of n = 8 (standard chessboard size).
# Function should draw chessboard composed of '#' signs and ' ' - spation.


def chessboard(n=8):
    for row in range(0,n):
        if row % 2 == 0:
            line = ''
            for col in range(0,n):
                if col % 2 == 0:
                    line += ' '
                else:
                    line += '#'
            print(line)
        else:
            line = ''
            for col in range(0, n):
                if col % 2 == 0 :
                    line += '#'
                else:
                    line += ' '
            print(line)

    text = 'Here is your {}x{} chessboard! '.format(n, n)
    return text
 
# print(chessboard(17))
# print(chessboard(4))
