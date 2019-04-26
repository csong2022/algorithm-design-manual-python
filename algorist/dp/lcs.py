from algorist.dp.editdistance import EditDistance, MAXLEN


class LCS(EditDistance):
    """
    Longest common subsequence of two strings.
    """

    def match(self, c, d):
        return 0 if c == d else MAXLEN

    def match_out(self, s, t, i, j):
        if s[i] == t[j]:
            print("%c" % s.charAt(i), end='')
