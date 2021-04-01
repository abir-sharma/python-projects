class Library:
    def __init__(self,nameoflib,booklist):
        self.nameoflib=nameoflib
        self.booklist=booklist
        self.dict={}
        print(f'Welcome to the {self.nameoflib}!!!')

    @staticmethod
    def welcomemsg():
        print('''
Please choose an option:
1. List all the books
2. Request a book
3. add/Return a book
4. Exit the Library
        ''')


    def displayallbooks(self):
        print(f'Availaible Books in the {self.nameoflib} are :')
        for books in self.booklist:
            print('*'+books)


    def borrowbook(self,bookname,user):
        if bookname in self.booklist:
            self.booklist.remove(bookname)
            self.dict.update({str(bookname):str(user)})
            print(f'{bookname} is issued to {user} ')
        elif bookname in self.dict.keys():
            print(f"{bookname} is already issued to {user}")
        else:
            print(f"{bookname} is not present in the {self.nameoflib}")


    def returnbook(self,bookname2,user2):
        if bookname2 in self.dict.keys():
           self.booklist.append(bookname2)
           self.dict.pop(bookname2)
           print(f"{bookname2} is returned by {user2}")
        elif bookname2 not in self.dict.keys():
            self.booklist.append(bookname2)
            print(f'{bookname2} is added in the library by {user2}')
        else:
            print('Something went wrong')


class Student:
    def requestbook(self):
        bookname=input('enter book name you want to borrow :')
        user=input('enter your name :')
        return bookname,user

    def reutrnbook(self):
        bookname2=input("type name of book you want to return/add :")
        user2=input("type your name :")
        return bookname2,user2


if __name__ == '__main__':
    centrallib=Library('//// LIBRARY',['python','java','html','css','java script'])
    students=Student()
    while(True):
        centrallib.welcomemsg()
        try:
           comm=int(input('enter your choice :'))
        except ValueError :
            print('input must be integer value')
            continue
        if comm==1:
            centrallib.displayallbooks()
        elif comm==2:
            inputs=students.requestbook()
            centrallib.borrowbook(inputs[0],inputs[1])
        elif comm==3:
            inputs2=students.reutrnbook()
            centrallib.returnbook(inputs2[0],inputs2[1])
        elif comm==4:
            print('thanks for using library')
            exit()
        else:
            print("invalid choice")
