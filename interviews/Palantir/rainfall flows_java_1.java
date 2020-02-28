"""
https://github.com/grant/Palantir-Code-Challenge/blob/master/try1/Solution.java

"""


import java.util.Collections;
import java.awt.Point;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class Solution {
    public static int[][] basinIds;
    public static void main(String args[]) throws Exception {
        Scanner input = new Scanner(System.in);

        int landSize = Integer.parseInt(input.nextLine());

        int[][] landArray = new int[landSize][landSize];
        for(int i = 0; i < landSize; i++) {
            String landRow = input.nextLine().trim();
            String[] landElements = landRow.split(" ");
            for(int j = 0; j < landElements.length; j++) {
	            landArray[i][j] = Integer.parseInt(landElements[j]);
            }
        }

        calculateBasins(landArray);
    }

    public static void calculateBasins(int area[][]) {
        int size = area.length;
        Point basins[][] = new Point[size][size];
        HashMap map = new HashMap();
        int basinId = 0;
        for (int x = 0; x < size; x++) {
            for (int y = 0; y < size; y++) {
                basins[x][y] = lowestPlot(area, x, y);
                if(map.containsKey(basins[x][y])) {
                    String landElementString = (String) map.get(basins[x][y]);
                    String[] landElement = landElementString.split(" ");
                    int thisBasinId = Integer.parseInt(landElement[0]);
                    int basinSize = Integer.parseInt(landElement[1]);
                    basinSize++;//increase basin size
                    map.put(basins[x][y], thisBasinId+" "+basinSize);
                } else {
                    map.put(basins[x][y], basinId+" "+1);
                    basinId++;
                }
            }
        }

        ArrayList<Integer> uniqueBasins = new ArrayList<Integer>();
        int currentId = -1;
        for (int x = 0; x < size; x++) {
            for (int y = 0; y < size; y++) {
                String landElementString = (String) map.get(basins[x][y]);
                String[] landElement = landElementString.split(" ");
                int thisBasinId = Integer.parseInt(landElement[0]);
                int basinSize = Integer.parseInt(landElement[1]);
                if (thisBasinId > currentId) {
                    currentId = thisBasinId;
                    uniqueBasins.add(basins);
                }
            }
        }
        Collections.sort(uniqueBasins);

        for (int i : uniqueBasins) {
            System.out.print(i+" ");
        }
    }

    public static Point lowestPlot(int area[][], int x, int y) {
        int size = area.length;
        int leftX, leftY, rightX, rightY, topX, topY, bottomX, bottomY;
        int minX, minY, minValue;

        leftX = x;
        leftY = y - 1;

        rightX = x;
        rightY= y + 1;

        topX = x - 1;
        topY = y;

        bottomX = x + 1;
        bottomY = y;

        minX = x;
        minY = y;
        minValue = area[x][y];

        if (!isOutOfBounds(leftX, leftY, size)) {
            if (area[leftX][leftY] < minValue) {
                minX = leftX;
                minY = leftY;
                minValue = area[leftX][leftY];
            }
        }
        if (!isOutOfBounds(rightX, rightY, size)) {
            if (area[rightX][rightY] < minValue) {
                minX = rightX;
                minY = rightY;
                minValue = area[rightX][rightY];
            }
        }
        if (!isOutOfBounds(topX, topY, size)) {
            if (area[topX][topY] < minValue) {
                minX = topX;
                minY = topY;
                minValue = area[topX][topY];
            }
        }
        if (!isOutOfBounds(bottomX, bottomY, size)) {
            if (area[bottomX][bottomY] < minValue) {
                minX = bottomX;
                minY = bottomY;
                minValue = area[bottomX][bottomY];
            }
        }

        //return self if lowest point else recurse
        return (minX == x && minY == y) ? new Point(x, y) : lowestPlot(area, minX, minY);
    }

    public static boolean isOutOfBounds(int x, int y, int size) {
        return (x < 0 || x >= size || y < 0 || y >= size);
    }
}


