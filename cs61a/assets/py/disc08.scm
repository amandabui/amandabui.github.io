

> (+ 1 2 (- 3 4))
Pair('+', Pair(1, Pair(2, Pair(
	Pair('-', Pair(3, Pair(4, nil))), nil))))

> (+ 1 (* 2 3) 4)
Pair('+', Pair(1, Pair(
	Pair('*', Pair(2, Pair(3, nil))),
	Pair(4, nil))))

>>> Pair('+', Pair(1, Pair(2, Pair(3, Pair(4, nil)))))
(+ 1 2 3 4)

>>> Pair('+', Pair(1, Pair(Pair('*', Pair(2, Pair(3, nil))), nil)))
(+ 1 (* 2 3))


# In Python iteratively:
def fib(n):
	previous = 0
	current = 1
	while n != 0:
		previous, current = 
			current, previous + current
		n = n - 1
	return previous




(define (fib n) 
	(define (fib-sofar i prev curr )
		(if (= i 0))
			prev
			(fib-sofar (- i 1) curr (+ prev curr))
	)
	(fib-sofar n 0 1)
)

(define (sum lst)
	(define (sum-sofar total lst)
		(if (null? lst)
			total
			(sum-sofar (+ total (car lst)) (cdr lst))
		)
	)
	(sum-sofar 0 lst)
)

