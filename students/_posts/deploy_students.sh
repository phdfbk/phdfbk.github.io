rm *.md
git pull
python create_students.py
git commit -a -m "update students"
git push -a
