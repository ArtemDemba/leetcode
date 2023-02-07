"""https://leetcode.com/problems/flood-fill/?envType=study-plan&id=level-1"""


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        old_color = image[sr][sc]
        image[sr][sc] = color
        is_checked = {
            (sr, sc): True
        }

        def recurse(y: int, x: int):
            for temp_y in range(y - 1, y + 2, 2):
                if temp_y < 0:
                    continue
                try:
                    if (temp_y, x) in is_checked:
                        continue
                    if image[temp_y][x] == old_color:
                        is_checked[(temp_y, x)] = True
                        image[temp_y][x] = color
                        recurse(temp_y, x)
                except IndexError:
                    continue
            for temp_x in range(x - 1, x + 2, 2):
                if temp_x < 0:
                    continue
                try:
                    if (y, temp_x) in is_checked:
                        continue
                    if image[y][temp_x] == old_color:
                        is_checked[(y, temp_x)] = True
                        image[y][temp_x] = color
                        recurse(y, temp_x)
                except IndexError:
                    continue
        recurse(sr, sc)
        return image


s = Solution()
image = [[0, 0, 0], [0, 1, 1]]
sr = 1
sc = 1
color = 2
print(s.floodFill(image, sr, sc, color))
