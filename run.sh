atom mu
python cheat.py
rm *.pyc
sed -i 's/&lt;/</g' mu
sed -i 's/&quot;/"/g' mu
sed -i 's/&gt;/>/g' mu
sed -i 's/&#48;/0/g' mu
sed -i 's/&#92;/\/g' mu





