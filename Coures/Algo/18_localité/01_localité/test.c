#include <stdio.h>



#define n 100

#define K 5

void affichage(int mat[n][n]);


void transp_cache_aware(int mat_A[n][n] , int mat_B[n][n])
{
    // affichage(mat_A);
    for(int I =0 ; I < n ; I+=K)
    {
        for(int J =0 ; J < n ; J+=K)
        {
            // int i_end = I+K ? I+K < n : n ;
            // int j_end = J+K ? J+K < n : n ;

            // printf("%d \n" , i_end);
            // printf("%d \n" , j_end);

            int i_end = I+K ;
            int j_end = J +K ;

            for(int i =I ; i <i_end ; ++i)
            {
                for(int j = J ; j <j_end ; ++j)
                {
                    // printf(" A[%d][%d] = %d \n",i , j , mat_A[i][j]);
                    mat_B[j][i] = mat_A[i][j];
                    // printf(" B[%d][%d] = %d \n",i , j , mat_B[i][j]);

                }
            }
            
        }
    }

    // affichage(mat_B);
}


void tarnsp_naive(int mat_A[n][n] , int mat_B[n][n])
{

   for(int i =0 ; i< n ; i++)
    {
        for(int j=0 ; j <n ; j++)
        {
            mat_B[j][i] = mat_A[i][j];
        }
    }
}

void affichage(int mat[n][n])
{
    for(int i =0 ; i<n ; i++)
    {
        for(int j=0 ; j<n ; j++)
        {
            printf("%d ", mat[i][j]);
        }
        printf("\n");
    }

    printf("\n");

}


void init_mat(int mat[n][n])
{

    for(int i =0 ; i< n ; i++)
    {
        for(int j=0 ; j <n ; j++)
        {
            mat[i][j] = i+j;
        }
    }

}



int main(void)
{
    int mat_A[n][n] ;

    init_mat(mat_A);

    affichage(mat_A);



    int mat_B[n][n] ;



 

    transp_cache_aware(mat_A,mat_B);

    affichage(mat_B);



    return 0 ;



}