# import strawberry
# from typing import Optional, List
# from enum import Enum

# @strawberry.type
# class Department:
#     id: strawberry.ID
#     name: str
#     municipalities: Optional[List['Municipality']]

# @strawberry.type
# class Municipality:
#     id: strawberry.ID
#     name: str
#     institutions: Optional[List['Institution']]

# @strawberry.enum
# class ReportType(Enum):
#     SABER11 = 'SABER11'
#     SABERPRO = 'SABERPRO'

# @strawberry.type
# class InstitutionInfo:
#     isBilingual: Optional[bool]

# @strawberry.type
# class Institution:
#     id: strawberry.ID
#     name: str
#     period: str
#     type: ReportType
#     info: Optional[InstitutionInfo]
#     students: Optional[List['Student']]

# @strawberry.enum
# class StudentGenre(Enum):
#     Female = "Female"
#     Male = "Male"
#     Other = "Other"

# @strawberry.interface
# class StudentResults:
#     id: strawberry.ID

# @strawberry.type
# class Saber11Results(StudentResults):
#     PUNT_ENGLISH: float
#     PUNT_MATHEMATICS: float
#     PUNT_SOCIAL_CITIZENSHIP: float
#     PUNT_NATURAL_SCIENCES: float
#     PUNT_CRITICAL_READING: float
#     PUNT_GLOBAL: float

# @strawberry.type
# class SaberProResults(StudentResults):
#     MOD_QUANTITATIVE_REASONING: float
#     MOD_WRITTEN_COMMUNICATION: float
#     MOD_CRITICAL_READING: float
#     MOD_ENGLISH: float
#     MOD_CITIZENSHIP_COMPETENCES: float

# @strawberry.type
# class Student:
#     id: strawberry.ID
#     genre: StudentGenre
#     results: StudentResults
