def convert_score(grade):
    match grade:
        case "A+":
            gpa=4.5
        case "A":
            gpa=4.0
        case "B+":
            gpa=3.5
        case "B":
            gpa=3.0
        case "C+":
            gpa=2.5
        case "C":
            gpa=2.0
        case "D+":
            gpa=1.5
        case "D":
            gpa=1.0
        case "F":
            gpa=0.0
#입력
archive_credit, submit_credit= 0, 0
archive_gpa, submit_gpa = 0,0
credit,gpa = 0,0

while True:
    user_value = input()
    value = int(user_value)
    print("작업을 선택하세요")
    print("1. 입력")
    print("2. 출력")

    match value:
        case 1:
            user_value = input("학점을 입력하세요: ")
            credit += int(user_value)

            user_value = input("평점을 입력하세요")
            gpa += convert_score
            if gpa == 0:
                submit_credit += credit
                submit_gpa += credit*gpa
            archive_credit +=credit
            archive_gpa += gpa
        case 2:
            print("")
            print("")
            break
