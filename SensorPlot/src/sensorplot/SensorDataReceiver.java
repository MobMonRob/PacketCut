/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sensorplot;

import java.io.* ;
import java.net.*;
import java.util.regex.*;
import java.util.*;
import java.util.stream.Collectors;
import java.time.OffsetDateTime;
import java.util.function.*;

/**
 *
 * @author MobMonRob
 */
public class SensorDataReceiver {
    //test: socat - TCP4:192.168.3.2:63351
    public static final String SENSOR_IP_ADRESS = "192.168.3.2";
    public static final int SENSOR_PORT = 63351;
    static final int MESSAGE_SIZE = 71;
    
    final String ipAdress;
    final int port;
    Socket socket;  
   
    private SensorDataReceiver() {
        this.ipAdress = SENSOR_IP_ADRESS;
        this.port = SENSOR_PORT;
        this.socket = new Socket();
    }
    
    public SensorDataReceiver(String ipAdress, int port) {
        this.ipAdress = ipAdress;
        this.port = port;
        this.socket = new Socket();
    }
    
    public static SensorDataReceiver createStandardReceiver() {
        return new SensorDataReceiver();
    }
    
    public void connect() {
        System.out.println("SensorDataReceiver.connect()");
        
        try {
            socket = new Socket(InetAddress.getByName(ipAdress), port);
            System.out.println("Connection succeeded!");
        }
        catch(IOException e) {
            System.err.println("Connection failed!");
            System.err.println(e.toString());
        }
    }
    
    public void receive(Consumer<DataPoint> dataPointConsumer) {
        System.out.println("SensorDataReceiver.receive()");
        
        try {
            BufferedReader socketReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            char[] buffer = new char[MESSAGE_SIZE];
            Pattern coordinateFormat = Pattern.compile("-?[0-9]+.{1}[0-9]+");
            String dataPointString;
            Matcher coordinateMatcher;
            ArrayList<String> stringCoordinates = new ArrayList();
            OffsetDateTime now;
            List<Double> dc; //doubleCoordinates
            DataPoint dataPoint;
            
            while (true) {
                stringCoordinates.clear();
                
                socketReader.read(buffer, 0, MESSAGE_SIZE);
                now = OffsetDateTime.now();
                dataPointString = String.valueOf(buffer);
                coordinateMatcher = coordinateFormat.matcher(dataPointString);
               
                while (coordinateMatcher.find()) {
                    stringCoordinates.add(dataPointString.substring(coordinateMatcher.start(), coordinateMatcher.end()));
                }
                assert stringCoordinates.size() == 6;
               
                dc = stringCoordinates.stream().map(s -> Double.parseDouble(s)).collect(Collectors.toList());

                dataPoint = new DataPoint(dc.get(0), dc.get(1), dc.get(2), dc.get(3), dc.get(4), dc.get(5), now);
                dataPointConsumer.accept(dataPoint);
            }
        }
        catch(IOException e) {
            System.err.println("Receiving failed!");
        }
        catch(Exception e) {
            System.err.println(e.toString());
        }
    }
}
