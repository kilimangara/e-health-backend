import logging

from tenacity import (after_log, before_log, retry, stop_after_attempt,
                      wait_fixed)

from app.db.base import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init() -> None:
    try:
        db = SessionLocal()
        # Try to create session to check if DB is awake
        db.execute("SELECT 1")
        db.execute(
            """
        INSERT into users (id, phone, status, parent_user_id) VALUES 
            (1,'79164598151','approved', NULL), (2, '79164598152','approved', 1) ON CONFLICT DO NOTHING; 
        """
        )
        db.execute(
            """
            INSERT INTO analysis (user_id, category_id, comment, created_at) VALUES
            (1, 1, '', '2020-01-01 20:20:20.123123'),
            (1, 1, '', '2020-01-02 20:20:20.123123'),
            (1, 1, '', '2020-01-03 20:20:20.123123'),
            (1, 1, '', '2020-01-04 20:20:20.123123'),
            (1, 1, '', '2020-01-05 20:20:20.123123'),
            (1, 1, '', '2020-01-06 20:20:20.123123'),
            (1, 1, '', '2020-01-07 20:20:20.123123'),
            (1, 1, '', '2020-01-08 20:20:20.123123'),
            (1, 1, '', '2020-01-09 20:20:20.123123'),
            (1, 1, '', '2020-01-10 20:20:20.123123'),
            (1, 1, '', '2020-01-11 20:20:20.123123'),
            (1, 1, '', '2020-01-12 20:20:20.123123'),
            (1, 1, '', '2020-01-13 20:20:20.123123'),
            (1, 1, '', '2020-01-14 20:20:20.123123'),
            (1, 1, '', '2020-01-15 20:20:20.123123'),
            (1, 1, '', '2020-01-16 20:20:20.123123'),
            (1, 1, '', '2020-01-17 20:20:20.123123'),
            (1, 1, '', '2020-01-18 20:20:20.123123'),
            (1, 1, '', '2020-01-19 20:20:20.123123'),
            (1, 1, '', '2020-01-20 20:20:20.123123'),
            (1, 1, '', '2020-01-21 20:20:20.123123'),
            (1, 1, '', '2020-01-22 20:20:20.123123'),
            (1, 1, '', '2020-01-23 20:20:20.123123'),
            (1, 1, '', '2020-01-24 20:20:20.123123');
        """
        )
        db.execute(
            """
        INSERT INTO image_blob (user_id, is_avatar, filename, content_type, check_sum, byte_size, analysis_id, position) VALUES 
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 1, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 1, 1),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 1, 2),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 1, 3),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 1, 4),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 1, 5),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 1, 6),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 1, 7),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 1, 8),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 1, 9),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 1, 10),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 1, 11),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 1, 12),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 1, 13),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 1, 14),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 1, 15),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 1, 16),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 1, 17),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 1, 18),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1,2, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1,3, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1,4, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1,5, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1,6, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1,7, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1,8, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1,9, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 10, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 11, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 12, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 13, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 14, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 15, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 16, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 17, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 18, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 19, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 20, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 21, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 22, 0),
            (1, False, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, 23, 0),
            (1, True, '1/amqdwoqpdow', 'image/jpeg', 'awponwnpioucpoinuawc', 1, NULL, 0);
        """
        )
        db.commit()
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("Initializing service")
    # init()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()
