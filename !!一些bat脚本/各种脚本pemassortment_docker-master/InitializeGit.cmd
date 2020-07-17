REM Vytvorenie git repository
git init

REM Adds the files in the local repository and stages them for commit. To unstage a file, use 'git reset HEAD YOUR-FILE'.
git add .

REM Commits the tracked changes and prepares them to be pushed to a remote repository. To remove this commit and modify the file, use 'git reset --soft HEAD~1' and commit and add the file again.
git commit -m "First commit"

REM Sets the new remote
git remote add origin https://github.com/slado/pemassortment_docker.git

REM Verifies the new remote URL
git remote -v

REM Pushes the changes in your local repository up to the remote repository you specified as the origin
git push origin master

REM na naklonovanie pouzit git clone <repo>