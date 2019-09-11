def set_date():
    date = input("For how long you want them to be unable?\n(Type data time in following format: H H)\n")
    date = list(map(int,date.split(" ")))
    return date

def make_list():
    weblist = input("Which websites would you like to block?:\n(Separate them by space)\n ")
    weblist = list(weblist.split(" "))
    return weblist

def make_final_list(weblist, redirect):
    final_list = [redirect+"\t"+ i for i in weblist]
    final_list = "\n".join(final_list)
    final_list = final_list.split("\n")
    return final_list

def orginal_file_data(file_path):
    with open(file_path,"r+") as file:
        content = file.read()

    return content
