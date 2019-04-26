/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sensorplot;

import java.time.OffsetDateTime;
import java.util.function.*;

/**
 *
 * @author MobMonRob
 */
public class SensorPlot {

    Plot plot;
    SensorDataProcessor sensorDataProcessor;

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        SensorPlot sensorPlot = new SensorPlot();
        sensorPlot.init();
    }

    public SensorPlot() {
        plot = new Plot();
        sensorDataProcessor = new SensorDataProcessor();
    }

    public void init() {
        System.out.println("SensorPlot.init()");

        plot.display();
        sensorDataProcessor.init();
    }

    public void loop() {
        DataPointCoordinatesList allDataPointCoordinates = new DataPointCoordinatesList();

        while (true) {
            allDataPointCoordinates.addDataPoint(sensorDataProcessor.getNextDataPoint());
            plot.updateDatePointCoordinatesList(allDataPointCoordinates);
            plot.repaint();
        }
    }
}
