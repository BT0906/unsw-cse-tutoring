#!/usr/bin/env python3

import sys
import psycopg2

### Constants
USAGE = f"Usage: {sys.argv[0]} subject term"

def main(db):
    ### Command-line args
    if len(sys.argv) != 3:
        print(USAGE)
        return 1

    subject_code = sys.argv[1]
    term_code = sys.argv[2]

    cur = db.cursor()

    
    # Check the subject code is valid
    query = """
      SELECT id
      FROM Subjects
      WHERE code = %s
    """
    cur.execute(query, [subject_code])
    subject = cur.fetchone()
    if subject is None:
        print(f"Invalid subject {subject_code}")
        cur.close()
        return 0
    subject_id = subject[0]


    # Check if the term is valid
    query = """
      SELECT id
      FROM Terms
      WHERE code = %s
    """
    cur.execute(query, [term_code])
    term = cur.fetchone()
    if term is None:
        print(f"Invalid term {term_code}")
        cur.close()
        return 0
    term_id = term[0]

    # Check if the given course is offered in the given term
    query = """
      SELECT id
      FROM Courses
      WHERE term = %s
      AND subject = %s
    """
    cur.execute(query, [term_id, subject_id])
    row = cur.fetchone()
    if row is None:
       print(f"No offering: {subject_code} {term_code}")
       cur.close()
       return 0 


    query = """
      SELECT s.id, p.family, p.given
      FROM People p
      JOIN Students s on s.id = p.id
      JOIN Course_enrolments e on e.student = s.id
      JOIN Courses c on c.id = e.course
      JOIN Subjects sb on sb.id = c.subject
      JOIN Terms t on t.id = c.term
      WHERE sb.id = %s
      AND t.id = %s
      ORDER BY p.family, p.given
    """
    cur.execute(query, [subject_id, term_id])

    roll = cur.fetchall()

    print(subject_code, term_code)
    for student_id, last_name, first_name in roll:
        print(f"{student_id} {last_name}, {first_name}")

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