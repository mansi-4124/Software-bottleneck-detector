from app.db.session import SessionLocal


def test_database_session_creation():
    """
    Verify database session can be created.
    """

    session = SessionLocal()

    assert session is not None

    session.close()