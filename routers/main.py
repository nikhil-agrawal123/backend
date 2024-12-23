from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from .. import schemas,models,database
import json

router = APIRouter(prefix="/content",tags=['Content'])

@router.post('/')
def new_user(request:schemas.User,db:Session=Depends(database.get_db)):
    new_content = models.User(
        username = request.username,
        password = request.password
    )
    new_entry = models.Content(
        description = {
  '1': {
    "html": '\n' +
      '    <div class="card" id="card1">\n' +
      '        <div class="card-inner" data-cardNo = "1">\n' +
      '            <div class="card-front">\n' +
      '                <p>1</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>1</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '2': {
    "html": '\n' +
      '    <div class="card" id="card2">\n' +
      '        <div class="card-inner" data-cardNo = "2">\n' +
      '            <div class="card-front">\n' +
      '                <p>2</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>2</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '3': {
    "html": '\n' +
      '    <div class="card" id="card3">\n' +
      '        <div class="card-inner" data-cardNo = "3">\n' +
      '            <div class="card-front">\n' +
      '                <p>3</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>3</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '4': {
    "html": '\n' +
      '    <div class="card" id="card4">\n' +
      '        <div class="card-inner" data-cardNo = "4">\n' +
      '            <div class="card-front">\n' +
      '                <p>4</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>4</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '5': {
    "html": '\n' +
      '    <div class="card" id="card5">\n' +
      '        <div class="card-inner" data-cardNo = "5">\n' +
      '            <div class="card-front">\n' +
      '                <p>5</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>5</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '6': {
    "html": '\n' +
      '    <div class="card" id="card6">\n' +
      '        <div class="card-inner" data-cardNo = "6">\n' +
      '            <div class="card-front">\n' +
      '                <p>6</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>6</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '7': {
    "html": '\n' +
      '    <div class="card" id="card7">\n' +
      '        <div class="card-inner" data-cardNo = "7">\n' +
      '            <div class="card-front">\n' +
      '                <p>7</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>7</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '8': {
    "html": '\n' +
      '    <div class="card" id="card8">\n' +
      '        <div class="card-inner" data-cardNo = "8">\n' +
      '            <div class="card-front">\n' +
      '                <p>8</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>8</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '9': {
    "html": '\n' +
      '    <div class="card" id="card9">\n' +
      '        <div class="card-inner" data-cardNo = "9">\n' +
      '            <div class="card-front">\n' +
      '                <p>9</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>9</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '10': {
    "html": '\n' +
      '    <div class="card" id="card10">\n' +
      '        <div class="card-inner" data-cardNo = "10">\n' +
      '            <div class="card-front">\n' +
      '                <p>10</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>10</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '11': {
    "html": '\n' +
      '    <div class="card" id="card11">\n' +
      '        <div class="card-inner" data-cardNo = "11">\n' +
      '            <div class="card-front">\n' +
      '                <p>11</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>11</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '12': {
    "html": '\n' +
      '    <div class="card" id="card12">\n' +
      '        <div class="card-inner" data-cardNo = "12">\n' +
      '            <div class="card-front">\n' +
      '                <p>12</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>12</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '13': {
    "html": '\n' +
      '    <div class="card" id="card13">\n' +
      '        <div class="card-inner" data-cardNo = "13">\n' +
      '            <div class="card-front">\n' +
      '                <p>13</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>13</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '14': {
    "html": '\n' +
      '    <div class="card" id="card14">\n' +
      '        <div class="card-inner" data-cardNo = "14">\n' +
      '            <div class="card-front">\n' +
      '                <p>14</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>14</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '15': {
    "html": '\n' +
      '    <div class="card" id="card15">\n' +
      '        <div class="card-inner" data-cardNo = "15">\n' +
      '            <div class="card-front">\n' +
      '                <p>15</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>15</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '16': {
    "html": '\n' +
      '    <div class="card" id="card16">\n' +
      '        <div class="card-inner" data-cardNo = "16">\n' +
      '            <div class="card-front">\n' +
      '                <p>16</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>16</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '17': {
    "html": '\n' +
      '    <div class="card" id="card17">\n' +
      '        <div class="card-inner" data-cardNo = "17">\n' +
      '            <div class="card-front">\n' +
      '                <p>17</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>17</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '18': {
    "html": '\n' +
      '    <div class="card" id="card18">\n' +
      '        <div class="card-inner" data-cardNo = "18">\n' +
      '            <div class="card-front">\n' +
      '                <p>18</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>18</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '19': {
    "html": '\n' +
      '    <div class="card" id="card19">\n' +
      '        <div class="card-inner" data-cardNo = "19">\n' +
      '            <div class="card-front">\n' +
      '                <p>19</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>19</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '20': {
    "html": '\n' +
      '    <div class="card" id="card20">\n' +
      '        <div class="card-inner" data-cardNo = "20">\n' +
      '            <div class="card-front">\n' +
      '                <p>20</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>20</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '21': {
    "html": '\n' +
      '    <div class="card" id="card21">\n' +
      '        <div class="card-inner" data-cardNo = "21">\n' +
      '            <div class="card-front">\n' +
      '                <p>21</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>21</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '22': {
    "html": '\n' +
      '    <div class="card" id="card22">\n' +
      '        <div class="card-inner" data-cardNo = "22">\n' +
      '            <div class="card-front">\n' +
      '                <p>22</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>22</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '23': {
    "html": '\n' +
      '    <div class="card" id="card23">\n' +
      '        <div class="card-inner" data-cardNo = "23">\n' +
      '            <div class="card-front">\n' +
      '                <p>23</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>23</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  },
  '24': {
    "html": '\n' +
      '    <div class="card" id="card24">\n' +
      '        <div class="card-inner" data-cardNo = "24">\n' +
      '            <div class="card-front">\n' +
      '                <p>24</p>\n' +
      '            </div>\n' +
      '            <div class="card-back">\n' +
      '                <p>24</p>\n' +
      '            </div>\n' +
      '        </div>\n' +
      '    </div>',
    "claimed": False
  }
}
,
        owner_id = new_content.id
    )
    db.add(new_content)
    db.add(new_entry)
    db.commit()
    db.refresh(new_content)
    return new_content

@router.post('/{id}/content')
def get_content(id:int,request:schemas.Content,db:Session=Depends(database.get_db)):
    id = db.query(models.User).filter(models.User.id == id).first()
    new_content = models.Content(
        description = request.description,
        owner_id = id.id
    )
    db.add(new_content)
    db.commit()
    db.refresh(new_content)
    return new_content

@router.get('/{id}/content')
def get_info(id:int,db:Session=Depends(database.get_db)):
    if not db.query(models.User).filter(models.User.id == id).first():
        return {"message":"User not found"}
    else:
        user_id = db.query(models.User).filter(models.User.id == id).first()
        content = db.query(models.Content).filter(models.Content.owner_id == user_id.id).first()
        return (user_id,content)

@router.put('/{id}/content')
def update_content(id:int,request:schemas.Content,db:Session=Depends(database.get_db)):
    if not db.query(models.User).filter(models.User.id == id).first():
        return {"message":"User not found"}
    else:
        id = db.query(models.Content).filter(models.User.id == id).first()
        id.description = request.description
        db.commit()
        db.refresh(id)
        return id
    
@router.delete('/{id}')
def delete_user(id:int,db:Session=Depends(database.get_db)):
    if not db.query(models.User).filter(models.User.id == id).first():
        return {"message":"User not found"}
    else:
        id = db.query(models.User).filter(models.User.id == id).first()
        db.delete(id)
        db.commit()
        for i in db.query(models.Content).filter(models.Content.owner_id == id.id).all():
            db.delete(i)
            db.commit()        
        return {"message":"Deleted Successfully"}
