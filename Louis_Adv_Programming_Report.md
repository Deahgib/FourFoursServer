Four fours server 
---------------------------------------------------

Advanced Programming - Goldsmiths
---------------------------------

*Louis Bennette*
 
Webpage: http://bennette.co.uk/FourFours/Index.php

Github Server: https://github.com/Deahgib/FourFoursServer 

Github App: https://github.com/Deahgib/FourFours 

The FourFours game is a personal project of mine. It’s an app of a mathematical puzzle game. The game requires the user to find a solution for a given integer using exactly four 4s. The player can use as many parentheses and operators as they need to find a solution. They can also concatenate the digits of 4 together as long as only 4 digits are used. 
For example: 1 = (4/4)/(4/4) or 1 = 44 / 44.
In 1892 the game was proposed in a scientific magazine publication. A solution for all integers was later discovered using a formula. This formula uses square roots which I deem an unfair operation, as fourth roots or 44th roots are more acceptable. 
However, many solutions exist without the formula. 

There is a large set of possible solutions for each integer. The aim of the server project is to log and record all the possible solutions. 
The app is designed in untiy3D, it’s a 2D game made using unity widgets. I consider the app a second project but it is included for context. The app uses TCP sockets to connect to a server and send a custom byte array packet data.
The server’s job is to receive the byte array, validate, parse and insert new solutions to the database.
 
**The server**
The server is written in python, this gives me access to sockets and to SQLite very easily. 
The server uses separate threads from a thread pool to handle new packet data. To do so the server listens for requests on it’s own thread. When a connection is received, a tread is used from the pool and the new data is passed to it for parsing.
The packet is structured as follows:

| Type | Size (bytes)  | Description  |
|---|---|---|
| byte array  |  16 |  Greeting packet for validation: 01 f2 83 e1 a3 44 da b7 af f4 d6 69 ca c9 01 00  |
|  char | 1  |  Game mode |
|  int | 4  |  Solution target |
|  char |  1 | Character length of solution string  |
|  string | 4 - 256  | Solution string (equation)  |

 
 
The server does not send a response to the client as TCP packet data ensures a connection in the TCP layer. The server just determines if the data is valid and if it is, it will attempt to add anything new and unique to the SQLite .db database file.
The parsing thread will first check that the first 16 bytes are equal to the greeting byte array. If at any point the data is incorrect the packet is discarded and the thread is added back to the pool.
The parsing process extracts the raw byte data and casts the data to it’s appropriate type. 
When the variables are ready and manipulable in python the database is queried.
The SQL table is a simple structure and is constructed as follows:

    CREATE TABLE IF NOT EXISTS results ( 
      solution_id INTEGER PRIMARY KEY AUTOINCREMENT,
      game_mode VARCHAR(1), 
      target INTEGER, 
      solution VARCHAR(255)
    );

When data is inserted into the database as check is needed to not add duplicate solutions to the database. As there could be multiple solutions for each integer target. The insertion query is as follows:

    INSERT INTO results (game_mode, target, solution) 
      SELECT 'game_mode_var', target_var, 'solution_var'
        WHERE NOT EXISTS
          ( SELECT 1 FROM results WHERE
            target = target_var 
            AND solution = 'solution_var')

 
**The webpage**
The website is constructed in php7, which has SQLite support.  The website connects to the same .db file to retrieve the data. Currently a simple webpage with a simple query is used to display the data. The php7 script simply grabs the whole table as an array of rows and each row is created using html table <tr> tags injected as an echo string to the html body.
The whole project is currently running on my personal server (hosted by Digitalocean) and the webpage link is under the title of this report.


**The app**
The app is implemented primarily using an implementation of the shunting yard algorithm, this takes a regular mathematical expression eg. 4 + 4 * (4 + 4) and turns it into a reverse polish (RP) expression  4 4 4 4 + * +. The RP expression is stored as two stacks, the tokens and the operators. Then to evaluate I simply pop the operator on the top of the stack. Then the appropriate number of tokens for that operator are popped off the token stack eg. factorial only requires one token and multiplication requires two tokens.
