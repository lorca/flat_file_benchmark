package progs;

import java.util.Vector;
import java.nio.charset.Charset;
import java.io.BufferedReader;
import java.nio.file.Files;
import java.io.File;
import java.nio.file.FileSystems;
import java.nio.file.Path;

public class ReadFile {
    static String join(String[] array, String sep) {
       StringBuilder s = new StringBuilder();
       int len_minus_one = array.length - 1;
       for (int i = 0; i < len_minus_one; ++i) {
          s.append(array[i]);
          s.append(sep);
       }
       s.append(array[len_minus_one]);
       return s.toString();
    }

    public static void main(String args[]) throws Exception {
        Vector<String[]> rows = new Vector<String[]>();
        Charset charset = Charset.forName("US-ASCII");
        Path path = FileSystems.getDefault().getPath(args[0]);
        BufferedReader reader = Files.newBufferedReader(path, charset);
        String line = null;
        while ((line = reader.readLine()) != null) {
            rows.add(line.split("\t"));
        }

        System.out.println(join(rows.get(1),","));
    }
}
