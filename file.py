f=input("enter file extension:")
match f:
    case 'py':print("python file")
    case 'c':print("c file")
    case 'c++':print("c++ file")
    case 'html':print("html file")
    case 'jpg':print("image file")
    case _:print("unknown file")
