def main():

    #     file = open('video.dat', 'w')
    #     num_video = int(input("Enter the number of videos: > "))
    #     print("Enter the runing time for each video")
    #     for count in range(1, num_video+1):
    #         run_time = float(input("video#"+str(count) + ": "))
    #         file.write(str(run_time)+'\n')
    #     file.close()
    file = open('video.dat', 'r')
    total_time = 0
    for line in file:
        print(line.rstrip('\n'))
        total_time += float(line)
    print(total_time)


main()
