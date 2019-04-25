/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sensorplot;

import java.util.ArrayList;
import java.util.List;
import org.knowm.xchart.*;

/**
 *
 * @author MobMonRob
 */
public class Plot {

    XYChart chart;
    SwingWrapper wrappedChart;

    public Plot() {
        chart = new XYChartBuilder().width(800).height(600).title("SensorPlot").xAxisTitle("Time").yAxisTitle("Coordinates").build();
        List dummy = new ArrayList<Double>();
        dummy.add(0.0);

        chart.addSeries​("fx", dummy);
        chart.addSeries​("fy", dummy);
        chart.addSeries​("fz", dummy);
        chart.addSeries​("mx", dummy);
        chart.addSeries​("my", dummy);
        chart.addSeries​("mz", dummy);

        wrappedChart = new SwingWrapper(chart);
    }

    public void updateDatePointCoordinatesList(DataPointCoordinatesList dataPointCoordinatesList) {
        chart.updateXYSeries("fx", dataPointCoordinatesList.timestamp, dataPointCoordinatesList.fx, null);
        chart.updateXYSeries("fy", dataPointCoordinatesList.timestamp, dataPointCoordinatesList.fy, null);
        chart.updateXYSeries("fz", dataPointCoordinatesList.timestamp, dataPointCoordinatesList.fz, null);
        chart.updateXYSeries("mx", dataPointCoordinatesList.timestamp, dataPointCoordinatesList.mx, null);
        chart.updateXYSeries("my", dataPointCoordinatesList.timestamp, dataPointCoordinatesList.my, null);
        chart.updateXYSeries("mz", dataPointCoordinatesList.timestamp, dataPointCoordinatesList.mz, null);
    }

    public void display() {
        wrappedChart.displayChart();
    }

    public void repaint() {
        wrappedChart.repaintChart();
    }
}
