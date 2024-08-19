<h1>Dynamic Programming</h1>
<hr>

<p>Dynamic programming is nothing but it is used to store the 
value of recursion method for the further use </p>

<dl>Dynamic Programming has two approaches

<dl>
1. Top - Down Approach
<dd>
In this approach recursion takes place and also called memoization.
</dd>

<h3> Recursive Method </h3>


    Find the fibonachi series Using Recursion:-----
    _______________________________________

    def fib(n):
        if n==0:
            return 0;
        elif n==1:
            return 1;
        else:
            return=fib(n-1)+fib(n-2);
    
    # Call the method with argument 
    
    print(fib(7);

<h3>Dynamic Programming</h3>

    def fib(n, dp):
        if n==0:
            return 0;
        elif n==1:
            return 1;
        elif dp[n] != -1:
            return dp[n];
        else:
            dp[n] = fib(n-1, dp), fib(n-2, dp);
    
    n=10;
    dp=[-1]*n+1;
    fib(n,dp);
    print(dp);

</dl>

<dl>
2. Bottom - Up Approach
<dd>
In this approach Iteration takes place and also called Tabulation.
</dd>
</dl>

    
 
</dl>