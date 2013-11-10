:- style_check(-singleton).


b_write(Line) :- writeln(Line),nl,
  flush_output.
b_writen(Line) :- write(Line).

b_write(FS, Par) :- format(FS, Par),
  nl,
    flush_output.


crack:-
  getenv('omfg', InsuranceNumber),
  b_random_password(InsuranceNumber, Password),
  b_writen(Password),
  halt.

b_random_password(Username, Password) :-
  libSecureRandom_randomHex(Username, 16, Password).

libSecureRandom_randomHex(U, I, P) :-
  libSecureRandom_randomHex(U, I, P, 1).

libSecureRandom_randomHex(U, I, P, C) :-
   atom_codes(U, []),
  !,
    set_random(seed(C)),
    libSecureRandom_randomHex(I, D),
    atom_codes(P, D).

libSecureRandom_randomHex(U, I, P, C) :-
    atom_codes(U, [N|R]),
    D is C + N,
    atom_codes(V, R),
    libSecureRandom_randomHex(V, I, P, D).
    libSecureRandom_randomHex(0, []) :- !.
    libSecureRandom_randomHex(I, [C|R]) :-
    N is random(16),
    ( N > 9 -> C is N + 55 ; C is N + 48  ),
    succ(J, I),
    libSecureRandom_randomHex(J, R).
