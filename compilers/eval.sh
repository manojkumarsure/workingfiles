cd Assignment4
javac P4.java
cd ..
cd Assignment3
javac P3.java
cd ..
cd Assignment5
javac P5.java
cd ..
count=0
totalcount=0
for i in examples/*.java;
do
echo $i;
    java -classpath Assignment3 P3 < $i | java -classpath Assignment4 P4 |java -classpath Assignment5 P5 > tempfile;
    java -jar Assignment5/kgi.jar < tempfile > tmpoutput;
    cd examples/;
       totalcount=$((totalcount+1))
	j=`echo $i | sed 's/\([^\/]*\/\)\(.*\)/\2/'`;
	javac $j;
	class=`echo $j | sed 's/\([^\.]*\)\(.java\)/\1/'`;
	java  $class> ../tmpoutput2;
	rm "$class.class";
	cd ..;
	diff tmpoutput2 tmpoutput > /dev/null;
    if [ $? -eq 0 ]
        then
        echo "Successful"
        count=$((count+1))
    fi
    #rm tmpoutput tmpoutput2 tempfile;
done
echo $count
echo $totalcount
rm examples/*.class