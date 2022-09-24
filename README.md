# River Crossing-Problem by DLS

A river crossing puzzle is a type of puzzle in which the object is to carry items from one river bank to another, usually in the fewest trips.

![image](https://user-images.githubusercontent.com/47561760/192118582-f8f7f319-177a-4f55-a476-ab1388e05daf.png)

## Problem Definition

A father, a mother, two sons, two daughters, a thief, a policeman are on one side of the river and they want to cross it.

General conditions of the problem:
1. The maximum capacity of the boat is two people.
2. Only father, mother and police can drive the boat.
3. If the mother is not present in the boat, the girls cannot be with the father.
4. If the father is not present in the boat, the boys cannot be with the mother.
5. The thief cannot be with the family members without the presence of the police.
6. The police and mother and father can go to the other side of the river alone. (combination of two items is also possible)

# Result
| Boat Side     | Left Side People | Right Side People |
| ---      | --- | ----  |
|left|Boy-Boy-Father-Mother-Girl-Girl-Police-Thief||
|right|Boy-Boy-Father-Mother-Girl-Girl|Thief-Police|
|left|Boy-Boy-Father-Mother-Girl-Police-Girl|Thief|
|right|Boy-Boy-Father-Mother-Girl|Girl-Police-Thief|
|left|Boy-Boy-Thief-Police-Father-Mother-Girl|Girl|
|right|Boy-Boy-Thief-Police-Father|Girl-Girl-Mother|
|left|Boy-Boy-Thief-Police-Father-Mother|Girl-Girl|
|right|Boy-Boy-Thief-Police|Girl-Girl-Mother-Father|
|left|Boy-Boy-Father-Thief-Police|Girl-Girl-Mother|
|right|Boy-Boy-Father|Girl-Girl-Police-Thief-Mother|
|left|Boy-Boy-Father-Mother|Girl-Girl-Police-Thief|
|right|Boy-Boy|Girl-Girl-Mother-Police-Thief-Father|
|left|Boy-Boy-Father|Girl-Girl-Mother-Police-Thief|
|right|Boy|Girl-Girl-Father-Boy-Mother-Police-Thief|
|left|Thief-Police-Boy|Girl-Girl-Father-Boy-Mother|
|right|Thief|Girl-Girl-Father-Boy-Boy-Mother-Police|
|left|Thief-Police|Girl-Girl-Father-Boy-Boy-Mother|
|right||Police-Thief-Girl-Girl-Father-Boy-Boy-Mother|


Done in 8.646481037139893s
