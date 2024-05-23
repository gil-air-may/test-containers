CREATE TABLE Tab (
    tab_id INT PRIMARY KEY AUTO_INCREMENT,
    table_number INT NOT NULL,
    is_paid BOOLEAN DEFAULT FALSE,
    items JSON NULL,
    from_day DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_from_day ON Tab (from_day);

CREATE TABLE test (column_1 INT);
INSERT INTO test VALUES (1);

INSERT INTO Tab (table_number,is_paid,items,from_day,created_at) VALUES (1,0,'[{"name": "chicken_salad", "amount": 1}]','2024-05-18','2024-05-18 20:36:42')
