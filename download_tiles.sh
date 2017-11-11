#!/bin/bash 

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
    ;;
    *)
    
esac
shift # past argument or value
done
echo "Downloading $X1 - $X2 x $Y1 - $Y2"

for x in `seq $X1 $X2`; do
    
    for y in `seq $Y1 $Y2`; do
    	
	
	if [ -e ${Z}_${y}_${x}.png ]
		then
    		echo "Keep ${Z}_${y}_${x}.png"
	else
		echo "Getting ${x},${y}"
        	curl -s https://a.tile.opentopomap.org/${Z}/${x}/${y}.png -o $DIR/${Z}_${y}_${x}.png &
		wait
	fi

    done

done

