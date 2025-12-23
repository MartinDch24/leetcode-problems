class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        i1 = None   # The index of the 1st mismatch
        i2 = None   # The index of the 2nd mismatch

        for i, c in enumerate(s1):
            # Check for differences in s1 and s2 at every index
            if c != s2[i]:
                # If we have a mismatch, check if it's the first one
                if i1 != None:

                    # Check if this is the third mismatch
                    if i2 != None:
                        return False
                    else:
                        i2 = i
                        # Check if swapping i1 and i2 will make strings equal
                        if not (s1[i1] == s2[i] and s1[i] == s2[i1]):
                            return False
                else:
                    # We save the index of the first mismatch
                    i1 = i

         # Return True if we have no or 2 mismatches and their swap makes the strings equal
        return (i1 == None) or (i1 != None and i2 != None)