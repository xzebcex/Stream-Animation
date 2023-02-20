# Matrix Stream Animation
import random
import shutil
import sys
import time
import bext

# Constants:
MIN_LENGTH = 3
MAX_LENGTH = 7

PAUSE = 0.3
STREAM_CHAR = ['0', '1',]

# The density can range between 0.0 and 1.0.
Density = 0.02

# Terminal window dimensions.
WIDTH = shutil.get_terminal_size()[0]

# On Windows, we can't print to the last column without it adding a newline,
# so lower the width by one:WIDTH -= 1

bext.fg('green')
print('\nWelcome to The Matrix.')
bext.fg('red')
print('Pres ctrl-c to exit.')

time.sleep(2)

try:
    # When the counter for each column is 0, no stream is displayed. Otherwise,
    # it serves as a counter to determine how many times a 1 or 0 should appear in that column:
    columns = [0]*WIDTH
    while True:
        # Set up the counter for each column as follows:
        for i in range(WIDTH):
            if columns[i] == 0:
                bext.fg('green')  # add green color
                if random.random() <= Density:
                    # Resume this column's stream:
                    columns[i] = random.randint(MIN_LENGTH, MAX_LENGTH)

            # Resume this column's stream. Show a blank space or a 1/0 character.
            if columns[i] > 0:
                print(random.choice(STREAM_CHAR), end='')
            else:
                print(' ', end='')
        print()
        # Check that the following text appears on the screen:
        sys.stdout.flush()
        time.sleep(PAUSE)

except KeyboardInterrupt:
    sys.exit()  # When ctrl-c is pressed, end the program:
