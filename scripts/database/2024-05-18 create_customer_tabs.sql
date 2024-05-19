CREATE TABLE Tab (
    tab_id INT PRIMARY KEY AUTO_INCREMENT,
    table_number INT NOT NULL,
    is_paid BOOLEAN DEFAULT FALSE,
    items JSON NULL,
    from_day DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_from_day ON Tab (from_day);
