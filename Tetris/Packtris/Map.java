package Packtris;

import org.newdawn.slick.*;
import org.newdawn.slick.geom.*;
import java.util.ArrayList;

public class Map {
	ArrayList<ArrayList> maplist;
	public int count = 0;
	public boolean full;
	public int disappear; //probably not necessary
	
	public Map(ArrayList<ArrayList> _maplist) {
		maplist = _maplist;
		for (int i = 0; i < Tetris.screenH/Tetris.block; i++){
			ArrayList<String> list_item = new ArrayList<>(20);
			for (int a = 0; a < 20; a++) {
				list_item.add("0");
			}
			maplist.add(list_item);
		}
	}
	
	public void update(GameContainer gc, int delta) {
		for (int a = 0; a < maplist.size(); a++) { //makes full rows disappear
			for (int i = 0; i < maplist.get(a).size(); i++) {
				if (maplist.get(a).get(i) == "0") {
					full = false;
				}
			}
			if (full == true) {
				for (int i = 0; i < maplist.get(a).size(); i++) {
					maplist.get(a).set(i, "0");
				}
				disappear = a; //pole ilmselt vajalik muutuja
				
				for (int k = 0; k < disappear; k++) { //makes pieces fall after a row disappears
					maplist.set(disappear-k, maplist.get(disappear-k-1));
				}
				
				for (int i = 0; i < maplist.get(0).size(); i++) { //makes first row empty after disappearance of a row
					maplist.get(0).set(i, "0");
				}
				
			}
			full = true;
		}
		
		for (int c = 0; c < maplist.get(0).size(); c++) { //if a piece is written to top row, the game window closes
			if (maplist.get(0).get(c) != "0") {
				System.out.println("GAME OVER");
				System.exit(0);
			}
		}
	}
	
	public void render(GameContainer gc, Graphics g) {
		for (int i = 0; i<maplist.size(); i++) {
			for (int a = 0; a<20; a++) {
				if (maplist.get(i).get(a) == "0") {
					g.setColor(new Color(0, 0, 0));
				} else if (maplist.get(i).get(a) == "1") {
					g.setColor(new Color(255, 0, 0));
				} else if (maplist.get(i).get(a) == "2") {
					g.setColor(new Color(255, 255, 0));
				} else if (maplist.get(i).get(a) == "3") {
					g.setColor(new Color(0, 255, 0));
				} else if (maplist.get(i).get(a) == "4") {
					g.setColor(new Color(0, 0, 255));
				}
				g.fill(new Rectangle(a*Tetris.block, i*Tetris.block, Tetris.block, Tetris.block));
			}
		}
	}
}