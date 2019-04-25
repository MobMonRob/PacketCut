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

    SensorDataReceiver sensorDataReceiver;

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        SensorPlot sensorPlot = new SensorPlot();
        sensorPlot.init();
    }

    public void init() {
        System.out.println("SensorPlot.init()");
        
        Plot plot = new Plot();
        plot.testPlot();
        
        // /*
        sensorDataReceiver = SensorDataReceiver.createStandardReceiver();
        sensorDataReceiver.connect();

        Consumer<String> dataPointStringConsumer = dataPointString -> {
            DataPoint dataPoint = SensorDataParser.parse(dataPointString, OffsetDateTime.now());
            System.out.println(dataPoint.toString());
        };

        sensorDataReceiver.receive(dataPointStringConsumer);
        // */
    }
}
