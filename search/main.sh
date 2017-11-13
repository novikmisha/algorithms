FILES=/home/misha/python/sorts/merge/1000000/*
for f in $FILES
do
  echo "Processing $f file"
  # take action on each file. $f store current file name
  cat $f | grep -n -w 3402
done
