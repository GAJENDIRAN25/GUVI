ch= input('enter your character')
if (ch.isalpha()):
  if ch in 'a,e,i,o,u,A,E,I,O,U':
    print('Vowel')
  else:
    print('Consonent')
else:
  print('invalid')
    
