/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sensorplot;

import java.io.BufferedReader;
import java.io.IOException;
import java.nio.CharBuffer;
import java.time.OffsetDateTime;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 *
 * @author MobMonRob
 */
public class SensorDataProcessor {

    static final Pattern WHOLE_COORDINATE_FORMAT = Pattern.compile("\\(.+?\\)");
    SensorDataReceiver dataReceiver;
    BufferedReader dataReader;
    CharBuffer dataPointBuffer;
    String twoOrMoreDataPoints;
    int DBG_COUNT = 0;

    public SensorDataProcessor() {
        dataReceiver = SensorDataReceiver.createStandardReceiver();
        dataPointBuffer = CharBuffer.allocate(SensorDataPointParser.MAX_DATA_POINT_STRING_SIZE);
        twoOrMoreDataPoints = "";
    }

    public void init() {
        dataReader = dataReceiver.connect();
    }

    public DataPoint getNextDataPoint() {
        System.out.println("SensorDataProcessor.getNextDataPoint()");
        
        DBG_COUNT++;

        String nextDataPointString = "";

        try {
            if (twoOrMoreDataPoints.length() <= SensorDataPointParser.MAX_DATA_POINT_STRING_SIZE) {
                dataPointBuffer.clear();
                dataReader.read(dataPointBuffer.array(), 0, dataPointBuffer.limit());

                twoOrMoreDataPoints = twoOrMoreDataPoints.concat(dataPointBuffer.toString());
            }

            Matcher wholeCoordinateMatcher = WHOLE_COORDINATE_FORMAT.matcher(twoOrMoreDataPoints);
            wholeCoordinateMatcher.find();

            nextDataPointString = twoOrMoreDataPoints.substring(wholeCoordinateMatcher.start(), wholeCoordinateMatcher.end());
            twoOrMoreDataPoints = twoOrMoreDataPoints.substring(wholeCoordinateMatcher.end(), twoOrMoreDataPoints.length());

        } catch (IOException e) {
            System.err.println("Reading next Characters of the sensor data failed!");
        }

        DataPoint dataPoint;
        dataPoint = SensorDataPointParser.parse(nextDataPointString, OffsetDateTime.now());
        
        if (dataPoint == null) {
            System.out.println("blub");
        }

        return dataPoint;

    }
}
