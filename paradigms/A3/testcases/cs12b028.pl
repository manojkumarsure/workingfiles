ispresent(T,[T|_]).
ispresent(T,[_|Y]) :- ispresent(T,Y).
listintersect([H|T],Y) :- ispresent(H,Y);listintersect(T,Y).
checkconflict(X,T,[Y|Z],W) :- catch(conflict(X,Y),Catcher,fail);catch(conflict(Y,X),Ct,fail);listintersect(T,W);checkconflict(X,T,Z,W).
fun([],[],A,B,C,D,E,F,G,Ax,Bx,Cx,Dx,Ex,Fx,Gx,Wy,W) :- W=Wy.
fun([X|H],[T|L],A,B,C,D,E,F,G,Ax,Bx,Cx,Dx,Ex,Fx,Gx,Wy,W) :- 
(\+ checkconflict(X,T,A,Ax)),append(Ax,T,Ay),append(Wy,[a],Wx),fun(H,L,[X|A],B,C,D,E,F,G,Ay,Bx,Cx,Dx,Ex,Fx,Gx,Wx,W) ;
(\+ checkconflict(X,T,B,Bx)),append(Bx,T,By),append(Wy,[b],Wx),fun(H,L,A,[X|B],C,D,E,F,G,Ax,By,Cx,Dx,Ex,Fx,Gx,Wx,W) ;
(\+ checkconflict(X,T,C,Cx)),append(Cx,T,Cy),append(Wy,[c],Wx),fun(H,L,A,B,[X|C],D,E,F,G,Ax,Bx,Cy,Dx,Ex,Fx,Gx,Wx,W) ;
(\+ checkconflict(X,T,D,Dx)),append(Dx,T,Dy),append(Wy,[d],Wx),fun(H,L,A,B,C,[X|D],E,F,G,Ax,Bx,Cx,Dy,Ex,Fx,Gx,Wx,W) ; 
(\+ checkconflict(X,T,E,Ex)),append(Ex,T,Ey),append(Wy,[e],Wx),fun(H,L,A,B,C,D,[X|E],F,G,Ax,Bx,Cx,Dx,Ey,Fx,Gx,Wx,W) ;
(\+ checkconflict(X,T,F,Fx)),append(Fx,T,Fy),append(Wy,[f],Wx),fun(H,L,A,B,C,D,E,[X|F],G,Ax,Bx,Cx,Dx,Ex,Fy,Gx,Wx,W) ;
(\+ checkconflict(X,T,G,Gx)),append(Gx,T,Gy),append(Wy,[g],Wx),fun(H,L,A,B,C,D,E,F,[X|G],Ax,Bx,Cx,Dx,Ex,Fx,Gy,Wx,W) .
main(X,Y,W) :- fun(X,Y,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],W),!.