def main():
    try:
        file = open("video.dat", 'r')
        total_video = 0.0
        for line in file:
            num = float(line)
            total_video += num
        # print("total_length: ", total_video)

    except IOError:
        print("An error occured while reading the file")
    except ValueError:

        print("no numeric data found in the file")
    else:
        print("total_length: ", total_video)

    finally:
        print("file is closing")
        file.close()


main()
