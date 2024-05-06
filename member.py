from dataclasses import dataclass


@dataclass
class Member:
    name: str
    telno: str
    email: str
    note: str

    @classmethod
    def parse_list(cls, l: list[str]):
        [enroll_date, name, surname, mobile_number, student_id, department, degree,
         ukd, elo, is_paid, is_added_to_group] = l

        if is_added_to_group == "1" or is_added_to_group == "-1":
            return None

        note = f"{student_id} {department} {degree}"

        name = f"HUSAT {name.strip().title()} {surname.strip().title()}"

        telno = mobile_number.replace(" ", "")
        if telno.startswith("5"):
            telno = "+90" + telno
        elif telno.startswith("0"):
            telno = "+9" + telno
        elif telno.startswith("9"):
            telno = "+" + telno

        return cls(name, telno, "", note)

    def __repr__(self) -> str:
        return f"'{self.name}','{self.telno}','{self.email}','{self.note}'\n"

    def __str__(self) -> str:
        return self.__repr__()
