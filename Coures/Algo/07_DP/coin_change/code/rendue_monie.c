#include <stdio.h>



int phi( int s , int valOpt[] , int choix_opt[] , int P[] , int n)
{
    if ( (s >0) && ( valOpt[s] == 0) ) // phi(s) n’a pas déjà été calcul é
    {
        int min = phi (s -1 , valOpt , choix_opt , P , n) ; // on rend 1 avec la pièce P[1] == 1
        int argmin = 1 ; // indice de la pièce à rendre

        for (int k =2 ; (k <= n ) && (P [ k ] <= s ) ; ++ k )
        {
            int aux = phi ( s - P[ k ] , valOpt , choix_opt , P , n) ;
            if ( aux < min )
            { 
                min = aux ;
                argmin = k ;
            }
        }
        // Stockage de la valeur $\phi (s)$ et d’un choix optimal correspondant
        valOpt [ s ] = min + 1;
        choix_opt [ s ] = argmin ;
    }

   return valOpt [ s ] ;
}


int main(void)
{

    int S = 11 ;
    int valpOpt[11] = {0} ; // valOpt [s] stocke la valeur \phi(s) une fois calcul ée ( init 0)
    int choixpOpt[11] = {0} ; // choixOpt [s] stocke le type de piece d’un rendu optimal de s.

    int P[3] ={1,5,10};
    
    int nb_min = phi(S,valpOpt,choixpOpt,P,3);

    printf("le rendu optimale est de nb : %d \n", nb_min);

    return 0 ;
}