pip install -qr ./requirements.txt
cd ./mish-cuda/
python setup.py build install
cd ..
cd pytorch_wavelets
pip install .
cd ..
echo ""
echo "----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----"
echo "SETUP COMPLETE."