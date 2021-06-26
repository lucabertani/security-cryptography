package it.security.ciphers.polyalphabetic;

public class Main {

	public static void main(String[] args) {
		
		PolyAlphabetic p = new PolyAlphabetic("resource/cipher/polyalphabetic.txt");
		p.output();
		//p.computeKeyLength();
		//p.computeKey();
		//p.decrypt();
		
		p.computeKeyLength();
		
		//p.computeKey(14);
		//p.decrypt(14);
		
	}
	
	

}
