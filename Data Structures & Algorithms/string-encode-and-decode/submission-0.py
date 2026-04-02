class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = [""]
        for s in strs:
            length = str(len(s))
            encoded.extend([length, "#", s])
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        l = r = 0
        while r < len(s):
            if s[r] == "#":
                length = int(s[l: r])
                start = r + 1
                end = start + length
                decoded.append(s[start: end])
                l = r = end
            else:
                r += 1
        return decoded
            
            