package it.security.ciphers.polyalphabetic;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;

public class PolyAlphabetic {
	
	private static final String ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	private static final List<String> ALPHABET_ARRAY;
	private static final int ALPHABET_SIZE;
	static {
		ALPHABET_ARRAY = ALPHABET
                .chars()
                .mapToObj(_char -> String.valueOf((char)_char))
                .collect(Collectors.toList());
		ALPHABET_SIZE = ALPHABET_ARRAY.size();
	}

	private final String cipherPath;
	private final String cipher;

	public PolyAlphabetic(String cipherPath) {
		this.cipherPath = cipherPath;
		
		StringBuilder sb = new StringBuilder();

		InputStream resourceAsStream = getClass().getClassLoader().getResourceAsStream(cipherPath);
		// Path cipherPath = Path.of("resource/cipher/polyalphabetic.txt");
		try (InputStreamReader streamReader = new InputStreamReader(resourceAsStream, StandardCharsets.UTF_8);
				BufferedReader reader = new BufferedReader(streamReader)) {

			String line = null;
			while ((line = reader.readLine()) != null) {
				sb.append(line);
			}

		} catch (IOException e) {
			e.printStackTrace();
		}
		
		this.cipher = sb.toString();
	}
	
	public void decrypt() {
		decrypt(-1);
	}
	
	public void decrypt(int m) {
		List<Integer> key = null;
		
		if ( m > 0 ) {
			key = computeKey(m);
		} else {
			key = computeKey();
		}
		
		List<String> sub = subciphers(key.size());
		
		for ( String k : ALPHABET_ARRAY ) {
			int paddingPos = ALPHABET_ARRAY.indexOf(k);
			
			StringBuilder sb = new StringBuilder();
		
			for ( String s : sub ) {
				List<String> subChars = s.chars()
		            .mapToObj(_char -> String.valueOf((char)_char))
		            .collect(Collectors.toList());
				
				for ( int i = 0; i < subChars.size(); i++ ) {
					String c = subChars.get(i);
					int j = key.get(i);
					
					int pos = ALPHABET_ARRAY.indexOf(c);
					int newPos = (pos + paddingPos + j) % ALPHABET_SIZE;
					String newC = ALPHABET_ARRAY.get(newPos);
					
					sb.append(newC);
				}
			}
			
			System.out.println("Decrypted: " + sb.toString());
		}
		
		
	}
	
	public List<Integer> computeKey() {
		int keyLength = computeKeyLength();
		return computeKey(keyLength);
	}
	
	public List<Integer> computeKey(int keyLength) {
		List<Integer> key = new ArrayList<Integer>();
		//int keyLength = computeKeyLength();
		int m = keyLength;
		
		List<String> sub = subciphers(m);
		
		for ( int i = 0; i < m; i++ ) {
			int k = 0;
			double mick = 0;
			
			for ( int j = 0; j < ALPHABET_SIZE; j++ ) {
				double mic = mic(sub.get(0), shift(j, sub.get(i)));
				if ( mic > mick ) {
					k = j;
					mick = mic;
				}
			}
			
			key.add(k);
		}
		
		System.out.println(key);
		return key;
	}
	
	public String shift(int j, String s) {
		StringBuilder sb = new StringBuilder();
		
		int n = s.length();
		for ( int i = 0; i < n; i++ ) {
			String singleChar = String.valueOf(s.charAt(i));
			int pos = ALPHABET_ARRAY.indexOf(singleChar);
			
			int newPos = (pos + j) % ALPHABET_SIZE;
			String newSingleChar = ALPHABET_ARRAY.get(newPos);
			sb.append(newSingleChar);
		}
		
		return sb.toString();
	}
	
	public double mic(String s1, String s2) {
		double totalF = 0.0;
		for ( String character : ALPHABET_ARRAY ) {
			int currentChar = character.charAt(0);
			long o1 = s1.chars().filter( ch -> ch == currentChar ).count();
			long o2 = s2.chars().filter( ch -> ch == currentChar ).count();
			totalF += (o1 * o2);
		}
		
		double result = totalF / (s1.length() * s2.length());
		return result;
	}
	
	public int computeKeyLength() {
/*
 * 
m = 1
LIMIT=0.06 # this is to check that ICs are above 0.06 and thus close to 0.065
found = False
while(not found):
    sub = subciphers() # takes the m subciphertexts sub[m] obtained by selecting one letter every m
    found = True
    for i in range(0,m): # compute the Ic of all subtexts
        if Ic(sub[i]) < LIMIT:
             # if one of the Ic is not as expected try to increase length
             found = False
             m += 1
             break
# survived the check, all Ic's are above LIMIT
output(m)
 */
		int m = 1;
		double limit = 0.002;
		boolean found = false;
		boolean error = false;
		double lastIC = 0;
		double lastICAvg = 0;
		
		while (!found) {
			if ( m > cipher.length() ) {
				error = true;
				break;
			}
			List<String> sub = subciphers(m);
			//found = true;
			found = false;
			lastICAvg = 0;
			
			for ( int i = 0; i < sub.size(); i++ ) {
				//double ic = ic(sub.get(i));
				double ic = calculate(sub.get(i));
				/*if ( ic < limit ) {
					found = false;
					m += 1;
					break;
				}*/
				
				lastIC = ic;
				lastICAvg += lastIC / sub.size();
			}
			
			m += 1;
			
			System.out.println("m : " + m + ", ic " + lastICAvg);
		}
		
		int keyLenght = m;
		if ( !error  ) {
			System.out.println("Key lenght: " + keyLenght + ", with IC " + lastIC);
			
		} else {
			System.out.println("Error!!");
			keyLenght = 0;
		}
		
		return keyLenght;
	}
	
	private List<String> subciphers(int m) {
		AtomicInteger splitCounter = new AtomicInteger(0);
		
		Collection<String> splittedStrings = cipher
                .chars()
                .mapToObj(_char -> String.valueOf((char)_char))
                .collect(Collectors.groupingBy(stringChar -> splitCounter.getAndIncrement() / m
                                            ,Collectors.joining()))
                .values();
		
		return new ArrayList<String>(splittedStrings);
	}

	private double ic(String s) {
		double totalF = 0.0;
		for ( String character : ALPHABET_ARRAY ) {
			int currentChar = character.charAt(0);
			long occurency = s.chars().filter( ch -> ch == currentChar ).count();
			totalF += (occurency * (occurency - 1));
		}
		
		int n = s.length();
		
		double result = totalF / (n * (n-1));
		return result;
	}
	
	public double calculate(String s){
    	
    	int i;
    	int N = 0;
    	double sum = 0.0;
    	double total = 0.0;
    	s = s.toUpperCase();
    	
    	//initialize array of values to count frequency of each letter
    	int[] values = new int[26];
    	for(i=0; i<26; i++){
    		values[i] = 0;
    	}
    	
    	//calculate frequency of each letter in s
    	int ch;
    	for(i=0; i<s.length(); i++){
    		ch = s.charAt(i)-65;
    		if(ch>=0 && ch<26){
    			values[ch]++;
    			N++;
    			}	
    	}
    	
    	//calculate the sum of each frequency
    	for(i=0; i<26; i++){
    		ch = values[i];
    		sum = sum + (ch * (ch-1));
    		}
    	
    	//divide by N(N-1)	
    	total = sum/(N*(N-1));
    	
    	//return the result
    	return total;
    	
    }
	
	public void output() {
		System.err.println(cipher);
	}

}
