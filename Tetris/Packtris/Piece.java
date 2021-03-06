package Packtris;

import org.newdawn.slick.*;
import org.newdawn.slick.geom.*;
import java.util.List;

public class Piece{
	private int id;
	private float x;
	private float y;
	private int height = 0;
	private int width = 0;
	private int heading = 90;

	private List<Rectangle> object;
	private List<List<Integer>> maplist;

	private int cooldown = 300;
	private float on_screen_x = 0; // Detect if piece moves out of screen horizontally during rotation
	private float on_screen_y = 0; // Detect if piece moves out of screen vertically during rotation
	private boolean collides;
	private boolean left; // boolean to detect if piece can move left
	private boolean right; // boolean to detect if piece can move right
	
	public Rectangle rect;
	
	public Piece(float _x, float _y, int _id, List<Rectangle> _object, List<List<Integer>> _maplist) {
		this.x = _x;
		this.y = _y;
		this.id = _id;
		this.object = _object;
		this.maplist = _maplist;
	}
	
	public boolean collide() { //function to detect collision with other pieces and the ground
		for (Rectangle r : object) {
			if ((int) r.getMaxY() / Tetris.block < 30) { //checks if the rectangle is still on screen
				if (maplist.get((int)r.getMaxY() / Tetris.block).get((int)r.getX() / Tetris.block) != 0) { //checks if the future position is vacant
					collides = true;
				}
			}
			
			if ((int)r.getMaxY() / Tetris.block >= 30) { //checks collision with the floor
				collides = true;
			}
		}

		return collides;
	}
	
	public void update(GameContainer gc, int delta) {
		Input ip = gc.getInput();

		if (cooldown <= 0 && !Tetris.stop && !collide()) { //falling downwards if collision not detected
			y += 1;
			cooldown = 300;
		}
		
		for (Rectangle r : object) { //checks if the piece is still on screen
			if (r.getX() > 0 && maplist.get((int)r.getY()/Tetris.block).get((int)r.getX()/Tetris.block-1) == 0) { //minimum r.getX() is zero
				left = true;
			} else { //if a rectangle in piece is found out of screen, break and return false
				left = false;
				break;
			}
			
			if (r.getMaxX() < Tetris.screenW && maplist.get((int)r.getY()/Tetris.block).get((int)r.getX()/Tetris.block+1) == 0) { //maximum r.getMaxX() is equal to screen width
				right = true;
			} else { //if a rectangle in piece is found out of screen, break and return false
				right = false;
				break;
			}
		}
		
		if (ip.isKeyPressed(Input.KEY_LEFT) && left) { //moving horizontally if piece remains on screen
			x -= 1;
		} else if (ip.isKeyPressed(Input.KEY_RIGHT) && right) {
			x += 1;
		}
		
		if (ip.isKeyDown(Input.KEY_DOWN)) { //adding extra speed when holding down key
			cooldown -= 5;
		}
		
		if (ip.isKeyPressed(Input.KEY_Z)) { //changing heading when pressing z key
			heading += 90;
			if (heading == 450) {
				heading = 90;
			}
		}
		
		if (collide()) { //stopping at the bottom/on other pieces and writing pieces to the map
			Tetris.stop = true;
			for (Rectangle r : object) {
				if ((int)r.getY()/Tetris.block < 30) {
					if (id == 0) {
						maplist.get((int)r.getY()/Tetris.block).set((int)r.getX()/Tetris.block, 1);
					} else if (id == 1) {
						maplist.get((int)r.getY()/Tetris.block).set((int)r.getX()/Tetris.block, 2);
					} else if (id == 2) {
						maplist.get((int)r.getY()/Tetris.block).set((int)r.getX()/Tetris.block, 3);
					} else if (id == 3) {
						maplist.get((int)r.getY()/Tetris.block).set((int)r.getX()/Tetris.block, 4);
					}
				}
			}
		}
		
		cooldown -= 2;
		object.clear();
	}
	
