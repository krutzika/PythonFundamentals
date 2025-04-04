class LongestString:

    def get_length(self, a: str ) -> int:

        b= []
        c = 0
        max_length = 0
        for i, char in enumerate(a):
            while char in b:
                b.remove(char)
                c+=1
            b.append(char)
            max_length = max(max_length, i-c+1)
        return max_length

def main():
    longest_string = LongestString()
    a = "abbac"
    length = longest_string.get_length( a)
    print(length)

if __name__ == "__main__":
    main()