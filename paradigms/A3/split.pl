splitx([],X,Y,P,N) :- X=P ,Y=N.
splitx([H|X],P,N,P2,N2) :- H >=0 , splitx(X,[H|P],N,P2,N2) ; H <0 ,splitx(X,P,[H|N],P2,N2).
split(X,Y,Z) :- splitx(X,[],[],Y,Z).