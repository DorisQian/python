"""
You are given the lengths for each side on a triangle. You need to find all three angles for this triangle. If the given side lengths cannot form a triangle (or form a degenerated triangle), then you must return all angles as 0 (zero). The angles should be represented as a list of integers in ascending order. Each angle is measured in degrees and rounded to the nearest integer number (Standard mathematical rounding).

triangle-angles
Input: The lengths of the sides of a triangle as integers.

Output: Angles of a triangle in degrees as sorted list of integers.

Example:

checkio(4, 4, 4) == [60, 60, 60]
checkio(3, 4, 5) == [37, 53, 90]
checkio(2, 2, 5) == [0, 0, 0]

How it is used: This is a classical geometric task. The ideas can be useful in topography and architecture. With this concept you can measure an angle without the need for a protractor.

Precondition: 
0 < a,b,c ≤ 1000

三角形的每边都有长度。你需要找到这个三角形的三个角。如果给定的边长度不能形成一个三角形(或者形成一个退化的三角形)，那么你必须返回所有的角为0(0)。角度应该以升序的整数形式表示。每个角都是用度数来测量的，并四舍五入到最接近的整数(标准的数学四舍五入)。

triangle-angles
输入:三角形的边长度为整数。

输出:一个三角形的角度，按顺序排列的整数。

如何使用:这是一个经典的几何任务。这些想法可以在地形和建筑方面很有用。有了这个概念，你可以测量一个角度而不需要量角器。
"""
def checkio(a, b, c):

    #replace this for solution
    return [0, 0, 0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"