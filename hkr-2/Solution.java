import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        
		Scanner in = new Scanner(System.in);
		String s = in.next();
		int res = 0;
		for (int i = 0; i < s.length(); i++)
						if( (s.codePointAt(i) >= 65) && (s.codePointAt(i) <= 90) )
                            res += 1; 
        res++;
		System.out.println(res);
		in.close();
	
    }
}