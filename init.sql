CREATE TABLE movie_categories (
    id SERIAL PRIMARY KEY,
    category VARCHAR(255) NOT NULL,
    rating INTEGER NOT NULL
);

INSERT INTO movie_categories (category, rating) VALUES
('Action', 5),
('Comedy', 4),
('Drama', 5),
('Fantasy', 4),
('Horror', 3),
('Romance', 4);