	public void render(GameContainer gc, Graphics g) { //drawing objects onto screen according to id, sin and cos of heading are used to locate rectangles according to x and y coordinates
		if (id == 0) {
			for (int i=0; i<4; i++) {
				rect = new Rectangle((x+i*(float)Math.cos(Math.toRadians(heading)))*Tetris.block, (y+i*(float)Math.sin(Math.toRadians(heading)))*Tetris.block, Tetris.block, Tetris.block);
				object.add(rect);
			}
			height = 4;
			width = 1;
		}
		
		else if (id == 1) {
			for (int i=0; i<3; i++) {
				rect = new Rectangle((x+i*(float)Math.cos(Math.toRadians(heading)))*Tetris.block, (y+i*(float)Math.sin(Math.toRadians(heading)))*Tetris.block, Tetris.block, Tetris.block);
				object.add(rect);
			}
			rect = new Rectangle((x+(float)Math.sin(Math.toRadians(heading)))*Tetris.block, (y+(-1)*(float)Math.cos(Math.toRadians(heading)))*Tetris.block, Tetris.block, Tetris.block);
			object.add(rect);
			height = 3;
			width = 2;
		}
		
		else if (id == 2) {
			for (int i=0; i<3; i++) {
				rect = new Rectangle((x+i*(float)Math.cos(Math.toRadians(heading)))*Tetris.block, (y+i*(float)Math.sin(Math.toRadians(heading)))*Tetris.block, Tetris.block, Tetris.block);
				object.add(rect);
			}
			rect = new Rectangle((x+(-1)*(float)Math.sin(Math.toRadians(heading)))*Tetris.block, (y+(float)Math.cos(Math.toRadians(heading)))*Tetris.block, Tetris.block, Tetris.block);
			object.add(rect);
			height = 3;
			width = 2;
		}
		
		else if (id == 3) {
			for (int i=0; i<3; i++) {
				rect = new Rectangle((x+i*(float)Math.cos(Math.toRadians(heading)))*Tetris.block, (y+i*(float)Math.sin(Math.toRadians(heading)))*Tetris.block, Tetris.block, Tetris.block);
				object.add(rect);
			}
			rect = new Rectangle((x+(float)Math.sin(Math.toRadians(heading))+(float)Math.cos(Math.toRadians(heading)))*Tetris.block, (y+(float)Math.sin(Math.toRadians(heading))+(-1)*(float)Math.cos(Math.toRadians(heading)))*Tetris.block, Tetris.block, Tetris.block);
			object.add(rect);
			height = 3;
			width = 2;
		}
		
		for (Rectangle r : object) { //if piece moves out of screen during rotation, register its location
			if (r.getX() < 0) { //If piece moved out of the screen's left side
				if (-((int)r.getX()) > on_screen_x) {
					on_screen_x = -((int)r.getX());
				}
			}
			
			if (r.getMaxX() > Tetris.screenW) { //If piece moved out of the screen's right side
				if (-((int)r.getMaxX()-Tetris.screenW) < on_screen_x) {
					on_screen_x = -((int)r.getMaxX()-Tetris.screenW);
				}
			}
			
			if (r.getY() < 0) { //If piece moved out of screen's upper side
				if (-((int)r.getY()) > on_screen_y) {
					on_screen_y = -((int)r.getY());
				}
			}
		}
		
		for (Rectangle r : object) {
			//if piece moves out of screen during rotation, move it back
			r.setX((int)r.getX()+on_screen_x); 
			r.setY((int)r.getY()+on_screen_y);
			x = object.get(0).getX()/Tetris.block; //set x coordinate right if piece moves out of screen during rotation
			y = object.get(0).getY()/Tetris.block; //set y coordinate right if piece moves out of screen during rotation
			
			if (id == 0) {
				g.setColor(new Color(255, 0, 0));
			} else if (id == 1) {
				g.setColor(new Color(255, 255, 0));
			} else if (id == 2) {
				g.setColor(new Color(0, 255, 0));
			} else if (id == 3) {
				g.setColor(new Color(0, 0, 255));
			}
			g.fill(r);
		}
		on_screen_x = 0;
		on_screen_y = 0;
	}
}