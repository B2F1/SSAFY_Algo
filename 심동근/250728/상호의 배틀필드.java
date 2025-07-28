import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.StringTokenizer;

/**
 * 벽돌(*)은 포탄에 맞으면 평지(.)가 된다.
 *
 */

class Solution {

    public static int y; // 최대범위
    public static int x; // 최대범위
    public static int current_y;
    public static int current_x;
    public static int direction; // 0=북, 1=동, 2=남, 3=서
    public static int d_y[]= {-1, 0, 1, 0};
    public static int d_x[]= {0, 1, 0, -1};

    public static void up(String[][] board) {
        int n_y= current_y+d_y[0];
        int n_x= current_x+d_x[0];
        if(0<=n_y && n_y<y && 0<=n_x && n_x<x && board[n_y][n_x].equals(".")) {
            board[current_y][current_x]= ".";
            board[n_y][n_x]= "^";
            current_y= n_y;
            current_x= n_x;
            direction= 0;
        }else {
            board[current_y][current_x]= "^";
            direction= 0;
        }
    }

    public static void right(String[][] board) {
        int n_y= current_y+d_y[1];
        int n_x= current_x+d_x[1];
        if(0<=n_y && n_y<y && 0<=n_x && n_x<x && board[n_y][n_x].equals(".")) {
            board[current_y][current_x]= ".";
            board[n_y][n_x]= ">";
            current_y= n_y;
            current_x= n_x;
            direction= 1;
        }else {
            board[current_y][current_x]= ">";
            direction= 1;
        }
    }

    public static void down(String[][] board) {
        int n_y= current_y+d_y[2];
        int n_x= current_x+d_x[2];
        if(0<=n_y && n_y<y && 0<=n_x && n_x<x && board[n_y][n_x].equals(".")) {
            board[current_y][current_x]= ".";
            board[n_y][n_x]= "v";
            current_y= n_y;
            current_x= n_x;
            direction= 2;
        }else {
            board[current_y][current_x]= "v";
            direction= 2;
        }
    }

    public static void left(String[][] board) {
        int n_y= current_y+d_y[3];
        int n_x= current_x+d_x[3];
        if(0<=n_y && n_y<y && 0<=n_x && n_x<x && board[n_y][n_x].equals(".")) {
            board[current_y][current_x]= ".";
            board[n_y][n_x]= "<";
            current_y= n_y;
            current_x= n_x;
            direction= 3;
        }else {
            board[current_y][current_x]= "<";
            direction= 3;
        }
    }

    /**
     * direction 방향으로 계속 이동
     * 벽돌(*)을 마주치면 -> 평지(.)로 전환
     * 강철(#)을 마주치면 -> 종료
     * 물(-), 평지(.) -> 계속 이동
     * 범위 밖 -> 종료
     */
    public static void shoot(String[][] board) {
        int n_y= current_y+d_y[direction];
        int n_x= current_x+d_x[direction];
        while(0<=n_y && n_y<y && 0<=n_x && n_x<x) { // 범위 체크
            if(board[n_y][n_x].equals("#")) {
                return;
            }else if(board[n_y][n_x].equals("*")) {
                board[n_y][n_x]= ".";
                return;
            }
            n_y+=d_y[direction];
            n_x+=d_x[direction];
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        int T= Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            /**
             * input
             */

            StringTokenizer st= new StringTokenizer(br.readLine());

            y= Integer.parseInt(st.nextToken());
            x= Integer.parseInt(st.nextToken());

            String[][] board= new String[y][x];

            for(int i=0; i<y; i++) {
                String line= br.readLine();
                for(int j=0; j<x; j++) {
                    board[i][j]= String.valueOf(line.charAt(j));
                }
            }

            int times= Integer.parseInt(br.readLine());
            String orders= br.readLine();


            /**
             * algo
             */
            int flag= 0;

            // 초기값 설정
            for(int i=0; i<y; i++) {
                if(flag==1) {
                    break;
                }
                for(int j=0; j<x; j++) {
                    if(board[i][j].equals("^")) {
                        direction= 0;
                        current_y= i;
                        current_x= j;
                        flag= 1;
                        break;
                    }else if(board[i][j].equals(">")) {
                        direction= 1;
                        current_y= i;
                        current_x= j;
                        flag= 1;
                        break;
                    }else if(board[i][j].equals("v")) {
                        direction= 2;
                        current_y= i;
                        current_x= j;
                        flag= 1;
                        break;
                    }else if(board[i][j].equals("<")) {
                        direction= 3;
                        current_y= i;
                        current_x= j;
                        flag= 1;
                        break;
                    }
                }
            }

            // 명령 수행
            for(int i=0; i<orders.length(); i++) {
                if(orders.charAt(i)=='U') {
                    up(board);
                }else if(orders.charAt(i)=='R') {
                    right(board);
                }else if(orders.charAt(i)=='D') {
                    down(board);
                }else if(orders.charAt(i)=='L') {
                    left(board);
                }else if(orders.charAt(i)=='S') {
                    shoot(board);
                }
            }

            // 결과 출력
            System.out.print("#" + t + " ");
            for(int i=0; i<y; i++) {
                for(int j=0; j<x; j++) {
                    System.out.print(board[i][j]);
                }
                System.out.println();
            }

        }


    }
}