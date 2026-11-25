"""Educational fixture; not a Zimantic runtime integration test."""
import sqlite3,math,tempfile
from pathlib import Path

def test_schema():
    db=sqlite3.connect(':memory:')
    db.executescript("""CREATE VIRTUAL TABLE docs USING fts5(title, lead UNINDEXED, path UNINDEXED, target UNINDEXED, tokenize='unicode61 remove_diacritics 2');
    CREATE TABLE vecs(id INTEGER PRIMARY KEY, v BLOB); CREATE TABLE meta(key TEXT PRIMARY KEY, value);""")
    db.executemany('INSERT INTO docs(rowid,title,lead,path,target) VALUES(?,?,?,?,?)',[(1,'Tetanus','Tetanus is a disease...','A/Tetanus',None),(2,'Lockjaw','','A/Tetanus',1),(3,'Malaria','Malaria is...','A/Malaria',None)])
    assert [r[0] for r in db.execute("SELECT rowid FROM docs WHERE docs MATCH 'Lockjaw'")]==[2]
    # UNINDEXED lead is not full-text searchable by its content:
    assert db.execute("SELECT count(*) FROM docs WHERE docs MATCH 'disease'").fetchone()[0]==0
    row=db.execute('SELECT target FROM docs WHERE rowid = 2').fetchone()
    assert row[0]==1
    return {'docs':db.execute('SELECT count(*) FROM docs').fetchone()[0],'redirect_target':row[0]}

def test_rrf():
    A=1/60+1/62; B=3/61
    assert B>A and abs(A-0.03279569892473118)<1e-12
    assert abs(B-0.04918032786885246)<1e-12
    return {'A':round(A,6),'B':round(B,6),'winner':'B'}

def test_index_selection():
    def choice(n):return 'flat' if n<10000 else f'IVF{int(4*n**.5)},SQ8'
    assert choice(9999)=='flat'
    assert choice(10000)=='IVF400,SQ8'
    assert choice(70000)=='IVF1058,SQ8'
    return {'9999':choice(9999),'10000':choice(10000),'70000':choice(70000)}

if __name__=='__main__':
    import json
    print(json.dumps({'schema':test_schema(),'rrf':test_rrf(),'index':test_index_selection()},indent=2))
