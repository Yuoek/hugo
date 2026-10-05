class Solution:
    def lengthLongestPath(self, input: str) -> int:
        i, n = 0, len(input)
        ans = 0
        stk = []
        while i < n:
            ident = 0
            while input[i] == '\t':
                ident += 1
                i += 1

            cur, isFile = 0, False
            while i < n and input[i] != '\n':
                cur += 1
                if input[i] == '.':
                    isFile = True
                i += 1
            i += 1

            # 栈深度大于当前层级，弹出
            while len(stk) > 0 and len(stk) > ident:
                stk.pop()

            if len(stk) > 0:
                cur += stk[-1] + 1  # +1 是路径分隔符 /

            if not isFile:
                stk.append(cur)
                continue

            ans = max(ans, cur)

        return ans

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    s1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    print(sol.lengthLongestPath(s1)) # 20
    s2 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print(sol.lengthLongestPath(s2)) #32
    s3 = "a"
    print(sol.lengthLongestPath(s3)) #0
