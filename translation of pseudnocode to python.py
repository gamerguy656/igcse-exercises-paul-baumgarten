N = input()
set flag = true
for Q from 2 to ( round_up( squareroot(N) )) do
   if N % Q == 0 then
      set flag = false
   end if
end for
if flag = true:
   print("yes")
else
   print("no")
