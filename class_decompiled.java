/*
 * Decompiled with CFR 0_118.
 *
 * Could not load the following classes:
 *  org.jasypt.encryption.pbe.StandardPBEStringEncryptor
 */
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintStream;
import java.io.PrintWriter;
import java.io.Reader;
import java.util.LinkedList;
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;

public class Main {
    private static String seed = "Hackathon2016";
    private static int[] CLAVE;
    private static int[] CLAVE_ENTRADA;

    public static void main(String[] args) {
        LinkedList<Integer> posiciones_falladas = new LinkedList<Integer>();
        if (args.length == 2) {
            Main.GetKeyFromFile(args[0]);
            Main.GetEntryKey(args[1]);
            if (CLAVE_ENTRADA.length == CLAVE.length) {
                int i = 0;
                while (i < CLAVE_ENTRADA.length) {
                    if (CLAVE_ENTRADA[i] != CLAVE[i]) {
                        posiciones_falladas.add(i);
                    }
                    ++i;
                }
                if (posiciones_falladas.size() == 0) {
                    System.out.println("Resuelto");
                    try {
                        PrintWriter writer = new PrintWriter("file.out", "UTF-8");
                        writer.println("Caja fuerte desbloqueada!. La clave es: \"" + Main.GetKeyFromArray(CLAVE_ENTRADA) + "\"");
                        writer.close();
                    }
                    catch (Exception e) {
                        System.out.println("Problema al generar el fichero de salida.");
                    }
                } else {
                    double porcentaje = 100.0 - (double)posiciones_falladas.size() / (double)CLAVE.length * 100.0;
                    System.out.println(porcentaje);
                }
            } else {
                System.out.println("La clave introducida no tiene la longitud (9) exacta a la de la clave.");
            }
        } else {
            System.out.println("Al fichero CajaFuerte.jar se le deben pasar dos argumentos: el fichero de entrada file.in, con la clave encriptada, y la combinaci\u00f3n para abrir la caja.\nEj: CajaFuerte.jar file.in 1234567899");
        }
    }

    private static int GetKeyFromArray(int[] key) {
        String c = "";
        int[] arrn = key;
        int n = arrn.length;
        int n2 = 0;
        while (n2 < n) {
            int n3 = arrn[n2];
            c = String.valueOf(c) + n3;
            ++n2;
        }
        return Integer.parseInt(c);
    }

    private static void GetEntryKey(String key) {
        try {
            CLAVE_ENTRADA = new int[key.length()];
            int i = 0;
            while (i < key.length()) {
                Main.CLAVE_ENTRADA[i] = key.charAt(i) - 48;
                ++i;
            }
        }
        catch (Exception ex) {
            System.out.println("La clave introducida es incorrecta.");
        }
    }

    private static void GetKeyFromFile(String file) {
        try {
            BufferedReader br = new BufferedReader(new FileReader(file));
            String encryptedKey = br.readLine();
            String decryptedKey = Main.decrypt(encryptedKey);
            CLAVE = new int[decryptedKey.split(",").length];
            int i = 0;
            while (i < CLAVE.length) {
                int n;
                String s = decryptedKey.split(",")[i].trim();
                Main.CLAVE[i] = n = Integer.parseInt(s);
                ++i;
            }
            br.close();
        }
        catch (IOException ex) {
            System.out.println("Error al cargar el fichero de entrada (\"" + file + "\")");
        }
    }

    private static String decrypt(String encrypted) {
        StandardPBEStringEncryptor encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword(seed);
        String decrypted = encryptor.decrypt(encrypted);
        return decrypted;
    }
}
