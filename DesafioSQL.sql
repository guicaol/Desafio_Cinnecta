SELECT 
    T1.NOME AS SALARIO_MENOR,
     T2.NOME AS SALARIO_MAIOR
FROM 
    FUNCIONARIOS T1
    INNER JOIN FUNCIONARIOS T2
        ON T1.SALARIO< T2.SALARIO
ORDER BY T1.SALARIO, T2.SALARIO