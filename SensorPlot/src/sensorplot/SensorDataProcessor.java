/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sensorplot;

import java.io.BufferedReader;
import java.io.IOException;
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
    char[] dataPointBuffer;
    String twoOrMoreDataPoints;
    FakeDataSource fakeDataSource;
    boolean DEBUG = false;

    public SensorDataProcessor() {
        dataReceiver = SensorDataReceiver.createStandardReceiver();
        dataPointBuffer = new char[SensorDataPointParser.MAX_DATA_POINT_STRING_SIZE];
        twoOrMoreDataPoints = "";

        fakeDataSource = new FakeDataSource();
    }

    public void init() {
        dataReader = new BufferedReader(dataReceiver.connect(), dataPointBuffer.length);
    }

    public DataPoint getNextDataPoint() {
        System.out.println("SensorDataProcessor.getNextDataPoint()");

        String nextDataPointString = "";

        try {
            if (twoOrMoreDataPoints.length() < SensorDataPointParser.MAX_DATA_POINT_STRING_SIZE) {
                Thread.sleep(20); //why does the dataReader not wait?
                dataReader.read(dataPointBuffer, 0, dataPointBuffer.length);

                if (!DEBUG) {
                    twoOrMoreDataPoints = twoOrMoreDataPoints + String.valueOf(dataPointBuffer, 0, dataPointBuffer.length);
                } else {
                    twoOrMoreDataPoints = twoOrMoreDataPoints + fakeDataSource.getNext();
                }
            }

            Matcher wholeCoordinateMatcher = WHOLE_COORDINATE_FORMAT.matcher(twoOrMoreDataPoints);
            boolean hasFound = wholeCoordinateMatcher.find();

            if (!hasFound) {
                System.out.println("has nothing found!");
            }

            nextDataPointString = twoOrMoreDataPoints.substring(wholeCoordinateMatcher.start(), wholeCoordinateMatcher.end());
            twoOrMoreDataPoints = twoOrMoreDataPoints.substring(wholeCoordinateMatcher.end(), twoOrMoreDataPoints.length());

        } catch (IOException e) {
            System.err.println("Reading next Characters of the sensor data failed!");
        } catch (InterruptedException e) {
            System.err.println("Interrupted while waiting!");
        }
        DataPoint dataPoint;

        System.out.println(nextDataPointString);

        dataPoint = SensorDataPointParser.parse(nextDataPointString, OffsetDateTime.now());

        return dataPoint;

    }
}
