#!/bin/bash

tmpfile='tmpfile.lisp';
startmark='STARTUSEFUL';
endmark='ENDUSEFUL';
debug=1;
timeout="600s";

for orifile in `ls -1 [cC][sS]*[bB]*.[lL][iI][sS][pP]`; do
	export file=`echo $orifile | tr 'a-z' 'A-Z' | sed 's/.LISP//'`;
	if [ "$debug" -eq 1 ]; then
		echo Student = $file;
	fi
	# mv $orifile $file.lisp
	export corrects=0;
	export wrongs=0;
	
	export starttime=`date '+%s'`
	for t in {1..20}; do
		export testfile="t$t.test"
		#echo $testfile;
		cp $orifile 			   $tmpfile;
		echo "(setq x '$startmark)" 	>> $tmpfile;
		cat $testfile 			>> $tmpfile;
		echo "(setq x '$endmark)" 	>> $tmpfile;

		export output=`timeout $timeout clisp $tmpfile`; 
		export relevantoutput=`echo $output | sed "s/.*$startmark//" | sed "s/$endmark.*//" | sed 's/(.*)//' | sed 's/^[ ]*//' | sed 's/[ ]*$//'`

		export golden=`cat a$t.answer | sed 's/^[ ]*//' | sed 's/[ ]*$//'`;
		export relevantgolden=`echo $golden`;
		if [ "$relevantoutput" = "$relevantgolden" ]; then
			if [ "$debug" -eq 1 ]; then
				echo "$t Correct";
			fi
			corrects=`expr $corrects + 1`;
		else
			if [ "$debug" -eq 1 ]; then
				echo "$t Wrong";
			fi
			wrongs=`expr $wrongs + 1`;
		fi
	done
	export endtime=`date '+%s'`
	export totaltime=`expr $endtime - $starttime`
	echo $file $corrects $wrongs $totaltime
done
