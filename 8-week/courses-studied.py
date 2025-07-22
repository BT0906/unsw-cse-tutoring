#!/usr/bin/env python3

import sys
import psycopg2

### Constants
USAGE = f"Usage: {sys.argv[0]} studentID term"

def main(db):
    ### Command-line args
    if len(sys.argv) != 3:
        print(USAGE)
        return 1

    student_id = sys.argv[1]
    term_code = sys.argv[2]

    cur = db.cursor()

    # check if the student exists
    query = """
      SELECT id
      FROM Students
      WHERE id = %s
    """
    cur.execute(query, [student_id])

    student = cur.fetchone()

    if student is None:
        print("No such student")
        cur.close()
        return 0
    
    student_id = student[0]


    # Check if the term is valid
    query = """
      SELECT id
      FROM Terms
      WHERE code = %s
    """
    cur.execute(query, [term_code])
    term = cur.fetchone()

    if term is None:
        print("No such term")
        cur.close()
        return 0

    term_id = term[0]

    query = """
      SELECT s.code, s.name
      FROM Courses c
      JOIN Terms t on t.id = c.term
      JOIN Course_enrolments e on c.id = e.course 
      JOIN Subjects s on c.subject = s.id
      WHERE t.id = %s
      AND e.student = %s
      ORDER BY s.code, s.name
    """
    cur.execute(query, [term_id, student_id])

    courses = cur.fetchall()

    for code, title in courses:
        print(code, title)

    cur.close()
    return 0

if __name__ == '__main__':
    exit_code = 0
    db = None
    try:
        db = psycopg2.connect(dbname="uni")
        exit_code = main(db)
    except psycopg2.Error as err:
        print("DB error:", err)
        exit_code = 1
    except Exception as err:
        print("Internal Error:", err)
        raise err
    finally:
        if db is not None:
            db.close()
    sys.exit(exit_code)