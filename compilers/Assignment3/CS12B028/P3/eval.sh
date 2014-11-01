javac  P3.java
count=0;
totalcount=0;
for i in examples/*.java;
do
	totalcount=$((totalcount+1));
#echo $i;
	java P3 < $i > tempfile;
	java -jar pgi.jar < tempfile > tmpoutput;
	cd examples/;
	j=`echo $i | sed 's/\([^\/]*\/\)\(.*\)/\2/'`;
	javac $j;
	class=`echo $j | sed 's/\([^\.]*\)\(.java\)/\1/'`;
#echo $class;
	java  $class> ../tmpoutput2;
	cd ../;
	diff tmpoutput2 tmpoutput > /dev/null;
	if [ $? -eq 0 ]
		then
		echo "Successful"
		count=$((count+1));
		else
		echo $j;
		echo "Failed"
	fi
	rm tmpoutput tmpoutput2
done
echo $count
echo $totalcount