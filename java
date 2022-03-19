package okancilesiz;

import java.util.Scanner;

public class oknClsz {

	public oknClsz() {
		// TODO Auto-generated constructor stub
		// if (boolean ifade = koşul yazılmalı )
		// a == b = a b ye eşit mi ?
		// a != b = a bye eşit değil mi ?
		// a < b = a b den küçük mü
		// a > b = a b den büyük mü
		// a <= b a b den küçük ve ya eşit mi
		// a >= b a b den büyük ve ya eşit mi
		// (b1 && b2==1) ikiside doğru olmak zorunda
		// (b1 || b2==1) ikisinden biri doğruysa 
	}

	public static void main(String[] args) {
		/*int a = 10;
		if (a == 35) {
			 System.out.println("Eşittir");
		}
		else {
			System.out.println("Eşit değildir.");
		}*/
		/*
		Scanner gs = new Scanner(System.in);
		int a = gs.nextInt();
		if (a > 0 ) {
			System.out.println("Sayı Pozitif");
					
		}
		else if (a < 0) {
			System.out.println("Sayı Negatif");
			
		}
		else {
			System.out.println("Sayı 0'dır");
		}
		*/
		/*
		Scanner gs = new Scanner(System.in);
		String hamburger , Lahmacun , pizza;
		System.out.println("Merhaba Hoşgeldiniz vermek istediğiniz siparişi yazar mısınız ?\n"
				+ "1 Hamburger "
				+ "2 Pizza "
				+ "3 Lahmacun");
		int a = gs.nextInt();
		if (a == 1) {
			System.out.println("Hamurger Siparişiniz Hazırlanıyor. Ücreti : 40 TL'dir.");
		}
		else if (a == 2) {
			System.out.println("Pizza siparişiniz Hazırlanıyor. Ücreti : 35 TL'dir");
			
		}
		else if (a == 3) {
			System.out.println("Lahmacun Siparişiniz Hazırlanıyor. Ücreti : 15 TL'dir");
			
		}
		*/
		/*
		Scanner gs = new Scanner(System.in);
		String yemek = gs.next();
		if(yemek.equalsIgnoreCase("lahmacun"))
			System.out.println("Lahmacun siparişiniz Hazırlanıyor. Hesabınız 15 Lira");
		else if (yemek.equalsIgnoreCase("hamburger"))
			System.out.println("Hamburger Siparişiniz Hazırlanıyor. Hesabınız 40 Lira");
		else if (yemek.equalsIgnoreCase("pizza"))
			System.out.println("Pizza siparişiniz hazırlanıyor. Hesabınız 35 Lira");
		*/
		/*
		Scanner gs = new Scanner(System.in);
		System.out.println("Lütfen Sipariş giriniz !");
		String yemek = gs.nextLine();
		yemek = yemek.toLowerCase();
		int hesap = 0;
		String temp ="";
		if(yemek.indexOf("lahmacun ") != -1) {
			hesap += 15;
			temp += "lahmacun";
		}
		if(yemek.indexOf("hamburger ") != -1) {
			hesap += 40;
			temp += " hamburger";
		}
		if(yemek.indexOf("pizza ") != -1) {
			hesap += 35;
			temp += " pizza";
		}
		System.out.println("Siparişiniz :" + temp  + "Hesabınız : " + hesap);
		*/
		/*
		Scanner gs = new Scanner(System.in);
		System.out.print("Lütfen Yaşınızı ve okulunuzu giriniz.");
		String okul = gs.next();
		int yas = gs.nextInt();
		if(yas >= 18 && okul.equalsIgnoreCase("universite"))
				System.out.println("Ehliyet Alabilirsiniz");
		else if (yas >= 18 && !okul.equalsIgnoreCase("universite"))
			System.out.println("Yaşınız yeterli ama hala universitede değilsiniz");
		else 
			System.out.println("Ehliyet Alamazsınız");
		*/
		/*
		Scanner gs = new Scanner(System.in);
		String c1 = gs.next(); // + - * /
		int a = 5;
		int b = 10;
		switch (c1)
		{
		case "+":
			System.out.println(a+b);
		case "-":
			System.out.println(a-b);
		case "*":
			System.out.println(a*b);
		case "/":
			System.out.println(a/b);
		break;
		default:
			System.out.println("Böyle bir işlem tanımlı değil");
		}
		*/
		/*
		Scanner gs = new Scanner(System.in);
		System.out.print("Lütfen Yaşınızı Giriniz");
		int yas = gs.nextInt();
		if (yas <= 18) {
			System.out.println("Öğrenci Bileti");	
		}
		else if (yas >= 18 && yas <65)
			System.out.println("Tam bilet");
		else if (yas >= 65)
			System.out.println("65 üstü bilet");
		
		else 
			System.out.println("Yaş negatif olamaz");
		*/
		/*
		Scanner gs = new Scanner(System.in);
		int a = 5;
		if(++a > 5)
			System.out.println("Girdi");
		else
			System.out.println("Girmedi");
		*/
		/*
		Scanner gs = new Scanner(System.in);
		int a = 5;
		int b = 10;
		if(a > 10 &&  ++b > 9) // tek & yanlış olsa dahi diğerine bak
			System.out.println("Girdi");
		else
			System.out.println("Girmedi");
			
		System.out.println(b);
		*/
		
		}
	}


