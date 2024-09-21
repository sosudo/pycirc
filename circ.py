def lcirc(shift:int, bit:str) -> str:
  bit = str(bit) if not isinstance(bit,str) else bit
  bit_list = [i for i in bit]
  shift_bit = ''
  for i in range(shift):
    bit_list.append(bit_list[0])
    bit_list.pop(0)
  for i in bit_list:
    shift_bit += i
  return shift_bit
def rcirc(shift:int, bit:str) -> str:
  bit = str(bit) if not isinstance(bit,str) else bit
  bit_list = [i for i in bit][::-1]
  shift_bit = ''
  for i in range(shift):
    bit_list.append(bit_list[0])
    bit_list.pop(0)
  for i in bit_list[::-1]:
    shift_bit += i
  return shift_bit
