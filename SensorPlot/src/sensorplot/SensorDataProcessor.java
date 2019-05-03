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
import java.util.logging.Level;
import java.util.logging.Logger;
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
    FakeDataSource fakeDataSource;
    CharBuffer dataReaderBuffer;
    boolean DEBUG = false;

    public SensorDataProcessor() {
        dataReceiver = SensorDataReceiver.createStandardReceiver();
        dataPointBuffer = CharBuffer.allocate(SensorDataPointParser.MAX_DATA_POINT_STRING_SIZE * 3); //Puffer größer, als was ausgelesen
        dataReaderBuffer = CharBuffer.allocate(SensorDataPointParser.MAX_DATA_POINT_STRING_SIZE);
        twoOrMoreDataPoints = "";

        fakeDataSource = new FakeDataSource();
    }

    public void init() {
        dataReader = new BufferedReader(dataReceiver.connect());
        try {
            Thread.sleep(20);
        } catch (InterruptedException ex) {
            Logger.getLogger(SensorDataProcessor.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public DataPoint getNextDataPoint() {
        System.out.println("SensorDataProcessor.getNextDataPoint()");

        String nextDataPointString = "";

        try {
            dataPointBuffer.clear();
            int readCount = 0;

            if (twoOrMoreDataPoints.length() < SensorDataPointParser.MAX_DATA_POINT_STRING_SIZE) {
                while (readCount < SensorDataPointParser.MAX_DATA_POINT_STRING_SIZE) {
                    while (!dataReader.ready()) {
                        Thread.sleep(10);
                    }

                    int newCharactersReadCount = dataReader.read(dataReaderBuffer.array(), 0, SensorDataPointParser.MAX_DATA_POINT_STRING_SIZE);

                    if (newCharactersReadCount == -1) {
                        continue;
                    }

                    dataPointBuffer.append(dataReaderBuffer, 0, newCharactersReadCount);
                    readCount = readCount + newCharactersReadCount;
                }

                if (!DEBUG) {
                    twoOrMoreDataPoints = twoOrMoreDataPoints + String.valueOf(dataPointBuffer.array(), 0, readCount);
                } else {
                    twoOrMoreDataPoints = twoOrMoreDataPoints + fakeDataSource.getNext();
                }
            }

            int len = twoOrMoreDataPoints.length(); //String vermeiden

            Matcher wholeCoordinateMatcher = WHOLE_COORDINATE_FORMAT.matcher(twoOrMoreDataPoints);
            boolean hasFound = wholeCoordinateMatcher.find();

            if (!hasFound) {
                System.out.println("has nothing found!");
            }

            nextDataPointString = twoOrMoreDataPoints.substring(wholeCoordinateMatcher.start(), wholeCoordinateMatcher.end());
            twoOrMoreDataPoints = twoOrMoreDataPoints.substring(wholeCoordinateMatcher.end(), twoOrMoreDataPoints.length());

            if (nextDataPointString.length() > 80) {
                System.out.println("too big!");
            }

        } catch (IOException e) {
            System.err.println("Reading next Characters of the sensor data failed!");
        } catch (InterruptedException ex) {
            Logger.getLogger(SensorDataProcessor.class.getName()).log(Level.SEVERE, null, ex);
        }
        DataPoint dataPoint;

        System.out.println(nextDataPointString);

        dataPoint = SensorDataPointParser.parse(nextDataPointString, OffsetDateTime.now());

        return dataPoint;

    }
}
