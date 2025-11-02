# managers/member_repository.py
from typing import List
from models.member import Member
from interfaces.storage import Storage

class MemberRepository:
    def __init__(self, storage: Storage):
        self.storage = storage

    def load_members(self) -> List[Member]:
        rows = self.storage.load()
        members = []
        for r in rows:

            m = Member(
                student_id=int(r.get("student_id") or r.get("id") or 0),
                family_name=r.get("family_name", ""),
                first_name=r.get("first_name", ""),
                email=r.get("email", ""),
                phone=r.get("phone", ""),
                address=r.get("address", ""),
                join_date=r.get("join_date", ""),
                subscription_status=r.get("subscription_status", ""),
            )
            members.append(m)
        return members

    def save_members(self, members: List[Member]):
        rows = [m.to_dict() for m in members]
        self.storage.save(rows)
