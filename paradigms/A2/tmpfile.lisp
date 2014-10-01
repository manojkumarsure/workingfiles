(setq x1 -1)
(setq y 1)
(setq currmax 0)
(setq newmax 0)
(setq currIdx 0)
(setq offset 0)
(defun checkPrime(n)
(progn
	(setq d 2)
	(loop
		(when ( < n 1 ) (return 0))
		(when ( = n 2) (return 1))
		(when (= 0 (rem n d)) (return 0))
		(when (= d (+ 1 (floor (sqrt n)))) (return 1))
		(setq d (+ d 1))
	)
)
)
(defun prime(n)
	(if (= 1 (checkPrime n)) (setq x1 n)  ())
)
(defun primelist(l)
(
	progn
	(setq offset (+ 1 offset))
	(
		if (null (cdr l) )
		(
			progn
			(
				if (prime x1)
				(progn
				(setq y x1)
				(setq newmax (+ currIdx offset))
				)
			)
		)
		(
			progn
			(
				if (prime x1)
				(progn
				(setq y x1)
				(setq newmax (+ currIdx offset))
				)
			)
			(setq x1  (ap x1 (car (cdr l))))
			(primelist (cdr l))
		)
	)
)
)
(defun len(n)
	(
		if (= n (rem  n 10)) 1 (+ 1 (len (floor (/ n 10))) )
	)
)
(defun ap(n m)
	(
		+ (* n  (expt 10  (len m))) m
	)
)
(defun main(l)
	(
		if (null l) ()
		(
		progn
		(setq x1 (car l))
		(primelist l)
		(if(= y 1) nil (if (> newmax currmax) (progn (print y)(setq currmax newmax))))
		(setq y 1)
		(setq currIdx (+ 1 currIdx))
		(setq newmax 0)
		(setq offset 0)
		(	
			if(null (cdr l))
			nil
			(main(cdr l))
		)
		)
	)
)(setq x 'STARTUSEFUL)
(main (list 103 577 8440))
(setq x 'ENDUSEFUL)
