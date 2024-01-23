import os
import random
li = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lst_drive = []
for drive in li:
    try:
        
        r = os.listdir(f'{drive}:/')
        lst_drive.append(drive)

    except FileNotFoundError:
        continue
    except PermissionError:
        continue

folder_name=['Music','Songs',"Gaane"]
def search_fol(drive):
    for folder in folder_name:
          
          try:
           m1 = os.listdir(f'{drive}:/{folder}')
           
           r=random.randint(0,len(m1)-1)

           os.startfile(f'{drive}:/{folder}/{m1[r]}')
           print(f"Playing music {m1[r]}in drive {drive} ")

          except:
              
              continue

def music_play(): 
 for drive in lst_drive:
     try:
         
         search_fol(drive)
         
             
     except FileNotFoundError:
         
         continue
if __name__=='__main__':
    music_play()
