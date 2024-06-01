def max_earnings(m,n,prices):
    prices.sort()
    max_earnings=0
    for i in range(min(m,n)):
        if prices[i] < 0:
            max_earnings -= prices[i]
    return max_earnings

def main():
    n,m= map(int,input().split())
    prices = list(map(int,input().split()))
    earnings= max_earnings(n,m,prices)
    print(earnings)
if __name__ =="__main__":
    main()