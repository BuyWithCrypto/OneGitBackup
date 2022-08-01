from os import name, system, mkdir, path
import time, json, requests, uuid

"""
      ______             _    _ _ _   _     _____                  _
      | ___ \           | |  | (_) | | |   /  __ \                | |
      | |_/ /_   _ _   _| |  | |_| |_| |__ | /  \/_ __ _   _ _ __ | |_ ___
      | ___ \ | | | | | | |/\| | | __| '_ \| |   | '__| | | | '_ \| __/ _ \
      | |_/ / |_| | |_| \  /\  / | |_| | | | \__/\ |  | |_| | |_) | || (_) |
      \____/ \__,_|\__, |\/  \/|_|\__|_| |_|\____/_|   \__, | .__/ \__\___/
                    __/ |                               __/ | |
                   |___/                               |___/|_|
              Buy Differently Everywhere
                https://www.buywithcrypto.fr
"""

def clear():
   if name == 'nt':
       _ = system('cls')
   else:
       _ = system('clear')

def main():
    clear()
    print("""
                 _nnnn_
                dGGGGMMb     ,^^^^^^^^^^^^^^.
               @p~qp~~qMb    | OneGitBackup |
               M|@||@) M|   _;..............'
               @,----.JM| -'
              JS^\__/  qKL
             dZP        qKRb     Powered by BuyWithCrypto
            dZP          qKKb      Buy Differently Everywhere
           fZP            SMMb
           HZM            MMMM
           FqM            MMMM
         __| ".        |\dS"qML
         |    `.       | `' \Zq
        _)      \.___.,|     .'
        \____   )MMMMMM|   .'
             `-'       `--' hjm

      https://www.buywithcrypto.fr

    """)
    ask_1 = input(" Enter the name of your organization : ")
    print(f"  Organization : {ask_1}\n")
    ask_2 = input(" Would you like to make a backup of the Github public repositories ? (Y/n) ")
    if ask_2 == "Y" or ask_2 == "Yes":
        print("  Type of backup : Public Repos")
        clear()
        time.sleep(2)
        public_backups(ask_1)
    else:
        print("  Type of backup : Private Repos")
        print("\n - Please fill in your Github credentials. (https://github.com/settings/tokens)")
        git_username = input(" Username [] : ")
        print(f"  Username : {git_username}\n")
        git_token = input(" Token [] : ")
        print(f"  Token : {git_token}\n")
        clear()
        time.sleep(2)
        private_backups(ask_1, git_username, git_token)

def public_backups(org_name):
    try:
        info = requests.get("https://api.github.com/orgs/"+org_name+"/repos?type=all")
        info = info.content.decode("utf-8")
        public_info = json.loads(info)
        total_repos = len(public_info)
        folder = str(uuid.uuid4())
        if path.exists(folder) == False:
            mkdir(folder)
        else:
            folder = str(uuid.uuid4())
            if path.exists(folder) == False:
                mkdir(folder)
        print(f"""
        Organization : {org_name}
        Type of backup : Public Repos
        Total number of repositories : {total_repos}
        UUID of the backup : {folder}

        """)
        for i in range(total_repos):
            local_file_backup_url = public_info[i]["html_url"]
            repo_name = public_info[i]["name"]
            repo_branch = requests.get("https://api.github.com/repos/"+org_name+"/"+repo_name+"/branches")
            repo_branch = repo_branch.content.decode("utf-8")
            repo_branch = json.loads(repo_branch)
            for j in range(len(repo_branch)):
                repo_branch_name = repo_branch[j]["name"]
                file_backup_url = requests.get(local_file_backup_url+"/archive/refs/heads/"+repo_branch_name+".zip")
                file_backup_name = public_info[i]["name"]+"-"+repo_branch_name+".zip"
                file_backup_zip = open(path.join(folder, file_backup_name), "wb")
                file_backup_zip.write(file_backup_url.content)
                file_backup_zip.close()
                print(f"{local_file_backup_url} [{repo_branch_name}] - [OK]")
    except:
        print("An error occurred and it was impossible to obtain the necessary data...")

def private_backups(org_name, git_username, git_token):
    try:
        info = requests.get("https://api.github.com/orgs/"+org_name+"/repos?type=all", auth=(git_username, git_token))
        info = info.content.decode("utf-8")
        public_info = json.loads(info)
        total_repos = len(public_info)
        folder = str(uuid.uuid4())
        if path.exists(folder) == False:
            mkdir(folder)
        else:
            folder = str(uuid.uuid4())
            if path.exists(folder) == False:
                mkdir(folder)
        print(f"""
        Organization : {org_name}
        Type of backup : Private Repos
        Total number of repositories : {total_repos}
        UUID of the backup : {folder}

        """)
        for i in range(total_repos):
            local_file_backup_url = public_info[i]["html_url"]
            repo_name = public_info[i]["name"]
            repo_branch = requests.get("https://api.github.com/repos/"+org_name+"/"+repo_name+"/branches", auth=(git_username, git_token))
            repo_branch = repo_branch.content.decode("utf-8")
            repo_branch = json.loads(repo_branch)
            for j in range(len(repo_branch)):
                repo_branch_name = repo_branch[j]["name"]
                file_backup_url = requests.get(local_file_backup_url+"/archive/refs/heads/"+repo_branch_name+".zip", auth=(git_username, git_token))
                file_backup_name = public_info[i]["name"]+"-"+repo_branch_name+".zip"
                file_backup_zip = open(path.join(folder, file_backup_name), "wb")
                file_backup_zip.write(file_backup_url.content)
                file_backup_zip.close()
                print(f"{local_file_backup_url} [{repo_branch_name}] - [OK]")
    except:
        print("An error occurred and it was impossible to obtain the necessary data...")

if __name__ == "__main__":
    main()
