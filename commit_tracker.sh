while true
do
git log -10 HEAD --pretty=format:%s >com.txt
git log -10 --pretty=format:'%an' >author.txt
git log -10 --format=%cd >date.txt
python3 commit_tracker.py
rm date.txt
rm author.txt
rm com.txt
sleep 10
done