# 💾 OneGitBackup

This is a tool to make backups of organisations' Github repositories automatically.

![Demo 1](https://raw.githubusercontent.com/BuyWithCrypto/OneGitBackup/main/demo/1.png)

------

# 💻 Examples of use

## - 💿 The backup of public repositories :

We want to back up all the public repositories of our organisation and all their branches.

![Demo 2](https://raw.githubusercontent.com/BuyWithCrypto/OneGitBackup/main/demo/2.png)

A UUID (Universally unique identifier) will then be generated and this will be the folder name where the backup will be saved.

![Demo 3](https://raw.githubusercontent.com/BuyWithCrypto/OneGitBackup/main/demo/3.png)

Once the tool has completed its tasks, the backups will be available as a .zip file with the repository name as a prefix and the repository branch name as a suffix.

![Demo 4](https://raw.githubusercontent.com/BuyWithCrypto/OneGitBackup/main/demo/4.png)

------

# 📦 Installation and use

## - To use the tool on Linux :

_1. Install the pre-required Python libraries :_
```shell
$ wget https://github.com/BuyWithCrypto/OneGitBackup/releases/download/v1.0/requirements.txt && pip3 install -r requirements.txt
```
_2. Download the executable file :_
```shell
$ wget https://github.com/BuyWithCrypto/OneGitBackup/releases/download/v1.0/OneGitBackup.pyc
```
_3. Start the executable :_
```shell
$ python3 OneGitBackup.pyc
```
------

## - To use the tool on Windows :

_1. Clone the repository with git :_
```shell
$ git clone https://github.com/BuyWithCrypto/OneGitBackup/
```
_2. Install the pre-required Python libraries :_
```shell
$ pip install -r requirements.txt
```
_3. Start the executable :_
```shell
$ python main.py
```
------

# 🔨 Contribution for developers

------

## ✅ Setting up the environment :
_1. Clone the Github repository :_
```shell
$ git clone https://github.com/BuyWithCrypto/OneGitBackup/
```
_2. Navigate to the project folder :_
```shell
$ cd OneGitBackup/
```
_3. Install the pre-required Python libraries :_
```shell
$ pip3 install -r requirements.txt
```

------

## 🚧 Building the source code
_To compile the source code into an executable, you can use this command. :_

```shell
$ python3 -m py_compile main.py
```