# http://www.quora.com/Dynamic-Programming-DP/How-can-one-start-solving-Dynamic-Programming-problems
# http://www.quora.com/Dynamic-Programming-DP/Are-there-any-good-resources-or-tutorials-for-dynamic-programming-besides-the-TopCoder-tutorial
# http://www.quora.com/Dynamic-Programming-DP/What-are-systematic-ways-to-prepare-for-dynamic-programming
# http://www.quora.com/Competitive-Programming/Where-can-I-find-good-problems-to-practice-recursion-topdown-approach


*writes down "1+1+1+1+1+1+1+1 =" on a sheet of paper*
"What's that equal to?"
*counting* "Eight!"
*writes down another "1+" on the left*
"What about that?"
*quickly* "Nine!"
"How'd you know it was nine so fast?"
"You just added one more"

"So you didn't need to recount because you remembered there were eight! Dynamic
"Programming is just a fancy way to say 'remembering stuff to save time later'

=====================================
NOTE: All DPs can be (re)formulated as recursion. The extra effort you put in in
finding out what is the underlying recursion will go a long way in helping you
in future DP problems.
=====================================

|STEP1:| Imagine you are GOD. Or as such, you are a third-person overseer of the
problem.

|STEP2:| As God, you need to decide what choice to make. Ask a decision
question.

|STEP3:| In order to make an informed choice, you need to ask "what
variables would help me make my informed choice?". This is an important step and
you may have to ask "but this is not enough info, so what more do I need" a few
times.

|STEP4:| Make the choice that gives you your best result.

=====================================
In the above, the variables alluded to in
Step3 are what is generally called the "state" of your DP. The decision in Step2
is thought of as "from my current state, what all states does it depend upon?"


EXAMPLES:
------------
Q. Given an array, find the largest sum along a contiguous segment of it. Simple
enough, and you probably know the answer, but lets see what the 4 steps amount
to.
------------
Step1: I am an overseer (just a psychological step)

Step2: I go through the
array, and ask, "does the largest sum begin at this point?"

Step3: I need to
know what is the largest sum that begins at the next point, in order to decide
if it can be extended or not.

Step4: I either extend it to the next point, or I
cut it off here: f(i) = max(arr[i], arr[i] + f(i+1)).

The above particular example was demonstrated to me by a friend and prior to his
demonstration (of how easy DP is), I was completely baffled by DPs myself.

------------
Q. I have a set of N jobs, and two machines A and B. Job i takes A[i] time on
machine A, and B[i] time on machine B. What is the minimum amount of time I need
to finish all the jobs?
------------
Step1: I am the overseer (this problem lends itself more
naturally to being "God").

Step2: I go through jobs from 1 to N, and have to
decide on which machine to schedule job i.

Step3: If I schedule the job on
machine A, then I then have a load of A[i] + best way to schedule the remaining
jobs. If its on B, then I have a load of B[i] + best way to schedule the
remaining jobs. But wait! "best way to schedule remaining jobs" doesn't account
for the fact that the i'th job will potentially interfere. Thus, I need to
infact also pass on the "total load" on each machine in order to make my
informed choice. Therefore, I need to modify my question to: "Given that the
current load on A is a, and on B is b, and I have to schedule jobs i to N, what
is the best way to do so?"

Step4:
f(a, b, i) = { min(a, b) : i == N+1,
          else min(f(a + A[i], b, i+1), f(a, b + B[i], i+1): i <= N}.

Final answer is in f(0, 0, 1).
