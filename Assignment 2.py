# Assignment 2 CPSC 231 Fall 2026
# Name (ID): Samoinmon Ahchile (30309553), Md Samiul Haque (30332988)
# Tutorial: 02
# Samoinmon Ahchile did 50% and Md Samiul Haque did 50%

from SimpleGraphics import *
# Slection Menu to choose between bar chart and pie chart
print("Chart Creation Menu")
print("\t1. Bar Chart")
print("\t2. Pie Chart")
choice = int(input("Enter your choice (1 or 2): "))
# Bar Chart Creation
if choice == 1:
    #Set up Graph
    line(100,100,100,500)
    line(100,500,700,500)

    #Get inputs
    title = input("Enter title of Bar chart: ")
    barNum = int(input("Enter number of bars (2 to 6): "))
    gridLine = int(input("Enter gridline interval (10 to 100): "))
    labelY = input("Enter label for Y-Axis: ")

    #Set up graph for bars
    text(400,50,title,"c")
    text(50,300,labelY,"c")
    barWidth = 500/barNum
    barGap = 100/barNum
    gridText = gridLine
    gridY = 500 - gridLine
    gridX = 100

    #Make gridlines
    for i in range (1, int(400/gridLine) + 1):
        text(750, gridY, str(gridText), "c")
        line(100, gridY, 700, gridY)
        gridY -= gridLine
        gridText += gridLine

    #Make bars
    for i in range (1, int(barNum)+1):
        label = input("Label Bar " + str(i) + ": ")
        value = int(input("Enter the value of bar " + label + ": "))
        setFill((i*97)%256, (i*173+60)%256, (i*29+100)%256)
        rect(gridX + barGap, 500 - value, barWidth, value)
        text(gridX + barGap + barWidth/2, 520, label, "c")
        if (value < 40):
            text(gridX + barGap + barWidth/2, 500 - value - 10, str(value), "c")
        else:
            text(gridX + barGap + barWidth/2, 500 - value + 20, str(value), "c")
        gridX += barWidth + barGap
      
# Pie Chart Creation
if choice == 2:

    # Take inputs about the graph parameters
    title= input("Enter the title of the Pie chart: ")
    sectorNum= int(input("Enter the number of data points (2-6): "))
    sumOfSectors= int(input("Enter the sum of all data points: "))

    # Set up the initial angle and running total
    initialAngle= 0
    runningTotal= 0

    # set up title and legend location
    setFont("Times", 20, "bold")
    text(400, 80, title, "c")
    legendLocationY= 150

    # Loop through sectors and drawing the pie chart and legend
    for i in range(1, sectorNum, 1):
        secTitle= input("Enter the title of sector " + str(i) + ": ")
        secValue=int(input("Enter the value of sector " + secTitle + ": "))
        sizeOfSector= (secValue/sumOfSectors) * 360
        setFill((i*97)%256, (i*173+60)%256, (i*29+100)%256)
        pieSlice(250, 150, 300, 300, initialAngle, sizeOfSector)
        setFont("Times", 10, "bold")
        text(750, legendLocationY, secTitle, "c")
        setFill((i*97)%256, (i*173+60)%256, (i*29+100)%256)
        rect(740, legendLocationY+10, 20, 20)
        legendLocationY= legendLocationY + 40
        initialAngle= initialAngle + sizeOfSector
        runningTotal= runningTotal + secValue
    
    # calculate the last sector and draw it with legend
    lastSecTitle= input("Enter the title of sector " + str(sectorNum) + ": ")
    lastSector=sumOfSectors - runningTotal
    lastSizeOfSector= (lastSector/sumOfSectors) * 360
    setFill((sectorNum*97)%256, (sectorNum*173+60)%256, (sectorNum*29+100)%256)
    pieSlice(250, 150, 300, 300, initialAngle, lastSizeOfSector)
    setFont("Times", 10, "bold")
    text(750, legendLocationY, lastSecTitle, "c")
    setFill((sectorNum*97)%256, (sectorNum*173+60)%256, (sectorNum*29+100)%256)
    rect(740, legendLocationY+10, 20, 20)
print("Your chart has been created. Please check the graphics window.")