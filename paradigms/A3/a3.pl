ispresent(T,[T|_]).
ispresent(T,[_|Y]) :- ispresent(T,Y).
listintersect([H|T],Y) :- ispresent(H,Y);listintersect(T,Y).
checkconflict(X,T,[Y|Z],W) :- conflict(X,Y);conflict(Y,X);listintersect(T,W);checkconflict(X,T,Z,W).
fun([],[],A,B,C,D,E,F,G,Ax,Bx,Cx,Dx,Ex,Fx,Gx) :- write(A),write(B),write(C),write(D),write(E),write(F),write(G).
fun([X|H],[T|L],A,B,C,D,E,F,G,Ax,Bx,Cx,Dx,Ex,Fx,Gx) :- (\+ checkconflict(X,T,A,Ax)),append(Ax,T,Ay),fun(H,L,[X|A],B,C,D,E,F,G,Ay,Bx,Cx,Dx,Ex,Fx,Gx) ;
													   (\+ checkconflict(X,T,B,Bx)),append(Bx,T,By),fun(H,L,A,[X|B],C,D,E,F,G,Ax,By,Cx,Dx,Ex,Fx,Gx) ;
													   (\+ checkconflict(X,T,C,Cx)),append(Cx,T,Cy),fun(H,L,A,B,[X|C],D,E,F,G,Ax,Bx,Cy,Dx,Ex,Fx,Gx) ;
													   (\+ checkconflict(X,T,D,Dx)),append(Dx,T,Dy),fun(H,L,A,B,C,[X|D],E,F,G,Ax,Bx,Cx,Dy,Ex,Fx,Gx) ; 
													   (\+ checkconflict(X,T,E,Ex)),append(Ex,T,Ey),fun(H,L,A,B,C,D,[X|E],F,G,Ax,Bx,Cx,Dx,Ey,Fx,Gx) ;
													   (\+ checkconflict(X,T,F,Fx)),append(Fx,T,Fy),fun(H,L,A,B,C,D,E,[X|F],G,Ax,Bx,Cx,Dx,Ex,Fy,Gx) ;
													   (\+ checkconflict(X,T,G,Gx)),append(Gx,T,Gy),fun(H,L,A,B,C,D,E,F,[X|G],Ax,Bx,Cx,Dx,Ex,Fx,Gy) .
main(X,Y) :- fun(X,Y,[],[],[],[],[],[],[],[],[],[],[],[],[],[]).