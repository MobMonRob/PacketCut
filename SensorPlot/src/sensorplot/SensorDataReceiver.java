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

/**
 *
 * @author MobMonRob
 */
public class SensorDataReceiver {
    //test: socat - TCP4:192.168.3.2:63351
    public static final String SENSOR_IP_ADRESS = "192.168.3.2";
    public static final int SENSOR_PORT = 63351;
    
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
    
    public void receive() {
        System.out.println("SensorDataReceiver.receive()");
        
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            
            char[] buffer = new char[72];
            
            int debug = 0;
            
            while (true) {
                debug++;
                if (debug > 1) break;
                
                reader.read(buffer, 0, 72);
                String dataPoint = String.valueOf(buffer);
                
                System.out.println(dataPoint);
                System.out.println("--------------------");
               
               Pattern p = Pattern.compile("-?[0-9]+.{1}[0-9]+");
               Matcher m = p.matcher(dataPoint);
               
               Vector<String> v = new Vector<String>();
               
               while (m.find()) {
                   v.add(dataPoint.substring(m.start(), m.end()));
               }
               
               if (v.size() != 6) throw new Exception("Wrong Format!");
               
               v.forEach(s -> System.out.println(s));
               
               System.out.println("__________");
               
               List<Double> d = v.stream().map(s -> Double.parseDouble(s)).collect(Collectors.toList());
               
               d.forEach(dou -> System.out.println(dou));
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
