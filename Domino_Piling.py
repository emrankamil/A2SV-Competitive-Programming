def dominopilling(M,N):
    "M and N are the rows and/or columns of the square board"
    assert 1 <= M <= N <= 16,' the value of M and N shoul conforrm this: 1<=M<=N<=16' 
    total_sqr=M*N
    output=total_sqr//2
    return output
