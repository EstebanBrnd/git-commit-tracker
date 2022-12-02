while true
do
git log -10 HEAD --pretty=format:%s >com.txt
git log -10 --pretty=format:'%an' >author.txt
git log -10 --format=%cd >date.txt
git log -10 --format=format:"%H" >hash.txt
basename -s .git `git config --get remote.origin.url` >name.txt
git show -10 --name-only --oneline HEAD >sortie.txt
python3 commit_tracker.py
rm date.txt
rm author.txt
rm com.txt
rm name.txt
rm hash.txt
rm sortie.txt
rm -f commit.txt
sleep $1
done
