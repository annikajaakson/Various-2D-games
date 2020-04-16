package Packtris;

import org.newdawn.slick.*;
import org.newdawn.slick.geom.*;
import java.util.ArrayList;
import java.util.List;

public class Map {
	private List<List<Integer>> maplist; // Dynamic size list to hold map structure
	private boolean full;
	
	// Initialize map
	public Map(List<List<Integer>> _maplist) {
		maplist = _maplist;
		for (int i = 0; i < Tetris.screenH / Tetris.block; i++){
			ArrayList<Integer> list_item = new ArrayList<>(Tetris.screenW / Tetris.block);
			for (int a = 0; a < 20; a++) {
				list_item.add(0);
			}
			maplist.add(list_item);
		}
	}
	
	public void update(GameContainer gc, int delta) {
		for (int row = 0; row < maplist.size(); row++) { //makes full rows disappear
			for (int column = 0; column < maplist.get(row).size(); column++) {
				if (maplist.get(row).get(column) == 0) {
					full = false;
					break;
				}
			}
			
			// Clear a full row
			if (full) {
				for (int column = 0; column < maplist.get(row).size(); column++) {
					maplist.get(row).set(column, 0);
				}
				
				for (int k = 0; k < row; k++) { //makes pieces fall after a row disappears
					maplist.set(row-k, maplist.get(row-k-1));
				}
				
				for (int col = 0; col < maplist.get(0).size(); col++) { //makes first row empty after disappearance of a row
					maplist.get(0).set(col, 0);
				}
				
			}
			full = true;
		}
		
		for (int col = 0; col < maplist.get(0).size(); col++) { //if a piece is written to top row, the game window closes
			if (maplist.get(0).get(col) != 0) {
				System.out.println("GAME OVER");
				System.exit(0);
			}
		}
	}
	
	public void render(GameContainer gc, Graphics g) {
		// Draw map to screen, rectangle by rectangle
		for (int i = 0; i<maplist.size(); i++) {
			for (int a = 0; a<20; a++) {
				if (maplist.get(i).get(a) == 0) {
					g.setColor(new Color(0, 0, 0));
				} else if (maplist.get(i).get(a) == 1) {
					g.setColor(new Color(255, 0, 0));
				} else if (maplist.get(i).get(a) == 2) {
					g.setColor(new Color(255, 255, 0));
				} else if (maplist.get(i).get(a) == 3) {
					g.setColor(new Color(0, 255, 0));
				} else if (maplist.get(i).get(a) == 4) {
					g.setColor(new Color(0, 0, 255));
				}
				g.fill(new Rectangle(a*Tetris.block, i*Tetris.block, Tetris.block, Tetris.block));
			}
		}
	}
}