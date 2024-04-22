double LU() {
	Matrix L(N, N);
	Matrix U(N, N);
	for (int i = 0; i < N; i++)
		L[i][i] = 1.0;
	for (int j = 0; j < N; j++) {
	    for (int i = 0; i <= j; i++) {
			U[i][j] += A[i][j];
			for (int k = 0; k <= i - 1; k++)
				U[i][j] -= L[i][k] * U[k][j];
		}
		for (int i = j+1; i < N; i++) {
			for (int k = 0; k <= j - 1; k++)
				L[i][j] -= L[i][k] * U[k][j];
			L[i][j] += A[i][j];
			L[i][j] /= U[j][j];
		}
	}
	Matrix y(N, 1);
	for (int i = 0; i < N; i++) {
		double val = b[i][0];
		for (int j = 0; j < i; j++) {
			if (j != i) val -= L[i][j] * y[j][0];
		}
		y[i][0] = val / L[i][i];
	}
	for (int i = N - 1; i >= 0; i--) {
		double val = y[i][0];
		for (int j = i; j < N; j++) {
			if (j != i) val -= U[i][j] * x[j][0];
		}
		x[i][0] = val / U[i][i];
	}
	return Matrix::norm(A * x - b);
}