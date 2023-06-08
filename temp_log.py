import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer
import pyqtgraph as pg
import serial
from pyqtgraph.Qt import QtCore

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a serial connection
        self.ser = serial.Serial('COM3', baudrate=115200,timeout=100)  # Replace '/dev/ttyUSB0' with the appropriate port

        # Create the main layout
        layout = QVBoxLayout()

        # Create the plot widget
        self.plot_widget = pg.PlotWidget()
        layout.addWidget(self.plot_widget)

        # Set the central widget and layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Initialize the plot
        self.plot = self.plot_widget.getPlotItem()
        self.plot.setLabel('left', 'Value')
        self.plot.setLabel('bottom', 'Time')

        # Create empty lists to store the data
        self.x_data = []
        self.y_data = []
        


    def update_plot(self):
        # Read a line of data from the serial port
        print('hi')
        temp1 = self.ser.readline().decode().strip()
        hum = self.ser.readline().decode().strip()
        temp2 = self.ser.readline().decode().strip()


        print(temp1)
        print(hum)
        print(temp2)

        # Split the line into x and y values (assuming comma-separated)
        #values = line.split(',')
        values = [12,14]
        if len(values) == 2:
            try:
                x = float(values[0])
                y = float(values[1])

                # Append the values to the data lists
                self.x_data.append(x)
                self.y_data.append(y)

                # Update the plot data
                self.plot.setData(self.x_data,self.y_data)

            except ValueError:
                pass
        else:
            print(values)



if __name__ == "__main__":
    # Create the Qt application
    app = QApplication(sys.argv)

    # Create the main window
    window = MainWindow()
    timer = QtCore.QTimer()
    timer.timeout.connect(window.update_plot)
    timer.start(50)
    window.show()

    # Run the Qt event loop
    sys.exit(app.exec())