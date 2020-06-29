def BinaryReversal(str):

  integer = int(str)
  binary = format(integer, 'b')
  bin_arr = []
  for x in binary:
    bin_arr.append(x)
  bin_arr_reverse = bin_arr[::-1]
  zeros_to_append = len(bin_arr_reverse) % 8
  if zeros_to_append != 0:
    zeros_to_append = 8 - zeros_to_append
  for x in range(zeros_to_append):
    bin_arr_reverse.append("0")
  bin_reverse = ''
  for x in bin_arr_reverse:
    bin_reverse += x
  dec_reverse = format(bin_reverse, "2")
  dec_reverse = int(dec_reverse, 2)

  return dec_reverse

# keep this function call here 
print(BinaryReversal(213))