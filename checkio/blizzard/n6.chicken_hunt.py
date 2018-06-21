'''
"It is plain indeed that in spite of later estrangement Hobbits are relatives of ours: far nearer to us than Elves, or even than Dwarves. Of old they spoke the languages of Men, after their own fashion, and liked and disliked much the same things as Men did. But what exactly our relationship is can no longer be discovered."

"Hobbits are an unobtrusive but very ancient people, more numerous formerly than they are today; for they love peace and quiet and good tilled earth: a well-ordered and well-farmed countryside was their favourite haunt."

-- "The Lord of the Rings" J.R.R.Tolkien
Two Hobbits are trying to catch a chicken in the yard. It should be an easy task, but these two neighbours never seem to get along. Now a chicken got loose and they need to catch it, but they refuse to talk to each other. So, we need to find an algorithm which will work for the both of the Hobbits independently, allowing either of them to catch a chicken without walking into a fence, tree or each other. One last thing, Hobbits cannot run or wait forever. After all. catching the chicken is important, but Hobbits must adhere to their strict dinner schedule.

You are given a yard map as a sequence of strings where:
- "." is an empty cell;
- "I" is managed Hobbit;
- "S" is companion;
- "C" is chicken (our target);
- "X" is obstacle (a tree, a rock etc)

The yard is surrounded by a fence.

The chicken and Hobbits can move in 8 direction into neighbouring cells (including diagonals). And they can wait and stay in one place for a while. Actions are described with the following strings:
- "N" north, "S" south, "W" west, "E" east;
- "NW" north-west, "NE" north-east, "SW" south-west, "SE" south-east;
- "" (empty string) is to wait.

The Chicken is unpredictable and can use various tactics (including random movement), but he can not go out of the yard. Hobbits can not run in obstacles or in fences. And they should not struck each other, even for the final jump by the chicken.

Now for the tricky part. Your function will be called twice in each step - once for the first Hobbit and once for the second Hobbit. The Hobbits cannot communicate with each other and make their moves simultaneously. So be careful with moving both Hobbits into one square. You should move a Hobbit into the chickens square to win, but only one should make the move as two hobbits entering the same cell would count as them colliding. The Hobbits and the chicken move simultaneously, so if you just jump to a cell where is chicken, then is not guaranteed that you will catch it. Since dinner time is coming soon for the Hobbits, you have no more 100 moves to catch the chicken.

This is a "multicall" mission and your function will be called until you win or lose. Each cycle of steps is running in a new environment, so you can use global variables between steps, but for the new "hunt" they will be reseted..

map
This map will be looked little different for each function call:

 First       Second
"......",   "......",
".I.XX.",   ".S.XX.",
"...CX.",   "...CX.",
".XX.X.",   ".XX.X.",
"...S..",   "...I..",
"......",   "......",

    
Input: A yard map as a tuple of strings. Your function is called twice for each step.

Output: The action as a string. One of ("N", "S", "W", "E", "NW", "NE", "SW", "SE", "S").

Example:

hunt(("......",
      ".I.XX.",
      "...CX.",
      ".XX.X.",
      "...S..",
      "......")) # return an action
    
How it is used: This concept is using for automated robots which should work as a team without needing a direct connection, like factory manufacturing robots or Cylons. These robots and AI should be complex enough to "think" about and predict the actions of other objects.

Precondition:
3 < len(yard) ≤ 10
all(3 < len(row) ≤ 10 and len(row) == len(yard[0]) for row in yard)
'''