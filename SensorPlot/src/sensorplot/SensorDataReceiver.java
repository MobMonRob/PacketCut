/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sensorplot;

import java.io.*;
import java.net.*;

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

    public InputStreamReader connect() {
        System.out.println("SensorDataReceiver.connect()");
        InputStreamReader socketReader = null;

        try {
            socket = new Socket(InetAddress.getByName(ipAdress), port);
            System.out.println("Connection succeeded!");
            socketReader = new InputStreamReader(socket.getInputStream());
        } catch (IOException e) {
            System.err.println("Connection failed!");
            System.err.println(e.toString());
        }

        return socketReader;
    }

    public void deconnect() {
        System.out.println("SensorDataReceiver.deconnect()");
        try {
            socket.close();
        } catch (IOException e) {
            System.err.println("deconnecting failed!");
        }
    }
}
