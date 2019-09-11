import time
import fileinput
import functions
from datetime import datetime as dt

host_path = "/etc/hosts"
redirect = "127.0.0.1"

website_list = functions.make_list()
orginal_data = functions.orginal_file_data(host_path)
final_list = functions.make_final_list(website_list, redirect)
date = functions.set_date()

try:

    while True:

        if date[0] < dt.now().hour < date[1]:
            print("Working hours...")
            with open(host_path, "r+") as file:
                    content = file.readlines()
                    for website in final_list:
                        if website+"\n" in content:
                                pass
                        else:
                            file.write(website+"\n")
        else:
            with open(host_path, "r+") as file_2:
                    file_2.truncate(0)
                    file_2.write(orginal_data)
                    print("Fun hours...")
                    break
        time.sleep(5)


except KeyboardInterrupt:
    with open(host_path, "r+") as file_2:
        file_2.truncate(0)
        file_2.write(orginal_data)
        print("You stopped the blocker...\nUnblocking websites...")



