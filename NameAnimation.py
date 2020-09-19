import os
import math
import imageio
import pandas as pd
import matplotlib.pyplot as plt


def main():
    path = 'D:/_UltraLearning/2020/9.2020/NameAnimation/Data/Reference.xlsx'
    values_list = pd.read_excel(path).values.tolist()

    # Extract coordinate position from
    # Excel file
    name_data = []
    for my_list in values_list:
        for point in my_list:
            if not pd.isna(point):
                name_data.append(point)

    # Make name into X and Y lists
    x,y = [],[]
    for point in name_data:
        point_x, point_y = int(point.split(',')[0]), int(point.split(',')[1])
        if point_y > 6:
            point_x += 2
        x.append(point_x)
        y.append(point_y)

    # Make our graph
    for i in range(0,len(x)):
        build_plot(x[:i], y[:i], i, additional_points=int(len(x)-i*1.25))

    # Make our animation!
    img_path = 'D:/_UltraLearning/2020/9.2020/NameAnimation/Figures/NameAnimation/'
    file_destination = 'D:/_UltraLearning/2020/9.2020/NameAnimation/Figures'
    create_gif(35.7, img_path, file_destination)

def build_plot(x,y, count, additional_points=0, length=105):

    plt.plot(figsize=(17,17))
    plt.xlim([-1, 17])
    plt.ylim([-1, 17])
    plt.axis('off')

    # Bottom Helix Animation
    plt.plot([i for i in range(0, additional_points)],
             [.5 * math.cos(i+math.pi/2) for i in range(0, additional_points)],
                color='#03FFDC', alpha=0.5)
    plt.plot([i for i in range(0, additional_points)],
             [.5 * math.sin(i) for i in range(0, additional_points)],
                color='#03FFDC', alpha=0.5)

    plt.scatter(x, y, color='#FF95C6')

    plt.savefig("D:/_UltraLearning/2020/9.2020/NameAnimation/Figures/NameAnimation/" +
                str(count), facecolor='black')
    print('Saved Figure: ', str(count))

    linecount = count

    lw = 4          # The width of our lines
    lc = '#03FFDC'  # The color of our lines
    a = 0.03        # The opacity of our lines

    # Draw out the name!
    if count == length:

        # First Names!
        xdataB, ydataB, = [], [],
        x_1dataB, x_2dataB = [2], [2]
        y_1dataB,y_2dataB = [13], [13]

        xdataI, ydataI = [], []

        xdataL1, ydataL1 = [], []

        xdataL2, ydataL2 = [], []

        xdataY, ydataY  =  [], []
        x_1dataY, x_2dataY = [14], [14]
        y_2dataY = [13]

        # Last Names!

        x_1dataH, y_1dataH = [], []
        x_2dataH, y_2dataH = [], []

        x_1dataA, y_1dataA = [], []
        x_2dataA, y_2dataA = [], []
        x_3dataA, y_3dataA = [], []

        xdataY2, ydataY2, = [], [],
        x_1dataY2, x_2dataY2 = [9], [9]
        y_2dataY2 = [3]

        xdataE, ydataE = [], []
        x_1dataE, y_1dataE = [], []
        x_2dataE, y_2dataE = [], []

        xdataS, ydataS = [], []


        for i in range(1,100+1):

            ## FIRST NAME ##

            # B, FN
            line, = plt.plot(0, 0, color=lc, linewidth=lw, alpha=a)
            line1, = plt.plot(0, 0, color=lc, linewidth=lw, alpha=a)
            line2, = plt.plot(0, 0, color=lc, linewidth=lw, alpha=a)
            # Making the curve in the 'B'!
            if i < 8:
                xdataB.append(2)
                ydataB.append(i + 9)
            elif i == 8:
                x_1dataB.append(3)
                x_2dataB.append(3)
                y_1dataB.append(13)
                y_2dataB.append(13)

            elif i <= 10:
                x_1dataB.append(4)
                x_2dataB.append(4)
                y_1dataB.append(5+i)
                y_2dataB.append(21-i)
            elif i <= 12:
                x_1dataB.append(14-i)
                x_2dataB.append(14-i)
                y_1dataB.append(16)
                y_2dataB.append(10)
            line.set_xdata(xdataB), line.set_ydata(ydataB)
            line1.set_xdata(x_1dataB), line1.set_ydata(y_1dataB)
            line2.set_xdata(x_2dataB), line2.set_ydata(y_2dataB)



            # I, FN
            line, = plt.plot(0, 0, color=lc, linewidth=lw, alpha=a)
            if i < 6:
                xdataI.append(6)
                ydataI.append(i + 9)
            if i > 8:
                # Dot the "i"
                plt.scatter(6, 16, color=lc, alpha=((a*i)/(a+i)))
            line.set_xdata(xdataI), line.set_ydata(ydataI)



            # L1, FN
            line, = plt.plot(0, 0, color=lc, linewidth=lw, alpha=a)
            if i <= 2:
                xdataL1.append(10 - i)
                ydataL1.append(10)
            if i > 2 and i < 8:
                xdataL1.append(8)
                ydataL1.append(i + 9)
            line.set_xdata(xdataL1), line.set_ydata(ydataL1)



            # L2, FN
            line, = plt.plot(0, 0, color=lc, linewidth=lw, alpha=a)
            if i <= 2:
                xdataL2.append(13 - i)
                ydataL2.append(10)
            if i > 2 and i < 8:
                xdataL2.append(11)
                ydataL2.append(i + 9)
            line.set_xdata(xdataL2), line.set_ydata(ydataL2)



            # Y, FN
            line, = plt.plot(0, 0, color=lc, linewidth=lw, alpha=a)
            line1, = plt.plot(0, 0, color=lc, linewidth=lw, alpha=a)
            line2, = plt.plot(0, 0, color=lc, linewidth=lw, alpha=a)
            if i < 5:
                xdataY.append(14)
                ydataY.append(i + 9)
            if i >= 5 and i < 8:
                x_1dataY.append(13)
                x_2dataY.append(15)
                y_2dataY.append(i + 9)
            line.set_xdata(xdataY), line.set_ydata(ydataY)
            line1.set_xdata(x_1dataY), line1.set_ydata(y_2dataY)
            line2.set_xdata(x_2dataY), line2.set_ydata(y_2dataY)



            ## LAST NAME ##

            # H, LN
            line, = plt.plot(0, 0, color=lc, linewidth=lw, alpha=a)
            line1, = plt.plot(0, 0, color=lc, linewidth=lw, alpha=a)
            if i <= 4:
                x_1dataH.append(0)
                y_1dataH.append(i - 1)

                x_2dataH.append(2)

            elif i > 4 and i <= 6:
                x_1dataH.append(i-4)
                y_1dataH.append(3)

                x_2dataH.append(6-i)


            elif i >= 7 and i < 10:
                x_1dataH.append(2)
                y_1dataH.append(i-3)

                x_2dataH.append(0)

            line.set_xdata(x_1dataH), line.set_ydata(y_1dataH)
            line1.set_xdata(x_2dataH), line1.set_ydata(y_1dataH)

            # A, LN
            line, = plt.plot(0, 0, color=lc,  linewidth=lw, alpha=a)
            line2, = plt.plot(0, 0, color=lc, linewidth=lw, alpha=a)
            line3, = plt.plot(0, 0, color=lc, linewidth=lw, alpha=a)
            if i <= 7:
                x_1dataA.append(4)
                y_1dataA.append(i-1)

                x_2dataA.append(6)
                y_2dataA.append(i-1)

            if i >= 4 and i <= 6:
                x_3dataA.append(i)
                y_3dataA.append(3)

            if i > 7 and i <= 9:
                x_1dataA.append(i-3)
                y_1dataA.append(6)

                x_2dataA.append(13-i)
                y_2dataA.append(6)
            line.set_xdata(x_1dataA), line.set_ydata(y_1dataA)
            line2.set_xdata(x_2dataA), line2.set_ydata(y_2dataA)
            line3.set_xdata(x_3dataA), line3.set_ydata(y_3dataA)

            # Y, LN
            line, = plt.plot(0, 0, color=lc, linewidth=lw, alpha=a)
            line1, = plt.plot(0, 0, color=lc, linewidth=lw, alpha=a)
            line2, = plt.plot(0, 0, color=lc, linewidth=lw, alpha=a)
            if i < 5:
                xdataY2.append(9)
                ydataY2.append(i -1)
            if i >= 5 and i < 8:
                x_1dataY2.append(8)
                x_2dataY2.append(10)
                y_2dataY2.append(i -1)
            line.set_xdata(xdataY2), line.set_ydata(ydataY2)
            line1.set_xdata(x_1dataY2), line1.set_ydata(y_2dataY2)
            line2.set_xdata(x_2dataY2), line2.set_ydata(y_2dataY2)

            # E, LN

            line, = plt.plot(0, 0, color=lc, linewidth=lw, alpha=a)
            line1, = plt.plot(0, 0, color=lc, linewidth=lw, alpha=a)
            line2, = plt.plot(0, 0, color=lc, linewidth=lw, alpha=a)

            if i <= 7:
                xdataE.append(12)
                ydataE.append(i-1)

            elif i == 8:
                xdataE.append(13)
                ydataE.append(6)

            if i <= 2:
                x_1dataE.append(i + 11)
                y_1dataE.append(0)

            if i > 3 and i <= 5:
                x_2dataE.append(i + 8)
                y_2dataE.append(3)

            line.set_xdata(xdataE), line.set_ydata(ydataE)
            line1.set_xdata(x_1dataE), line1.set_ydata(y_1dataE)
            line2.set_xdata(x_2dataE), line2.set_ydata(y_2dataE)

            # S, LN
            line, = plt.plot(0, 0, color=lc, linewidth=lw, alpha=a)

            if i <= 2:
                xdataS.append(i + 14)
                ydataS.append(0)
            elif i <= 5:
                pass
                xdataS.append(16)
                ydataS.append(i-2)
            elif i <= 8:
                xdataS.append(15)
                ydataS.append(i - 2)
            elif i == 9:
                xdataS.append(16)
                ydataS.append(6)

            line.set_xdata(xdataS), line.set_ydata(ydataS)


            print('Saved Figure: ', str(linecount + i))

            plt.savefig("D:/_UltraLearning/2020/9.2020/NameAnimation/Figures/NameAnimation/" +
                        str(linecount + i), facecolor='black')
    plt.clf()

def create_gif(fps, img_path,destination, name='/animation'):

    images = []
    file_names = os.listdir(img_path)
    files = sorted([int(file.split('.')[0]) for file in file_names])
    for file in files:
        # Read the image of each picture
        images.append(imageio.imread(img_path + str(file) + ".png"))

        print("Incorporated sim:", file)
    # Save it as a gif!
    imageio.mimsave(destination + name +'.gif', images,
                     fps=fps, loop=1)

main()


# Accomplished with reference to:

# https://www.codespeedy.com/how-to-convert-dataframe-into-list-using-python/
# https://html-color-codes.info/colors-from-image/
# https://matplotlib.org/3.1.0/gallery/color/color_demo.html#sphx-glr-gallery-color-color-demo-py