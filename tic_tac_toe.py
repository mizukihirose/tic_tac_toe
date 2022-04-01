def display(rows):
  for i in rows:
    print(i)


def tick(rows, num, side):
  if num <= 3:
    rows[0][num - 1] = side
  elif num <= 6:
    rows[1][num - 4] = side
  elif num <= 9:
    rows[2][num - 7] = side
  else:
    pass

  return(rows)


def check_is_won(rows, side):
  positions = []

  win_patterns = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,4,7],
    [2,5,8],
    [3,6,9],
    [1,5,9],
    [3,5,7],
  ]

  row1 = rows[0]
  row2 = rows[1]
  row3 = rows[2]

  for index, item in enumerate(row1):
    if item == side:
      positions.append(index+1)
  
  for index, item in enumerate(row2):
    if item == side:
      positions.append(index+4)
  
  for index, item in enumerate(row3):
    if item == side:
      positions.append(index+7)

  for i in win_patterns:
    if all(pattern in positions for pattern in i):
      return True
    
  return False


def input_check(rows, input):
  row1,row2,row3 = rows[0],rows[1],rows[2]

  if input <= 3:
    if row1[input-1] == ' ':
      return True
  elif input <= 6:
    if row2[input-4] == ' ':
      return True
  elif input <=9:
    if row3[input-7] == ' ':
      return True
  
  return False


def is_rows_full(rows):
  for i in rows:
    for j in i:
      if j == ' ':
        return False

  return True


def main():
  rows = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
  display(rows)
  is_won = False
  winner = ''

  while not is_won:
    input_ok = False
    while not input_ok:
      num_place = int(input('Enter an integer: '))
      input_ok = input_check(rows, num_place)
    rows = tick(rows, num_place, 'x')
    display(rows)
    is_won = check_is_won(rows, 'x')
    if is_won:
      winner = 'x'
      break
    elif is_rows_full(rows):
      winner = None
      break


    input_ok = False
    while not input_ok:
      num_place = int(input('Enter an integer: '))
      input_ok = input_check(rows, num_place)
    rows = tick(rows, num_place, 'y')
    display(rows)
    is_won = check_is_won(rows, 'y')
    if is_won:
      winner = 'y'
    elif is_rows_full(rows):
      winner = None
      break
  
  if winner:
    print(f'Winner is {winner}! Congrats!')
  else:
    print('You tied.')

if __name__ == '__main__':
  main()