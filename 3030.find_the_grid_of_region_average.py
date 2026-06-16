class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        # total[i][j] is the total sum of the average intensity of the regions to which image[i][j] belongs to
        total = [[0] * n for _ in range(m)]
        # count[i][j] is how many regions does image[i][j] belong to
        count = [[0] * n for _ in range(m)]

        for i in range(m - 2):
            for j in range(n - 2):
                valid = True
                s = 0
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if k > i and abs(image[k][l] - image[k-1][l]) > threshold:
                            valid = False
                        if l > j and abs(image[k][l] - image[k][l-1]) > threshold:
                            valid = False
                        s += image[k][l]
                if not valid:
                    continue

                avg = s // 9
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        total[k][l] += avg
                        count[k][l] += 1

        return [
            [total[i][j] // count[i][j] if count[i][j] else image[i][j]
             for j in range(n)]
            for i in range(m)
        ]