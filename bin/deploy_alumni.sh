cd ../alumni/_posts
wget "https://docs.google.com/spreadsheets/d/1UJ8eHwcBsdKRjwc6uu2KVhNIn_FSEpLMh6xqMNQ5sUY/pub?gid=2103651667&single=true&output=csv" -O alumni.csv 
mkdir -p old
mv *.md old
git pull
python ../../bin/create_alumni.py
git add *.md
git commit -a -m "update alumni"
git push 
