""" Nonrepeat.py """"

def find_non_repeat(A_STRING):
  LEN_A_STRING = len(A_STRING)
  Ctr = 0
  Ltrs = dict()
  while Ctr < (LEN_A_STRING):
      Testchar = A_STRING[Ctr]
      if Testchar in Ltrs:
          Ltrs[Testchar] += 1
      else:
          Ltrs[Testchar] = 1
      Ctr += 1
  First = 1
  for k in Ltrs:
      if Ltrs[k] == 1:
          if First == 1:
              First = 0
              return(k)
  if First == 1:
      raise ValueError("No non-repeating characters")
      #print(f"no repeat character in {A_STRING}")