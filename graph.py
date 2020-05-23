# Program for plotting the graph for comparing the algorithms

import matplotlib.pyplot as plt

# Values for MD5
x1 = range(4, 49, 4)
y1 = [4.23274040222168E-05, 7.5969934463501E-05, 0.000363713741302,
      0.001378767967224, 0.005347669363022, 0.021734683990479,
      0.091323490858078, 0.379030643224716, 2.1482998418808,
      7.01985987186432, 28.598748178, 84.2786835275]
# plotting the MD5 points
plt.plot(x1, y1, label="MD5")

# Values for SHA-1
x2 = range(4, 49, 4)
y2 = [5.0157970852322E-05, 0.000145072407193, 0.001477119657728,
      0.001337561607361, 0.006334042549133, 0.026065371990204,
      0.102867744922638, 0.488515527963638, 2.19540992736816,
      9.11998206853867, 35.3046548366547, 106.715069830418]
# plotting the SHA-1 points
plt.plot(x2, y2, label="SHA-1")

# Values for SHA-256
x3 = range(4, 49, 4)
y3 = [5.23247718811035E-05, 0.000137008666992, 0.000348737504747,
      0.001669829156664, 0.006522273752424, 0.026779025130802,
      0.112133940590753, 0.415944425794813, 2.06295880476634,
      8.23789692454868, 28.734085811509, 128.827531788084]
# plotting the SHA-256 points
plt.plot(x3, y3, label="SHA-256")

# Values for SHA-512
x4 = range(4, 49, 4)
y4 = [6.74827098846436E-05, 9.22646522521973E-05, 0.000430134296417,
      0.001465956449509, 0.005994033575058, 0.026638387918472,
      0.102476279258728, 0.427343961238861, 1.7890253226757,
      7.34159641265869, 37.1885885763168, 225.130336006482]
# plotting the SHA-512 points
plt.plot(x4, y4, label="SHA-512")


# naming the x axis
plt.xlabel('Number of bits')
# naming the y axis
plt.ylabel('Time (in seconds)')

# setting the scale of x-axis
plt.xticks(range(4, 49, 4))
# giving a title to my graph
plt.title('Performance comparison of algorithms')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()
