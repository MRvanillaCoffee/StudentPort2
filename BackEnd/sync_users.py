import database
from sqlalchemy import text


def run():
    with database.engine.begin() as conn:
        conn.execute(
            text("UPDATE users SET password='1234', name='แอดมิน (แก้ไขได้)' WHERE username='admin'")
        )

        exists = conn.execute(
            text("SELECT COUNT(*) FROM users WHERE username='psp'")
        ).scalar()

        if exists == 0:
            conn.execute(
                text(
                    "INSERT INTO users (username, password, email, role, created_at, name) "
                    "VALUES ('psp', '1234', 'psp@student.local', 'viewer', NOW(), 'คุณ psp (ดูได้อย่างเดียว)')"
                )
            )
        else:
            conn.execute(
                text("UPDATE users SET password='1234', role='viewer', name='คุณ psp (ดูได้อย่างเดียว)' WHERE username='psp'")
            )

        rows = conn.execute(text("SELECT id, username, password, role, name FROM users")).fetchall()
        print(rows)


if __name__ == '__main__':
    run()
