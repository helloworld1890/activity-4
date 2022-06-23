def pascal(n):
  triangle = [[1], [1,1]]
  if n == 1:
    print(triangle[0])
  else:
    row_number = 2
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number-1]
      length = len(row_prev)+1
      for i in range(length):
        if i == 0:
          row.append(1)
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        else:
          row.append(1)
          triangle.append(row)
          row_number += 1
          
    for row in triangle:
      print(row)

pascal(4)

def max_num():
  num = [1, 2, 3]
  
  for i in num:
    print(max(num))


def mult_list():
  l = [ 1, 2, 3]

  for i in l:
    i *= 2
    print(i)


def rev_string(string):
  txt = string[::-1]
  print(txt)



def num_within(within):
  r = range(1, 10)
  for i in r:
    if i <= 10:
      print("you are within range")
    else:
      print("you our out of range")
 
