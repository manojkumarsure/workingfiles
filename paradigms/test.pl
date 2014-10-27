butlast(X,Y) :- X=[A],Y=[].
butlast(X,Y) :- [H|T]=X,butlast(T,Z),Y=[H|Z].