#######################

import java.io.File;
import java.awt.Point;

import java.util.*;

public class Solution {
	private static final String yes = "YES";
	private static final String no = "NO";

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		try {
			input = new Scanner(new File("test.txt"));
		} catch (Exception e) {

		}
		boolean good = isGood(input);
		if (good) {
			System.out.println(yes);
		} else {
			System.out.println(no);
		}
	}

	private static boolean isGood(Scanner input) {
        int numStars = Integer.parseInt(input.nextLine());
        List<Point> points = new ArrayList<Point>();

        for (int i = 0; i < numStars; i++) {
        	String[] splitString = input.nextLine().split(" ");
        	points.add(new Point(Integer.parseInt(splitString[0]), Integer.parseInt(splitString[1])));
        }

        // Test if points array works
        // for (int i = 0; i < points.size(); i++) {
        // 	System.out.println(points.get(i));
        // }

        //list of all points added to arraylist

        Map<Double, ArrayList<Point[]>> mp = new HashMap<Double, ArrayList<Point[]>>();

        for (int i = 0; i < points.size() - 1; i++) {//all starter points
        	for (int j = i + 1; j < points.size(); j++) {
        		// System.out.println(i + " " + j);
        		Point p1 = points.get(i);
	        	Point p2 = points.get(j);

	        	if (p2.x != p1.x) {//if valid slope
		        	double slope = (p2.y - p1.y) / (p2.x - p1.x);
		        	slope = (double)Math.round(slope * 100000) / 100000;//round to 5 decimals

		        	if (!mp.containsKey(slope)) {//add new arraylist
		        		mp.put(slope, new ArrayList<Point[]>());
		        	}

		        	Point[] pts = new Point[2];
		        	pts[0] = p1;
		        	pts[1] = p2;

	        		mp.get(slope).add(pts);
	        	}
        	}
        }

        //all starter point indexes are put in an array

        for (ArrayList<Point[]> pointsPairsArray : mp.values()) {
        	//pointStartIndex is the array of indexes of starting points with same slopes
        	Set uniquePoints = new HashSet();
       		if (pointsPairsArray.size() >= 4) {//if a possible line
			    for (int i = 0; i < pointsPairsArray.size(); i++) {
	        		Point[] pts = pointsPairsArray.get(i);
	        		Point pt1 = pts[0];
	        		Point pt2 = pts[1];
	        		// System.out.println(pt1);
	        		// System.out.println(pt2);
	        		uniquePoints.add(pt1);
	        		uniquePoints.add(pt2);
        		}
        	}

        	ArrayList<Point> uniquePointsArray = new ArrayList<Point>();

        	Iterator it = uniquePoints.iterator();
			while(it.hasNext()) {
				uniquePointsArray.add((Point)it.next());
			}

			if (uniquePointsArray.size() >= 4) {
				for (int i = 0; i < uniquePointsArray.size()-3; i++) {
					for (int j = i+1; j < uniquePointsArray.size()-2; j++) {
						for (int k = j+1; k < uniquePointsArray.size()-1; k++) {
							for (int l = k+1; l < uniquePointsArray.size()-0; l++) {
								if (isCollinear(uniquePointsArray.get(i), uniquePointsArray.get(j), uniquePointsArray.get(k), uniquePointsArray.get(l))) {
									return true;
								}
							}
						}
					}
				}
			}
		}
		return false;
	}

	public static boolean isCollinear(Point p1, Point p2, Point p3) {
		return (((p1.y - p2.y) * p3.x + (p2.x - p1.x) * p3.y + (p1.x * p2.y - p2.x * p1.y)) == 0);
	}

	public static boolean isCollinear(Point p1, Point p2, Point p3, Point p4) {
		return isCollinear(p1, p2, p3) && isCollinear(p1, p2, p4) && isCollinear(p1, p3, p4) && isCollinear(p2, p3, p4);
	}
}
