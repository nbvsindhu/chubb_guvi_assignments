from app.models import db, StudentPerformance

def load_to_db(data):
 for _, row in data.iterrows():
     student_performance = StudentPerformance(
         student_id=row['student_id'],
         subject=row['subject'],
         score=row['score'],
         grade=row['grade'],
         date=row['date']
     )
     db.session.add(student_performance)
 db.session.commit()
