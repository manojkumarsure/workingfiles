#!/bin/bash

tmpfile='tmpfile.txt';
debug=1;
timeout="600s";

for orifile in `ls -1 [cC][sS]*[bB]*.pl`; do
	export filecase=`echo $orifile | sed 's/.pl//'`;
	export file=`echo $orifile | tr 'a-z' 'A-Z' | sed 's/.PL//'`;
	if [ "$debug" -eq 1 ]; then
		echo Student = $file;
	fi
	# mv $orifile $file.lisp
	export corrects=0;
	export wrongs=0;
	
	export starttime=`date '+%s'`
	for t in {1..10}; do
		export testfile="t$t.test"
		#echo $testfile;
		echo "consult(c$t)."		 > $tmpfile;
		echo "consult($filecase)."	>> $tmpfile;
		cat $testfile 			>> $tmpfile;

		export output=`timeout $timeout cat $tmpfile | prolog 2>&1 | grep =`; 
		export relevantoutput=`echo $output | sed 's/\?*//' | sed 's/^[ ]*//' | sed 's/[ ]*$//' | sort`

		export golden=`cat a$t.answer | sed 's/^[ ]*//' | sed 's/[ ]*$//' | sort`;
		export relevantgolden=`echo $golden`;
		echo $relevantgolden > "o$t.txt";
		echo $relevantoutput > "o_$t.txt";
		if [ "$relevantoutput" = "$relevantgolden" ]; then
			if [ "$debug" -eq 1 ]; then
				echo "$t Correct";
			fi
			corrects=`expr $corrects + 1`;
		else
			if [ "$debug" -eq 1 ]; then
				#echo "golden=$relevantgolden";
				#echo "actual=$relevantoutput";
				echo "$t Wrong";
			fi
			wrongs=`expr $wrongs + 1`;
		fi
	done
	export endtime=`date '+%s'`
	export totaltime=`expr $endtime - $starttime`
	echo $file $corrects $wrongs #$totaltime
done
