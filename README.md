         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


Hi there! Welcome to AWS Cloud9!

To get started, create some files, play with the terminal,
or visit https://docs.aws.amazon.com/console/cloud9/ for our documentation.

Happy coding!

# Description
Kode latihan python untuk kelas IDJAK127


# How to integrate AWS Cloud9 with GitHub

<img width="733" height="433" alt="Pasted Graphic 1" src="https://github.com/user-attachments/assets/2d5f90cd-3e3a-4ec0-8349-f13e1126be29" />

1. Create .ssh folder in root folder.
   ```
   mkdir .ssh
   ```
   
1. Generate an SSH key pair named "github". You can customize the name as you like.
   ```
   ssh-keygen -t ed25519 -C "zavfake@gmail.com" -f /home/ec2-user/environment/.ssh/github
   ```

1. Register generated publickey github.pub to GitHub.
   <img width="946" height="520" alt="image" src="https://github.com/user-attachments/assets/51f623f6-a07f-4225-926f-8b28a2219da6" />

   > **_Login to your GitHub account through github.com -> Profile (rigt corner) -> Settings -> SSH and GPG Keys -> New SSH key:_**
   > **_Copy all content within your .ssh/github.pub content -> paste to ssh(see the config in the image above):_**

   
1. Create ssh with custom key path. (Repeat this step whenever you start the machine again)
   ```
   eval "$(ssh-agent -s)"
   ssh-add .ssh/github
   ```

1. Validate the SSH connection & key is loaded successfully.
   ```
   ssh git@github.com
   ```
   expected output:
   ```
   Hi zavfake! You've successfully authenticated, but GitHub does not provide shell access.
   ```
   **If you are not successfully authenticated, repeat the step from begining. **

1. Create **.gitignore** file and fill with the code below. Remember: We shouldn't share the private key to everyone. Keeping the key secret on our machine is a must!!
   ```
   .ssh/
   .c9/
   ```
   
1. Init new local git. By default, the new repository will place your code in the "master" branch.
   ```
   git init
   ```

1. Register remote github repository.
   note: SSH remote address begin with **git@github.com:...**
   <img width="395" alt="image" src="https://github.com/user-attachments/assets/d8ce22ef-1030-4c42-b571-ceae79b89b1e" />
   ```
   git remote add origin [copied ssh remote address]
   ```


1. Create & checkout to new branch named "main". Remember, when you open the github, the default branch is main, so we should follow this rule.
   ```
   git checkout -b main
   ```

1. Test pulling the code from GitHub
   ```
   git pull origin main
   ```
   
   If you get the error "unrelated history", do this:
   ```
   git pull origin main --allow-unrelated-histories
   ```

   If yout get the warning "You have divergent branches and need to specify how to reconcile them...", do this:
   ```
   git config pull.rebase false
   ```
   
1. Sync your code from local git to the GitHub (do this whenever you want to sync the new code to GitHub)
   ```
   git add .
   git commit -m "Commit Message/Update notes"
   git push origin main --force
   ```

1. Check your uploaded code in GitHub. Happy coding! If you encounter any issues, please drop your question in the whatsapp group and I will answer as soon as possible 😊❤️💡
   

