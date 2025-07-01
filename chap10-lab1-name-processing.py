#Tim Lucas
#Lab 10-1
#2025-07-01

def main():
    print("Name Processor")
    print("")

    name = input("Enter your name: ")

    i = name.find(",")
    if i == -1:
        space = name.find(" ")
        first_name = name[:space]
        last_name = name[space:]

    else:
        comma = name.find(",")
        last_name = name[:comma]
        
        first_name = name[comma + 2:]

    formatted_name = f"{last_name}, {first_name}"
    formatted_name = formatted_name.title()
    formatted_name = formatted_name.strip()

    print(formatted_name)        

if __name__ == "__main__":
    main()