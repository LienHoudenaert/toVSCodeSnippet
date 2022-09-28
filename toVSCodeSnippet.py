print("\nCONVERT FILE TO A CUSTOM VS CODE SNIPPET:")
print("----------------------------------------\n")

try:
    # user input
    name = input("Enter the name for the snippet: ")
    prefix = input("Enter the prefix (= name used to call the snippet in VS Code): ")

    # check if file exists
    while True:
        input_path = input("Enter the path of the to be converted file: ")
        try:
            file = open(input_path, 'r').readlines()
        except FileNotFoundError:
            print("\nWrong file or file path\n")
        else:
            break

    description = input("Enter the description: ")
    output_path = input("Enter the path and filename for the output file: ")

    # convert array list to string
    def listToString(list):
        # initialize an empty string
        str = ""
        # traverse in the string
        for element in list:
            str += element
        # return string
        return str

    try:
    
        # read lines in file and store them in variable
        with open(input_path) as code_file:
            lines = code_file.readlines()

        # declare variables
        tab = "\\t"
        double_quote = '\\"'
        body = []

        # loop through all the lines and make needed changes
        for line in lines:
            # count all tabs in a line
            tabcount = line.count("  ")
            
            # start with 3 tabs
            tabs = "\t\t\t"
            i = 0

            # add tabs based on tabs in original file
            while i < tabcount:
                tabs = "".join(("\t", tabs))
                i += 1
            
            line = line.replace("  ", tab)
            line = line.replace("\"", double_quote)
            line = line.replace("\n", "")
            line = "".join((tabs ,"\"", line, "\",\n"))
            body.append(line)

        text_list = ["{\n", "\t\"" + name + "\": {\n", "\t\t\"prefix\": \"" + prefix + "\",\n", "\t\t\"body\": [\n", listToString(body) + "\n", "\t\t],\n", "\t\t\"description\": \"" + description + "\"\n", "\t}\n" ,"}"]

        snippet_file = open(output_path, "w")
        snippet_file.writelines(text_list)
        snippet_file.close()

    except:
        print("\nSomething went wrong!")
    finally:
        print("\nFile successfully converted to a VS Code snippet!\n")

        # save the snippet directly to VS Code
        save_in_vscode = input('Do you also want to add the snippet to VS Code? (yes or no): ')
        while save_in_vscode not in {"yes", "no"}:
            save_in_vscode = input("Please enter yes or no: ")
            # Now response is either "yes" or "no"
    
        if save_in_vscode == "yes":
            try:
                vscode_snippets_path = "C:\\Users\\Lien\\AppData\\Roaming\\Code\\User\\snippets\\" + name + ".code-snippets"
                vscode_file = open(vscode_snippets_path, "w")
                vscode_file.writelines(text_list)
            except:
                print("\nSomething went wrong!")
            finally:
                print("\nFile successfully saved in VS Code! \nYou can call the snippet by typing " + prefix.upper() + " in VS Code") 

except KeyboardInterrupt:
    print("\n")
    print("Exiting code...")
    exit()