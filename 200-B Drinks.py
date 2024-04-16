def main():
    n = int(input())  
    volumes = list(map(int, input().split()))  

    total_volume = sum(volumes)  
    average_volume = total_volume / n  

    print(average_volume)

main()  
