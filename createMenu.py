def createMenu(optionlist):
  '''Description:  Returns printable sting of options
     Prescription: optionlist is a list of options w/out numbers
  '''
  ct = 1
  optionstr = ''
  for a in optionlist:
    optionstr = optionstr + str(ct) + ':' + ' ' + a + '\n'
    ct += 1

  return optionstr
