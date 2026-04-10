class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for s in strs:
            # string length + # + string ex:4#12342#31
            encode_str += str(len(s)) + "#" + s
        return encode_str

    def decode(self, s: str) -> List[str]:
        # num before # is the length of the following words
        decode_list = []
        i = 0
        while i < len(s):
            # find the seperator #
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            sub_list = s[j+1: j+1+length]
            decode_list.append(sub_list)
            i = j+1+length
        return decode_list