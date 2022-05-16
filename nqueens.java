import java.util.Scanner;

public class nqueens {

	public int ans = 0;
	private int n;
	private int board[][];
	private static Scanner sc = new Scanner(System.in);
	
	public nqueens(int n) {
		this.n = n;
		this.board = new int[n][n];
	}
	public void printBoard() {
		System.out.println("\n");
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				System.out.print(this.board[i][j] + " ");
			}
			System.out.println();
		}
	}
	
	
	public boolean check(int i,int j) {
		
		int k,jj;
		k= i-1;
		while(k>=0) {
			if(this.board[k][j] == 1) {return false;}
			k--;
		}
		
		k = i-1;
		jj = j-1;
		while(k>=0 && jj>=0) {
			if(this.board[k][jj] == 1) {return false;}
			k--;
			jj--;
		}
		
		k = i-1;
		jj = j+1;
		while(k>=0 && jj<n) {
			if(this.board[k][jj] == 1) {return false;}
			k--;
			jj++;
		}
		return true;
	}
	public void solve(int i) {
		if(i==n) {
			ans++;
			this.printBoard();
			return;
		}
		
		for(int j=0;j<this.n;j++) {
			
			if(this.check(i, j)) {
				this.board[i][j] = 1;
				this.solve(i+1);
				this.board[i][j] = 0;
			}
		}
	}
	
	public static void main(String argc[]) {
		System.out.print("Enter n: ");
		int n = sc.nextInt();
		
		int[][] board = new int[n][n];
		
		nqueens solution = new nqueens(n);
		
		solution.printBoard();
		
		solution.solve(0);
		System.out.println("\nTotal outcomes: " + solution.ans);
		
//		solution.printBoard();;
		sc.close();
	}

}
