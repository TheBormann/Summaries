# Git 
This is a quick summary of the most useful git commands.

## Create repos

* git init  
    (initialize an existing directory as a Git repository)

* git clone [url]  
    (retrieve an entire repository from a hosted location via URL)


## Branches
* git branch [branch-name]  
    (create a new brand name)

* git checkout [branch-name]  
    (Switches to other branch and updates the working directory)
    
* git merge [branch]  
    (Combines the specified with the current branch)

* git branch -d [branch-name]  
    (Deletes the specified branch)

## Gitignore
You can add a empty ".gitignore" file to any folder. This will stop git from uploading that folder.

You can also add an gitignore file in your root dir of your project and specify in that file what elements shouldn't get
uploaded:  
https://www.atlassian.com/git/tutorials/saving-changes/gitignore

## Synchronize changes

* git fetch  
    (Update your branch to newest version)

* git merge  
    (combines remote tracking branch into current local branch)

* git push  
    (Uploads local branch changes to branch)
    
* git pull  
    (pull is a combination of fetch and merge. It updates your current local working branch with all new commits)

## Make changes
* git log  
    (Lists version history for current branch)

* git log --follow [file]  
    (Lists version history for a file, including renames)

* git diff [first-branch]...[second-branch]  
    (Shows differences between both branches)
    
* git show [commit]  
    (Displays metadata and content changes of the specified commit)
    
* git add [file]  
    (Adds file to git versioning)
    
* git commit -m "[message]"  
    (Uploads changes to the repo)

## Configure

* git config --global user.name "[name]"  
    (Change your name)

* git config --global user.email "[email]"  
    (Change your email)
    
* git config --global color.ui auto  
    (enable colorization in command line)

## Redo commits

* git reset [commit]  
    (Undoes all commits after [commit], preserving changes locally)

* git reset --hard [commit]  
    (Discards all history and changes back to the specific commit)
    
## Reference 

* https://git-scm.com/
* https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiR79iN4MrsAhUMzqQKHXIcD6MQFjAAegQIBhAC&url=https%3A%2F%2Feducation.github.com%2Fgit-cheat-sheet-education.pdf&usg=AOvVaw2D3W2R0fwoOBi8YrhZYLFJ
