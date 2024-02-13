# 블록리스트 관리 파일

BLOCKLIST = set()


def add_to_blocklist(jt1):
    BLOCKLIST.add(jt1)


def remove_from_blocklist(jt1):
    BLOCKLIST.discard(jt1)
