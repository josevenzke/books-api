CREATE TABLE IF NOT EXISTS authors (
  id SERIAL PRIMARY KEY,
  name varchar(250) NOT NULL,
  age int NOT NULL
);

CREATE TABLE IF NOT EXISTS books (
  id SERIAL PRIMARY KEY,
  name varchar(250) NOT NULL,
  lenght int NOT NULL,
  genre varchar(100) NOT NULL,
  author_id INT,
  CONSTRAINT fk_author
    FOREIGN KEY(author_id) 
	    REFERENCES authors(id)
);