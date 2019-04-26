/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sensorplot;

import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

/**
 *
 * @author MobMonRob
 */
public class SensorDataPointParser {

    static final Pattern COORDINATE_FORMAT = Pattern.compile("-?[0-9]+.{1}[0-9]+");
    public static final int MAX_DATA_POINT_STRING_SIZE = 83;

    private SensorDataPointParser() {

    }

    public static DataPoint parse(String dataPointString, OffsetDateTime now) {
        ArrayList<String> stringCoordinates = new ArrayList();

        Matcher coordinateMatcher = COORDINATE_FORMAT.matcher(dataPointString);

        while (coordinateMatcher.find()) {
            stringCoordinates.add(dataPointString.substring(coordinateMatcher.start(), coordinateMatcher.end()));
        }
        //assert stringCoordinates.size() == 6;
        System.out.println(dataPointString);

        List<Double> dc = stringCoordinates.stream().map(s -> Double.parseDouble(s)).collect(Collectors.toList()); //doubleCoordinates

        return new DataPoint(dc.get(0), dc.get(1), dc.get(2), dc.get(3), dc.get(4), dc.get(5), now);
    }
}
