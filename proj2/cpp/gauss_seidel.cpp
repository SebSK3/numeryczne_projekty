double Gauss_Seidl() {
	for (int t = 1; ; t++) {
		for (int i = 0; i < N; i++) {
			double val = b[i][0];
			for (int k = 0; k < N; k++) {
				if (k != i)
					val -= A[i][k] * x[k][0];
			}
			val /= A[i][i];
			x[i][0] = val;
		}
		auto norm = Matrix::norm(A * x - b);
		if (norm <= e || t >= 1000)
			return t;
	}
}
