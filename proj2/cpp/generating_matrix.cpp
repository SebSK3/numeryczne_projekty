void init(int a1, int a2, int a3) {
	for (int i = 0; i < rows - 2; i++) {
		for (int j = 0; j < cols - 2; j++) {
			if (i == j) {
				mat[i][j] = a1;
				mat[i + 1][j] = mat[i][j + 1] = a2;
				mat[i + 2][j] = mat[i][j + 2] = a3;
			}
		}
	}
	mat[rows - 2][cols - 2] = mat[rows - 1][cols - 1] = a1;
	mat[rows - 1][cols - 2] = mat[rows - 2][cols - 1] = a2;
}
