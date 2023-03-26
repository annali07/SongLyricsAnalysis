import os
import collections

# Definition 
directory = "songs"
charlist=['']
countdic={'End':0}
count=1
count2=1
test=False
kanatest=False

def delete():
  countdic.pop('\n')
  countdic.pop(' ')
  countdic.pop('(')
  countdic.pop(')')
  countdic.pop('「')
  countdic.pop('」')
  countdic.pop('"')
  countdic.pop(':')
  countdic.pop('”')
  countdic.pop('“')
  countdic.pop('…')
  countdic.pop('　')
  countdic.pop('.')
  countdic.pop('（')
  countdic.pop('）')
  countdic.pop('、')
  countdic.pop('-')

def deletekana():
  with open('kana.txt',encoding='utf8') as file:
    char=file.read()
    for i in char:
      if i in countdic:
        countdic.pop(i)
  return True

for filename in os.listdir(directory):
  f = os.path.join(directory,filename)
  if os.path.isfile(f):
    
    print(f'\nReading File No.{count}...')
    
    with open(f, encoding='utf8') as file:   
      
      result=file.read()
      
      for i in result:
        for j in charlist:
          
          if i==j:
            test=False  
            
            for key,value in countdic.items():  
              if i==key:
                countdic.update({i:int(int(countdic[i])+1)})
                test=True
            
            if test==True:
              charlist.remove(j)
              break  
            elif test==False:
              countdic.update({i:int(2)})
              charlist.remove(j)
                  
        charlist.append(i)
  
  count+=1

print(f'\nAnalysis of {count-1} songs finished\n')


# Formating (Optional) 
delete()
kanatest=deletekana()


# Output
sorted_x = sorted(countdic.items(), key=lambda x:x[1], reverse=True)
sorted_dict = collections.OrderedDict(sorted_x)

with open('summary.txt','w') as file:
  file.write(f'Data collected from {count-1} HoneyWorks songs!\n')
  file.write(f'Character: frequency\n\n')
  if kanatest==True:
    file.write("----Now viewing the version without kana----\n\n")
  
  for key,value in sorted_dict.items():
    a=f'{key}: {value}'
    file.write(f'{count2}.\t{a}')
    file.write("\n")
    count2+=1