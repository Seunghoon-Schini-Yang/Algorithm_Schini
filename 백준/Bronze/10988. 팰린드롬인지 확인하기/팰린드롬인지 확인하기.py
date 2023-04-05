def main(word):
    for i in range(len(word)>>1):
        if word[i] != word[~i]:
            return 0
    return 1
    
    
if __name__ == '__main__':
    ans = main(input())
    print(ans)