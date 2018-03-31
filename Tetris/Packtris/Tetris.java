/*
To do:
Maybe a menu
A point counter
Remove unnecessary variables
*/

package Packtris;

import org.newdawn.slick.*;
import org.newdawn.slick.geom.*;
import java.util.ArrayList;
import java.util.Random;
import Packtris.Piece.*;

public class Tetris extends BasicGame {
	public static int block = 20;
	public static int screenW = 400;
	public static int screenH = 600;
	public static ArrayList<Rectangle> activelego = new ArrayList<Rectangle>();
	public static ArrayList<ArrayList> activemap = new ArrayList<ArrayList>();
	
	public static boolean stop = false;
	
	Piece activepiece;
	Map structmap;
	
	public Tetris(String name) {
		super(name);
	}
	
	public void init(GameContainer gc) throws SlickException {
		// Initialize map and active piece
		activepiece = new Piece(9, 0, (int)(Math.random()*4), activelego, activemap);
		structmap = new Map(activemap);
	}
	
	public void update(GameContainer gc, int delta) throws SlickException {
		activepiece.update(gc, delta);
		if (stop == true) {
			//Create a new piece if previous one stopped moving
			activepiece = new Piece(9, 0, (int)(Math.random()*4), activelego, activemap);
			stop = false;
		}
		structmap.update(gc, delta);
	}
	
	public void render(GameContainer gc, Graphics g) throws SlickException {
		structmap.render(gc, g);
		activepiece.render(gc, g);
	}
	
	public static void main(String[] args) {
		try {
			AppGameContainer appgc;
			appgc = new AppGameContainer(new Tetris("Tetris clone"));
			appgc.setDisplayMode(screenW, screenH, false);
			appgc.start();
		} catch (SlickException e) {
			
		}
	}
}