/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sensorplot;

import java.time.OffsetDateTime;

/**
 *
 * @author MobMonRob
 */
public class DataPoint {
    public final double fx;
    public final double fy;
    public final double fz;
    public final double mx;
    public final double my;
    public final double mz;
    public final OffsetDateTime timestamp;
    
    public DataPoint(double fx, double fy, double fz, double mx, double my, double mz, OffsetDateTime timestamp) {
        this.fx = fx;
        this.fy = fy;
        this.fz = fz;
        this.mx = mx;
        this.my = my;
        this.mz = mz;
        this.timestamp = timestamp;
    }
    
    @Override
    public String toString() {
        return "(" + String.format("%.06f, %.06f, %.06f, %.06f, %.06f, %.06f", fx, fy, fz, mx, my, mz) + ", " + timestamp.toString() + ")";
    }
} 
