try:
    class Library:
        import pandas as pd
        def __init__(self,library_name):
            print('Welcome user, \n!!world of managing libraries!!')
            self.libname=library_name
            with open(f'{self.libname}booklistfile.txt','a+') as f:
                self.book_list=[]
            with open(f'{self.libname}booklistfile.txt','r') as f:
                for all_books in f:
                    self.book_list.append(all_books[:-1])

        def available_options(self):
            def stoping_option():
                stop_option=input('Wanna exit??\n(Type yes or no)\n ::')
                if stop_option=='yes' or stop_option=='YES' or stop_option=='Yes':
                    return exit()
                elif stop_option=='No' or stop_option=='no' or stop_option=='NO':
                    return None
                else:
                    print('!enter valid option please!')
                    print('########################### Enter again ###########################')
                    stoping_option()
            while(True):
                print('//Dear, Please click//')
                print('Click ->1 : for adding books \n Click ->2 : for displaying books \n Click ->3 : for lending book \n Click ->4 : for returning book')
                print('Enter:')
                option=int(input())
                if option == 1:
                    self.book_add()
                elif option == 2:
                    self.book_display()
                elif option == 3:
                    self.book_lending()
                elif option == 4:
                    self.book_return()
                else:
                    print('Sorry, there is no options like that (- _ -)')
                stoping_option()

        def book_add(self):
            print('\\Please add book\\')
            n=int(input('Enter number of books you want to add:'))
            list_new=[]
            for i in range(n):
                book=input('Enter name of Book:')
                list_new.append(book)
                self.book_list.append(book)
            with open(f'{self.libname}booklistfile.txt','a') as f:
                for i in list_new:
                    f.write(str(i+'\n'))


        def book_display(self):
            print('\n\nAll available books are:-\n')
            if self.book_list == '':
                print('~~Sorry dear, No books available~~')
            else:
                count=1
                for i in self.book_list:
                    print(f"{count}.{i}",end='\n')
                    count+=1

        def book_lending(self):
            book_name=input('please enter the book name you want?:')
            if book_name in self.book_list:
                person_name = input('Enter your name:')
                person_id = input('Enter your ID:')
                from datetime import datetime, timedelta
                lending_date = datetime.today()
                print(f"Current date:{lending_date.strftime('%B,%d,%y')}")
                date_return = lending_date + timedelta(days=7)
                print(f"your last date to return is:{date_return.strftime('%B,%d,%y')}")
                with open(f'{self.libname}Library_mange_file.txt','a+') as f:
                    f.write(str(str(book_name)+','+','+person_name+','+person_id+','+str(lending_date)+','+str(date_return.strftime('%m-%d-%y'))+'\n'))
                    print(f'Here is your {book_name} book,thankyou dear for lending!!')
                self.book_list.remove(book_name)
                import os
                with open(f'{self.libname}booklistfile.txt','r') as input_file:
                    with open('tmp_file_book_list.txt','w') as output_file:
                        for line in input_file:
                            if book_name not in line.strip('\n'):
                                output_file.write(line)
                os.replace('tmp_file_book_list.txt', f'{self.libname}booklistfile.txt')

            else:
                with open(f'{self.libname}Library_mange_file.txt','r') as f:
                    print('~~Searched book is not available dear!~~')
                    for line in f:
                        if book_name in line:
                            print(f"It is already by lended by' :{line}")

        def book_return(self):
            print('please,')
            person_id=input('Enter your id:')
            book_name=input('Enter the book name:')
            import os
            with open(f'{self.libname}Library_mange_file.txt','r') as input_file:
                with open('tmp_Library_mange_file.txt','w') as output_file:
                    for line in input_file:
                        if person_id not in line.strip('\n') and book_name not in line.strip('\n'):
                            output_file.write(line)
            os.replace('tmp_Library_mange_file.txt', f'{self.libname}Library_mange_file.txt')
            with open(f'{self.libname}booklistfile.txt', 'a') as f:
                        f.write(book_name)
            print('Thankyou for returning dear')

    print('Create your library by creating new library, please enter the library name and list of books:')
    Library_name=input('Enter your library_name:')
    obj_library=Library(Library_name)
    obj_library.available_options()

except Exception as e:
    print('\n\n~~~~~~~~~~~~~~~~~~~Error occured:')
    print(e,end='')
    print('~~~~~~~~~~~~~~~~~~~')