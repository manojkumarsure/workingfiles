(setq x1 -1)
(setq y 1)
(setq currmax 0)
(setq newmax 0)
(setq currIdx 0)
(setq offset 0)
(defun checkPrime(n d)
	(
		if(> n 1)
		(
			if (= d (+ 1 (floor (sqrt n)))) t
			(
				if (= 0 (rem n d))  nil (checkPrime n (+ d 1))
			)
		)
	)
)
(defun prime(n)
	(if (checkPrime n 2) (setq x1 n)  ())
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
(defun main(l)
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
;; (checkPrime 143433737 2)