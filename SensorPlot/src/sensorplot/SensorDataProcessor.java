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
import java.util.ArrayDeque;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 *
 * @author MobMonRob
 */
public class SensorDataProcessor {

    SensorDataReceiver dataReceiver;
    ArrayDeque<Character> dataQueue;
    BufferedReader dataReader;
    CharBuffer charBuffer;

    public SensorDataProcessor() {
        dataReceiver = SensorDataReceiver.createStandardReceiver();
        dataQueue = new ArrayDeque(SensorDataPointParser.MAX_DATA_POINT_STRING_SIZE * 2);
        charBuffer = CharBuffer.allocate(SensorDataPointParser.MAX_DATA_POINT_STRING_SIZE);
    }

    public void init() {
        dataReader = dataReceiver.connect();
    }

    public DataPoint getNextDataPoint() {
        String nextDataPointString;

        try {
            //To be optimized -> ideally: Circular Buffer Class on Top of a character array with an sufficiant interface
            for (int i = 0; i < SensorDataPointParser.MAX_DATA_POINT_STRING_SIZE; ++i) {
                dataQueue.add((char) dataReader.read());
            }
        } catch (IOException e) {
            System.err.println("Reading next Characters of the sensor data failed!");
        }

        //To be optimized
        String dataQueueString = String.valueOf(dataQueue.toArray());

        Pattern WHOLE_COORDINATE_FORMAT = Pattern.compile("({1}?.+?){1}?"); //Reluctant Regex Quantifier
        Matcher wholeCoordinateMatcher = WHOLE_COORDINATE_FORMAT.matcher(dataQueueString);

        wholeCoordinateMatcher.find();

        nextDataPointString = dataQueueString.substring(wholeCoordinateMatcher.start(), wholeCoordinateMatcher.end());

        //To be optimized
        for (int i = 0; i < wholeCoordinateMatcher.end(); ++i) {
            dataQueue.pollFirst();
        }

        DataPoint dataPoint;
        dataPoint = SensorDataPointParser.parse(nextDataPointString, OffsetDateTime.now());

        return dataPoint;
    }
}
