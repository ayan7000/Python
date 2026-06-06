def print_kwargs(**kwargs):
    # print("Name",name,"Power:",power)
    for key,value in kwargs.items():
        print(f"{key}:{value}")


print_kwargs(name = "shaktiman",power="lazer", enemy="shakaal")