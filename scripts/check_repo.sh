if [ -d "/content/yolor_train" ] 
then
    python ./utils/setup.py
else
    echo "Error: Download failed."
fi

