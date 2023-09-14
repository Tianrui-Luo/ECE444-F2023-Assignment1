class utils:

  def reversed(number):
    num=str(number)
    num_rev=int(num[len(num)::-1])
    print(num_rev)

  def formatter(number):
    print("Binary:",bin(number))
    print("Octal:",oct(number))
