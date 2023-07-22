LC 688. Knight Probability in Chessboard

// DP Space optimized

class Solution {
    public double knightProbability(int n, int k, int row, int column) {
        double[][] dp1 = new double[n][n]; // current status
        double[][] dp2 = new double[n][n]; // next status

        dp1[row][column] = 1;

        int[][] dir = {{1, 2}, {2, 1}, {-1, 2}, {2, -1}, {1, -2}, {-2, 1},
                        {-1, -2}, {-2, -1}};
        
        int nr = 0, nc = 0;

        for(int i = 0; i < k; i++){
            for(int r = 0; r < n; r++){
                for(int c = 0; c < n; c++){
                    if(dp1[r][c] > 0){
                        for(int[] d: dir){
                            nr = r + d[0];
                            nc = c + d[1];

                            if(nr >= 0 && nc >= 0 && nr < n && nc < n){
                                dp2[nr][nc] += dp1[r][c] / 8;
                            }
                        }
                    }
                }
            }
            dp1 = dp2;
            dp2 = new double[n][n];
        }

        double net = 0.0;

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                net += dp1[i][j];
            }
        }
        
        return net;
    }
}

// Time complexity: O(k⋅n2)
// Space complexity: O(n2)