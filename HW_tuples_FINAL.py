library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]  # tuple 

def main():
    while True:    #Define main then create user menu
        ans = input('''   
"Welcome to Library Finder!!
Enter an option , please: 
1. Add a Book to the list
2. View All Books
3. Exit                   
''')
    #Starting the loops
        if  ans == '1':   #Add a tuple to the list
            add_book()  #Call the function
        elif ans == '2':             #IF user hits 2 
             for title,author in library:
                print(f"{title},{author}")
        elif ans == '3':   #if user hits 3
            print("Thank you for using this terrible app-  May God have mercy on your      soul!")
            break   #Quit 

def add_book():
    title = input("Enter the book title:") #Asking for the title
    author = input("Enter the author's name: ")#Asking for the author's name
    book = (title, author)
    print(f"Book {title}, {author} added successfully.") # Letting the user know all is good
    if book in library:
         print("This book is already in the libray")
    else:
         library.append(book)
             
main()


