/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sensorplot;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

/**
 *
 * @author MobMonRob
 */
public class DataPointCoordinatesList {

    public final List<Double> fx;
    public final List<Double> fy;
    public final List<Double> fz;
    public final List<Double> mx;
    public final List<Double> my;
    public final List<Double> mz;
    public final List<Integer> timestamp;

    public DataPointCoordinatesList() {
        fx = new ArrayList();
        fy = new ArrayList();
        fz = new ArrayList();
        mx = new ArrayList();
        my = new ArrayList();
        mz = new ArrayList();
        timestamp = new ArrayList();
    }

    public void addDataPoints(List<DataPoint> dataPoints) {
        fx.addAll(dataPoints.stream().map(dataPoint -> dataPoint.fx).collect(Collectors.toList()));
        fy.addAll(dataPoints.stream().map(dataPoint -> dataPoint.fy).collect(Collectors.toList()));
        fz.addAll(dataPoints.stream().map(dataPoint -> dataPoint.fz).collect(Collectors.toList()));
        mx.addAll(dataPoints.stream().map(dataPoint -> dataPoint.mx).collect(Collectors.toList()));
        my.addAll(dataPoints.stream().map(dataPoint -> dataPoint.my).collect(Collectors.toList()));
        mz.addAll(dataPoints.stream().map(dataPoint -> dataPoint.mz).collect(Collectors.toList()));

        for (int i = 0; i < dataPoints.size(); ++i) {
            timestamp.add(timestamp.size());
        }
    }

    public void addDataPoint(DataPoint dataPoint) {
        fx.add(dataPoint.fx);
        fy.add(dataPoint.fy);
        fz.add(dataPoint.fz);
        mx.add(dataPoint.mx);
        my.add(dataPoint.my);
        mz.add(dataPoint.mz);

        timestamp.add(timestamp.size());
    }
}
