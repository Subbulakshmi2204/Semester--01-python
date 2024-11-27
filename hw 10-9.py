
def display():
    print("Available books")
    x=["Harry potter","Love stories","Jeronimo Stilton","Jungle book"]
    print(x)
display()
def add_newbook():
    print("Adding a new book")
    c=input()
    x=["Harry potter","Love stories","Jeronimo Stilton","Jungle book"]
    x.append(c)
    print(x)
add_newbook()
def del_book():
    print("Deleting a new book")
    x=["Harry potter","Love stories","Jeronimo Stilton","Jungle book"]
    x.pop(1)
    print(x)
del_book()

def display():
    print("View inventory")
    x={"Shampoo":120,"Hamam":30,"Cardiac oil":230,"Maggie":15}
    print(x)
display()
def add_product():
    print("Adding a new product")
    c={"Cake":20}
    x={"Shampoo":120,"Hamam":30,"Cardiac oil":230,"Maggie":15}
    x.update(c)
    print(x)
add_product()
def remove_product():
    print("Removing a product")
    x={"Shampoo":120,"Hamam":30,"Cardiac oil":230,"Maggie":15}
    x.pop("Hamam")
    print(x)
remove_product()
