#!/bin/bash 

#Fill in the desired tile numbers here
#X1=8505
#X2=8844
#Y1=5709
#Y2=5710
#Y2=5876

while [[ $# -gt 1 ]]
do
key="$1"

case $key in
    -x1)
    X1="$2"
    shift # past argument
    ;;
    -x2)
    X2="$2"
    shift # past argument
    ;;
    -y1)
    Y1="$2"
    shift # past argument
    ;;
    -y2)
    Y2="$2"
    shift # past argument
    ;;   
    -p|--path)
    DIR="$2"
    shift # past argument
    ;;
    -z)
    Z="$2"
    shift
    ;;
    *)
    
esac
shift # past argument or value
done
echo "Constructing $X1 - $X2 x $Y1 - $Y2"

OUTPUT_DIR=$DIR
INPUT_DIR=$DIR

TIMEFORMAT='%lU'

echo "Creating rows from tiles..."
for y in `seq $Y1 $Y2`; do
    out="$OUTPUT_DIR/out_${Z}_${y}_${X1}-${X2}.png"
    duration=$(time (montage -mode concatenate -tile "x1" "$INPUT_DIR/${Z}_${y}_*.png" $out) 2>&1 1>/dev/null)
    echo "Row $((y-Y1+1)) of $((Y2-Y1+1)) in $duration ($out)"
done
echo "Concatenating rows now..."
MAGICK_TEMPORARY_PATH=. convert -debug cache -append "$OUTPUT_DIR/out_$Z_*_*.png" "$OUTPUT_DIR/out_${Z}_${Y1}-${Y2}_${X1}-${X2}.png"

