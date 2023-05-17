from src.api_hh import HeadHunterAPI
from src.dbmanager import DBManager


if __name__ == '__main__':
    hh = HeadHunterAPI()
    companies, vacancies = hh.get_vacancies('', 2)
    db_test = DBManager()
    db_test.clean()
    db_test.add_companies(companies)
    db_test.add_vacancies(vacancies)
    ans1 = db_test.get_companies_and_vacancies_count()
    for i in ans1:
        print(i)
    print('_______________________________')
    ans2 = db_test.get_all_vacancies()
    for i in ans2:
        print(i)
    print('_______________________________')
    ans3 = db_test.get_avg_salary()
    print(ans3)
    print('_______________________________')
    ans4 = db_test.get_vacancies_with_higher_salary()
    for i in ans4:
        print(i)
    print('_______________________________')
    ans5 = db_test.get_vacancies_with_keyword('чатов')
    for i in ans5:
        print(i)
    db_test.close()