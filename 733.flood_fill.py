from collections import deque


class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == color:  # Otherwise we'll keep revisiting the same cells over and over
            return image

        m = len(image)  # The length of a row
        n = len(image[0])  # The length of a column

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))  # up, down, left, right

        q = deque([(sr, sc)])  # A queue with which we can perform BFS and gradually expand from each pixel
        color_to_change = image[sr][sc]  # Saving the initial color of the root pixel
        image[sr][sc] = color

        while q:
            r, c = q.popleft()  # Each element in the queue is a tupel with row and column as coordinates

            for dr, dc in directions:
                nr = r + dr  # New row
                nc = c + dc  # New column

                if 0 <= nr < m and 0 <= nc < n and image[nr][
                    nc] == color_to_change:  # We check whether the indeces are valid and the pixel is the color we want to change
                    image[nr][nc] = color  # Change the color
                    q.append((nr, nc))  # Append to the queue, so we cna expand from it further

        return image