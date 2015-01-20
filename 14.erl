-module(collatz).
-export([cl/1, len/1, zergrush/2, most/1]).

cl(N) when N rem 2 == 0 -> N div 2;
cl(N) -> 3*N+1.

len(N) when N == 1 -> 1;
len(N) -> 1 + len(cl(N)).

gt(A, B) when A > B -> A;
gt(A, B) -> B.

most(CURRENT) ->
   receive
      {VAL, MAX} when VAL > CURRENT ->
         io:format("~p:~p~n", [MAX, VAL]),
         most(gt(VAL, CURRENT));
      {VAL, MAX} -> 
         most(gt(VAL, CURRENT));
      _ -> io:format("finished~n")
   end.

zergrush(ACC, 1) -> 1;
zergrush(ACC, MAX) ->
   F = fun() ->
         receive
            {ACC, V} -> 
               ACC ! {len(V), MAX}
         end
       end,
   PID = spawn(F),
   PID ! {ACC, MAX},
   zergrush(ACC, MAX-1).
