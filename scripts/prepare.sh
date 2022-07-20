cd /content/yolor_train/models

curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=1l85UwQBa1thN6koSVysa6X-kmscA9I5r" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=1l85UwQBa1thN6koSVysa6X-kmscA9I5r" -o behAI_pretrained_yolor_p6.pt
rm ./cookie

curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=1Kf9hnvOfsdYMc9PM4qMRDRKybArZT7k9" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=1Kf9hnvOfsdYMc9PM4qMRDRKybArZT7k9" -o behAI_pretrained_yolor_w6.pt
rm ./cookie

cd ..

echo ""
echo "----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----"
echo "PREPARATIONS COMPLETED"