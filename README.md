# cookies-redes
Desenvolvendo um cookie em Python para a matéria de Redes de Computadores I.

Esse cookie contem as seguintes características 

1.  **Nome e valor**    
    - O nome (chave) identifica o cookie.
    - O valor que à armazenar: nome, ID de sessão e idioma.


2. **Validade / Expiração (expires ou max-age)**
    - Controla a duração do cookie.
    - Essencial para diferenciar: 
        - duram até fechar o navegador (se não definir expires).
        - duram um tempo definido (ex: 7 dias, 30 dias).

        
3. **Tentar identificar o tema do navegador**; 
    - Data ou hora da ultima visita;    
    - Timestamp da visita (ex: visitado em)
    - Origem da visita (ex: referencia=google)



### Bibliotecas utilizadas

Para esse trabalho foi utilizado o _microframework_ ``Flask``. Para instalar, é necessário rodar o código
> ``pip install Flask`` 
Ele é um WSGI leve que foi designado para começar aplicações rapidamente e que possam ser escaladas para outras de maior complexidades

Além disso, o programa foi rodado em um ambiente virtual `.venv`.