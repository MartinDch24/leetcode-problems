class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split each version by revision and convert the revisions to integers to be able to compare them and remove leading 0s
        revs1 = [int(rev) for rev in version1.split(".")]
        revs2 = [int(rev) for rev in version2.split(".")]

        # We loop over the longer version and take 0 for the revisions of the 2nd version that don't exist
        n = max(len(revs1), len(revs2))

        for i in range(n):
            v1 = revs1[i] if i < len(revs1) else 0
            v2 = revs2[i] if i < len(revs2) else 0

            if v1 != v2:
                return 1 if v1 > v2 else -1

        return 0