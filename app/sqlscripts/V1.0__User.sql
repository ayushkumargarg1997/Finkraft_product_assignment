CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  password VARCHAR(100),
  phone VARCHAR(100),
  isactive BOOLEAN,
  updatedatetime TIMESTAMP,
  createdatetime TIMESTAMP
);
