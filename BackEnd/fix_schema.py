import database
from sqlalchemy import text


def run():
    with database.engine.begin() as conn:
        conn.execute(
            text("ALTER TABLE users ADD COLUMN IF NOT EXISTS name VARCHAR(255) NOT NULL DEFAULT ''")
        )
        conn.execute(
            text("UPDATE users SET name = username WHERE name IS NULL OR name = ''")
        )
        rows = conn.execute(text("SHOW COLUMNS FROM users")).fetchall()
        print(rows)


if __name__ == "__main__":
    run()
